import time
import os
import platform
import pandas as pd
import helpers as hp
from datetime import date
from openpyxl import load_workbook

# ;906383023=0249? Fake
# ;906383024=0249? Real


studentData = ["UserInfo.xlsx","Sheet1"] # Database of existing inVenTs users
entranceData = ["EntranceInfo.xlsx", "Sheet1"] # Attendance log sheet

opsys = platform.system()
if opsys == "Windows":
    clearMethod = "cls"
else:
    clearMethod = "clear"


while True:
    os.system(clearMethod)
    pid = input("Swipe your card: ") # Grabs the 9 digit PID

    currentTime, currentDate = hp.timeDate()

    if (pid == "QUIT"):
        checkForDate, wb1, ws1 = hp.loadExcel(entranceData[0],entranceData[1])
        hp.autoFillSignOut(checkForDate,entranceData[0],ws1,wb1, currentTime, currentDate)
        exit()
        
    pid = pid[1:10]

    if len(pid) !=9: # Return error if the full 9 digits weren't grabbed properly
        print("Card read error try again")
        time.sleep(5)
    else:
        os.system(clearMethod)

        # Load an existing database of student information
        data, wb, ws = hp.loadExcel(studentData[0],studentData[1])
        data['PID'] = data['PID'].astype(str)
        containsPID = data[data['PID']==pid]

        # If the user isn't in the database, create a new user with the following info
        if containsPID.empty:
            firstName, lastName, email, community, year = hp.addNewUser(pid, studentData[0], ws, wb)

        else: # Grab the information of the existing user otherwise
            firstName, lastName, email, community, year, cnc, lc, sold, pt = hp.grabData(containsPID)

        # Load current attendance sheet
        checkForSignIn, wb1, ws1 = hp.loadExcel(entranceData[0],entranceData[1])

        checkForSignIn['ID Number'] = checkForSignIn['ID Number'].astype(str)
        containsPID2 = checkForSignIn[checkForSignIn['ID Number']==pid]

        if containsPID2.empty: # Brand new users won't have trainings use this guy
            hp.firstSignIn(currentDate, currentTime, pid, firstName, lastName, email, community, year, ws1, wb1, entranceData[0])
        else:

            # Find the last row of the excel sheet with the PID
            lastRow = containsPID2.tail(1)
            indexCell = lastRow.index.item() + 2 

            # If the PID exists and there is an available Time Out field, fill that out
            if lastRow["Time Out"].to_string(index=False) == "NaN":
                hp.signOut(firstName, lastName, currentTime, indexCell, ws1, wb1, entranceData[0])
            else: # Otherwise make a new row with all the info
                hp.signIn(firstName, lastName, email, community, year, pid, currentTime, currentDate, cnc, lc, sold, pt, ws1, wb1, entranceData[0])
            
        time.sleep(5)
