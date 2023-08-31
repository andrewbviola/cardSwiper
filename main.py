import time
import os
import platform
import pandas as pd
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

    x = time.localtime()
    currentTime = time.strftime("%H:%M", x)
    currentDate = date.today()

    if (pid == "QUIT"):
        checkForDate = pd.read_excel(entranceData[0], sheet_name=entranceData[1])
        wb1 = load_workbook(entranceData[0])
        ws1 = wb1[entranceData[1]]
        currentDate = currentDate.strftime("%Y-%m-%d")
        checkForDate['Date'] = checkForDate['Date'].astype(str)
        containsDate = checkForDate[checkForDate['Date']==currentDate]

        numRows = containsDate.shape[0]
        
        for i in range(numRows):
            currentRow = containsDate.iloc[[i]]
            if currentRow["Time Out"].to_string(index=False) == "NaN":
                indexCell = currentRow.index.item() + 2
                cell = ws1.cell(row=indexCell, column=3)
                cell.value = currentTime
                wb1.save(entranceData[0])  
        exit()
        
    pid = pid[1:10]

    if len(pid) !=9: # Return error if the full 9 digits weren't grabbed properly
        print("Card read error try again")
        time.sleep(5)
    else:
        os.system(clearMethod)

        # Load an existing database of student information

        data = pd.read_excel(studentData[0], sheet_name=studentData[1])
        wb = load_workbook(studentData[0])
        ws = wb[studentData[1]]
        data['PID'] = data['PID'].astype(str)
        containsPID = data[data['PID']==pid]

        # If the user isn't in the database, create a new user with the following info

        if containsPID.empty:
            print("We couldn't find your information please fill out the following (Case Sensitive):")
            firstName = input("First Name: ")
            lastName = input("Last Name: ")
            email = input("Email: ")
            community = input("Community (Galileo, Hypatia, Other, N/A): ")
            year = input("Year (Freshman, Sophomore, Junior, Senior, Graduate): ")

            newData = {"PID": [pid], "First Name": [firstName], "Last Name": [lastName], "Email": [email], "Community": [community],"Year": [year]}
            newDataFrame = pd.DataFrame(newData)
            max_row = ws.max_row
            for row_idx, row in newDataFrame.iterrows():
                values = row.values
                for col_idx, value in enumerate(values, start=1):
                    ws.cell(row=max_row + row_idx + 1, column=col_idx, value=value)
            wb.save(studentData[0])

        # Grab the information of the existing user otherwise

        else:
            firstName = containsPID["First Name"].to_string(index=False)
            lastName = containsPID["Last Name"].to_string(index=False)
            email = containsPID["Email"].to_string(index=False)
            community = containsPID["Community"].to_string(index=False)
            year = containsPID["Year"].to_string(index=False)
            cnc = containsPID["CNC"].to_string(index=False)
            lc = containsPID["Laser Cutter"].to_string(index=False)
            sold = containsPID["Soldering"].to_string(index=False)
            pt = containsPID["Power Tools"].to_string(index=False)

        # Load current attendance sheet

        checkForSignIn = pd.read_excel(entranceData[0], sheet_name=entranceData[1])
        wb1 = load_workbook(entranceData[0])
        ws1 = wb1[entranceData[1]]

        checkForSignIn['ID Number'] = checkForSignIn['ID Number'].astype(str)
        containsPID2 = checkForSignIn[checkForSignIn['ID Number']==pid]

        if containsPID2.empty:
            print("Signing in")
            newEntry = {"Date": [currentDate], "Time In": [currentTime], "Time Out": [""], "ID Number": [pid], "First Name": [firstName], "Last Name": [lastName], "Email": [email], "Community": [community],"Year": [year]}
            newEntryFrame = pd.DataFrame(newEntry)
            max_row2 = ws1.max_row
            for row_idx, row in newEntryFrame.iterrows():
                values = row.values
                for col_idx, value in enumerate(values, start=1):
                    ws1.cell(row=max_row2 + row_idx + 1, column=col_idx, value=value)
            wb1.save(entranceData[0])
        else:

            lastRow = containsPID2.tail(1)
            indexCell = lastRow.index.item() + 2 

            if lastRow["Time Out"].to_string(index=False) == "NaN":
                print("Signing out:", firstName, lastName, "at", currentTime)
                cell = ws1.cell(row=indexCell, column=3)
                cell.value = currentTime
                wb1.save(entranceData[0])
            else:
                print("Signing in:", firstName, lastName,"at", currentTime)
                trainedTools = {"CNC": [cnc], "Laser Cutter": [lc], "Soldering": [sold], "Power Tools": [pt]}
                dataTrained = pd.DataFrame(trainedTools)
                print(firstName, "is trained on the following tools:")
                print(dataTrained)
                newEntry = {"Date": [currentDate], "Time In": [currentTime], "Time Out": [""], "ID Number": [pid], "First Name": [firstName], "Last Name": [lastName], "Email": [email], "Community": [community],"Year": [year]}
                newEntryFrame = pd.DataFrame(newEntry)
                max_row2 = ws1.max_row
                for row_idx, row in newEntryFrame.iterrows():
                    values = row.values
                    for col_idx, value in enumerate(values, start=1):
                        ws1.cell(row=max_row2 + row_idx + 1, column=col_idx, value=value)
                wb1.save(entranceData[0])
            
            time.sleep(5)
