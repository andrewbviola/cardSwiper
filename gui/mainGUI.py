import tkinter as tk
import helpers as hp
import os
import time

# ;906383023=0249? Fake
# ;906383024=0249? Real

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Create a root
root = tk.Tk()
root.resizable(False, False)

width = 600
height = 500
studentData = ["UserInfo.xlsx","Sheet1"] # Database of existing inVenTs users
entranceData = ["EntranceInfo.xlsx", "Sheet1"] # Attendance log sheet
currentCanvas = "mainMenuCanvas"
pid = ""
firstName = ""
lastName = ""
email = ""
community = ""
year = ""
cnc = ""
lc = ""
sold = ""
pt = ""


# Set initial size
mainMenuCanvas = tk.Canvas(root, width=width, height=height)
signInCanvas = tk.Canvas(root, width=width, height=height)
fillOutCanvas = tk.Canvas(root, width=width, height=height)
cardReadErrorCanvas = tk.Canvas(root, width=width, height=height)
confirmedSignInCanvas = tk.Canvas(root, width=width, height=height)

# Photo Buttons
photo = __location__ + r"\assets\ConfirmBase.png"
confirmBasePhoto = tk.PhotoImage(file=(photo))
photo = __location__ + r"\assets\CancelBase.png"
cancelBasePhoto = tk.PhotoImage(file=(photo))

# Background color
mainMenuCanvas.configure(bg="#C64600")
signInCanvas.configure(bg="#FFE484")
fillOutCanvas.configure(bg="#FFE484")
cardReadErrorCanvas.configure(bg="#F74242")
confirmedSignInCanvas.configure(bg="#00C667")

# Top Bar
hp.topBar(mainMenuCanvas,width, height)
hp.topMessage(mainMenuCanvas,width,height, "We're glad you're here", "white")
hp.middleMessage(mainMenuCanvas,width,height, "Swipe your Hokie P", "white")
hp.topBar(signInCanvas,width, height)
hp.topBar(cardReadErrorCanvas,width, height)
hp.topMessage(cardReadErrorCanvas,width,height, "Press \"enter\" to return to the main menu", "black")
hp.middleMessage(cardReadErrorCanvas,width,height, "Card Reader Error", "black")
signInCanvas.create_text(width/2,140,font=("Roboto Mono",42),text="Signing in:",fill="black")

# Buttons
confirm = tk.Label(signInCanvas, bg="#FFE484", image = confirmBasePhoto, bd = 0)
confirm.place(x=12.0,y=380.0,width=231.25,height=50.0)
cancel = tk.Label(signInCanvas, bg="#FFE484", image = cancelBasePhoto, bd = 0)
cancel.place(x=width-243.25,y=380.0,width=231.25,height=50.0)


# Time and Date
timer = tk.Label(root)
date = tk.Label(root)
timer.pack()
date.pack()

def clock():
    color, textColor = hp.determineBG(currentCanvas)
    timer.config(font=("Roboto Mono",24,),text=hp.guiTime(),bg=color,fg=textColor)
    timer.place(x=width-160,y=height-47)
    date.config(font=("Roboto Mono",24,),text=hp.guiDate(),bg=color,fg=textColor)
    date.place(x=width-(width-5),y=height-47)
    root.after(250,clock)
    
def idNum(event):
    global pid
    if event.char == "Return":
        return
    pid = pid + event.char
  
def swipe(event):
    currentTime, currentDate = hp.timeDate()
    global pid, firstName, lastName, email, community, year, cnc, lc, sold, pt, currentCanvas
    if (pid == "QUIT"):
        checkForDate, wb1, ws1 = hp.loadExcel(entranceData[0],entranceData[1])
        hp.autoFillSignOut(checkForDate,entranceData[0],ws1,wb1, currentTime, currentDate)
        exit()
        
    pid = pid[1:10]

    if len(pid) !=9: # Return error if the full 9 digits weren't grabbed properly
        mainMenuCanvas.forget()
        cardReadErrorCanvas.pack()
        currentCanvas = "cardReadErrorCanvas"
        cardReadErrorCanvas.focus_set()
    else:
        # Load an existing database of student information
        data, wb, ws = hp.loadExcel(studentData[0],studentData[1])
        data['PID'] = data['PID'].astype(str)
        containsPID = data[data['PID']==pid]

        # If the user isn't in the database, create a new user with the following info
        if containsPID.empty:
            # TODO Implement fill in screen
            exit()

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
                print("Signed Out")
            
            else: # Otherwise make a new row with all the info    
                mainMenuCanvas.forget()
                name = firstName + " " + lastName
                signInCanvas.create_text(width/2,200,font=("Roboto Mono",42),text=name,fill="black")
                signInCanvas.pack()
                currentCanvas = "signInCanvas"
                signInCanvas.focus_set()

def returnMain(event):
    global pid, currentCanvas
    pid = ""
    signInCanvas.forget()
    confirmedSignInCanvas.forget()
    mainMenuCanvas.pack()
    currentCanvas = "mainMenuCanvas"
    mainMenuCanvas.focus_set()
    
def returnFromError(event):
    global pid, currentCanvas
    pid = ""
    cardReadErrorCanvas.forget()
    mainMenuCanvas.pack()
    currentCanvas = "mainMenuCanvas"
    mainMenuCanvas.focus_set()
    
def signInConfirmed():
    global currentCanvas, firstName, lastName, email, community, year, pid, cnc, lc, sold, pt, entranceData
    currentTime, currentDate = hp.timeDate()
    checkForSignIn, wb1, ws1 = hp.loadExcel(entranceData[0],entranceData[1])
    hp.signIn(firstName, lastName, email, community, year, pid, currentTime, currentDate, cnc, lc, sold, pt, ws1, wb1, entranceData[0])    
    signInCanvas.forget()
    confirmedSignInCanvas.pack()
    currentCanvas = "confirmedSignInCanvas"
    confirmedSignInCanvas.focus_set()
    time.sleep(2)
    returnMain(True)
    
def confirmBut(event):
    if currentCanvas == "signInCanvas":
        signInConfirmed()

def cancelBut(event):
    returnMain(True)
    
clock()

mainMenuCanvas.pack()
currentCanvas = "mainMenuCanvas"
mainMenuCanvas.focus_set()

confirm.bind("<Button-1>", confirmBut)
cancel.bind("<Button-1>", cancelBut)
mainMenuCanvas.bind("<Key>",idNum)
mainMenuCanvas.bind("<Return>",swipe)
cardReadErrorCanvas.bind("<Return>",returnFromError)

# Create a mainloop
tk.mainloop()
