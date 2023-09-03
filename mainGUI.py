import tkinter as tk
import helpers as hp
import os
import time

# ;906383023=0249? Test Test
# ;906383024=0249? Andrew Viola
# ;906383055=0249? Fill in user tester

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

width = 600
height = 500
studentData = ["UserInfo.xlsx","Sheet1"] # Database of existing inVenTs users
entranceData = ["EntranceInfo.xlsx", "Sheet1"] # Attendance log sheet
currentCanvas = "mainMenuCanvas"
fullName = ""
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

# Create a root
root = tk.Tk()
root.resizable(False, False)
root.title("inVenTs Studio Sign In/Out")

# Set initial size
mainMenuCanvas = tk.Canvas(root, width=width, height=height)
signInCanvas = tk.Canvas(root, width=width, height=height)
fillOutCanvas = tk.Canvas(root, width=width, height=height)
cardReadErrorCanvas = tk.Canvas(root, width=width, height=height)
confirmedSignInCanvas = tk.Canvas(root, width=width, height=height)
signOutCanvas = tk.Canvas(root, width=width, height=height)
confirmedSignOutCanvas = tk.Canvas(root, width=width, height=height)
manualEntryCanvas = tk.Canvas(root, width=width, height=height)

# Photo Buttons
photo = __location__ + r"/assets/ConfirmBase.png"
confirmBasePhoto = tk.PhotoImage(file=(photo))
photo = __location__ + r"/assets/CancelBase.png"
cancelBasePhoto = tk.PhotoImage(file=(photo))
photo = __location__ + r"/assets/smallTextEntry.png"
smallTextPhoto = tk.PhotoImage(file=photo)
photo = __location__ + r"/assets/CNCicon.png"
cncPhoto = tk.PhotoImage(file=photo)
photo = __location__ + r"/assets/LCicon.png"
lcPhoto = tk.PhotoImage(file=photo)
photo = __location__ + r"/assets/PTicon.png"
ptPhoto = tk.PhotoImage(file=photo)
photo = __location__ + r"/assets/Sicon.png"
sPhoto = tk.PhotoImage(file=photo)
photo = __location__ + r"/assets/check.png"
checkPhoto = tk.PhotoImage(file=photo)
photo = __location__ + r"/assets/x.png"
xPhoto = tk.PhotoImage(file=photo)
photo = __location__ + r"/assets/icon.png"
iconPhoto = tk.PhotoImage(file=photo)
photo = __location__ + r"/assets/plus.png"
plusPhoto = tk.PhotoImage(file=photo)
photo = __location__ + r"/assets/exit.png"
exitPhoto = tk.PhotoImage(file=photo)
photo = __location__ + r"/assets/longTextEntry.png"
longTextPhoto = tk.PhotoImage(file=photo)
photo = __location__ + r"/assets/Enter.png"
enterPhoto = tk.PhotoImage(file=photo)
photo = __location__ + r"/assets/Return.png"
returnPhoto = tk.PhotoImage(file=photo)

# Set window icon
root.iconphoto(False, iconPhoto)

# Background color
mainMenuCanvas.configure(bg="#C64600")
signInCanvas.configure(bg="#FFE484")
fillOutCanvas.configure(bg="#FFE484")
cardReadErrorCanvas.configure(bg="#F74242")
confirmedSignInCanvas.configure(bg="#00C667")
confirmedSignOutCanvas.configure(bg="#00C667")
signOutCanvas.configure(bg="#FFE484")
manualEntryCanvas.configure(bg="#C64600")


# Text
hp.topBar(mainMenuCanvas,width, height)
hp.topBar(manualEntryCanvas,width, height)
hp.topBar(fillOutCanvas,width, height)
hp.topBar(confirmedSignInCanvas,width, height)
hp.topBar(confirmedSignOutCanvas,width, height)
hp.topBar(signOutCanvas,width, height)
hp.topMessage(mainMenuCanvas,width,height, "We're glad you're here", "white")
hp.topMessage(manualEntryCanvas,width,height, "Please type in your 9 digit ID number below", "white")
hp.topMessage(confirmedSignInCanvas,width,height, "Click anywhere to return to the main menu", "black")
hp.topMessage(confirmedSignOutCanvas,width,height, "Click anywhere to return to the main menu", "black")
hp.middleMessage(mainMenuCanvas,width,height, "Swipe your Hokie P", "white")
hp.topBar(signInCanvas,width, height)
hp.topBar(cardReadErrorCanvas,width, height)
hp.topMessage(cardReadErrorCanvas,width,height, "Click anywhere to return to the main menu", "black")
hp.middleMessage(cardReadErrorCanvas,width,height, "Card Reader Error", "black")
signInCanvas.create_text(width/2,85,font=("Roboto Mono",42),text="Signing in:",fill="black")
confirmedSignInCanvas.create_text(width/2,height/2 - 30,font=("Roboto Mono",42),text="Thank you for",fill="black")
signOutCanvas.create_text(width/2,height/2 - 40,font=("Roboto Mono",42),text="Signing out:",fill="black")
confirmedSignInCanvas.create_text(width/2,height/2 + 30,font=("Roboto Mono",42),text="signing in!",fill="black")
confirmedSignOutCanvas.create_text(width/2,height/2 - 30,font=("Roboto Mono",42),text="Thank you for",fill="black")
confirmedSignOutCanvas.create_text(width/2,height/2 + 30,font=("Roboto Mono",42),text="signing out!",fill="black")
fillOutCanvas.create_text(width-70,185,font=("Roboto Mono",16),text="Last Name",fill="black")
fillOutCanvas.create_text(width-(width-75),185,font=("Roboto Mono",16),text="First Name",fill="black")
fillOutCanvas.create_text(width-(width-75),285,font=("Roboto Mono",16),text="Email",fill="black")
fillOutCanvas.create_text(width-70,285,font=("Roboto Mono",16),text="LLC",fill="black")
fillOutCanvas.create_text((width/2),285,font=("Roboto Mono",16),text="Class Year",fill="black")
fillOutCanvas.create_text(width/2,100,font=("Roboto Mono",36),text="New User",fill="black")
manualEntryCanvas.create_text(width/2,200,font=("Roboto Mono",36),text="Manual Login",fill="White")
mainMenuCanvas.create_text(width/2,485,font=("Roboto Mono",8),text="designed by av",fill="White")

# Buttons
manualEntry = tk.Label(mainMenuCanvas, bg="#C64600", image = plusPhoto, bd = 0)
manualEntry.place(x=width-51,y=51.0,width=50,height=50.0)
exitBut = tk.Label(mainMenuCanvas, bg="#C64600", image = exitPhoto, bd = 0)
exitBut.place(x=1,y=51,width=50,height=50.0)
confirm = tk.Label(signInCanvas, bg="#FFE484", image = confirmBasePhoto, bd = 0)
confirm.place(x=12.0,y=380.0,width=231.25,height=50.0)
cancel = tk.Label(signInCanvas, bg="#FFE484", image = cancelBasePhoto, bd = 0)
cancel.place(x=width-243.25,y=380.0,width=231.25,height=50.0)
confirm1 = tk.Label(signOutCanvas, bg="#FFE484", image = confirmBasePhoto, bd = 0)
confirm1.place(x=12.0,y=380.0,width=231.25,height=50.0)
cancel1 = tk.Label(signOutCanvas, bg="#FFE484", image = cancelBasePhoto, bd = 0)
cancel1.place(x=width-243.25,y=380.0,width=231.25,height=50.0)
confirm2 = tk.Label(fillOutCanvas, bg="#FFE484", image = confirmBasePhoto, bd = 0)
confirm2.place(x=12.0,y=380.0,width=231.25,height=50.0)
cancel2 = tk.Label(fillOutCanvas, bg="#FFE484", image = cancelBasePhoto, bd = 0)
cancel2.place(x=width-243.25,y=380.0,width=231.25,height=50.0)
enterBut = tk.Label(manualEntryCanvas, bg="#C64600", image = enterPhoto, bd = 0)
enterBut.place(x=12.0,y=380.0,width=231.25,height=50.0)
returnBut = tk.Label(manualEntryCanvas, bg="#C64600", image = returnPhoto, bd = 0)
returnBut.place(x=width-243.25,y=380.0,width=231.25,height=50.0)

# Entry Boxes
firstNameEntryImage  = fillOutCanvas.create_image(width-(width-20)+54,223.0,image=smallTextPhoto)
firstNameEntry = tk.Entry(fillOutCanvas, bd=0,bg="#BA5375",fg="#000716",highlightthickness=0)
firstNameEntry.place(x=width-(width-20),y=200.0,width=108.0,height=38.0)

lastNameEntryImage  = fillOutCanvas.create_image(width-123+54,223.0,image=smallTextPhoto)
lastNameEntry = tk.Entry(fillOutCanvas, bd=0,bg="#BA5375",fg="#000716",highlightthickness=0)
lastNameEntry.place(x=width-123,y=200.0,width=108.0,height=38.0)

emailEntryImage  = fillOutCanvas.create_image(width-(width-20)+54,323.0,image=smallTextPhoto)
emailEntry = tk.Entry(fillOutCanvas, bd=0,bg="#BA5375",fg="#000716",highlightthickness=0)
emailEntry.place(x=width-(width-20),y=300.0,width=108.0,height=38.0)

yearEntryImage  = fillOutCanvas.create_image(width-355+54,323.0,image=smallTextPhoto)
yearEntry = tk.Entry(fillOutCanvas, bd=0,bg="#BA5375",fg="#000716",highlightthickness=0)
yearEntry.place(x=width-355,y=300.0,width=108.0,height=38.0)

communityEntryImage  = fillOutCanvas.create_image(width-123+54,323.0,image=smallTextPhoto)
communityEntry = tk.Entry(fillOutCanvas, bd=0,bg="#BA5375",fg="#000716",highlightthickness=0)
communityEntry.place(x=width-123,y=300.0,width=108.0,height=38.0)

pidEntryImage  = manualEntryCanvas.create_image(300,269.0,image=longTextPhoto)
pidEntry = tk.Entry(manualEntryCanvas, bd=0,bg="#BA5375",fg="#000716",highlightthickness=0)
pidEntry.place(x=151,y=249.0,width=298.0,height=35.0)

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
    
    if currentCanvas != "manualEntryCanvas":
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
            mainMenuCanvas.forget()
            fillOutCanvas.pack()
            currentCanvas = "fillOutCanvas"
            fillOutCanvas.focus_set()

        else: # Grab the information of the existing user otherwise
            firstName, lastName, email, community, year, cnc, lc, sold, pt = hp.grabData(containsPID)
            signInandOut()
            
def signInandOut():
    global pid, firstName, lastName, email, community, year, entranceData, cnc, lc, sold, pt, currentCanvas, fullName, cncPhoto, lcPhoto, sPhoto, ptPhoto, checkPhoto, xPhoto
    currentTime, currentDate = hp.timeDate()
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
            fullName = firstName + " " + lastName
            signOutCanvas.create_rectangle(0, height/2-3, width, height/2+100, fill="#FFE484", outline="#FFE484")
            signOutCanvas.pack()
            signOutCanvas.create_text(width/2,height/2 + 20,font=("Roboto Mono",42),text=fullName,fill="black")
            mainMenuCanvas.forget()
            signOutCanvas.pack()
            currentCanvas = "signOutCanvas"
            signOutCanvas.focus_set()
        
        else: # Otherwise make a new row with all the info    
            mainMenuCanvas.forget()
            fullName = firstName + " " + lastName
            signInCanvas.create_rectangle(0, height/2-127, width, height-200, fill="#FFE484", outline="#FFE484")
            signInCanvas.pack()
            signInCanvas.create_image(75,250,image=cncPhoto)
            signInCanvas.create_image(225,250,image=lcPhoto)
            signInCanvas.create_image(375,250,image=sPhoto)
            signInCanvas.create_image(525,250,image=ptPhoto)
            if cnc == "X":
                signInCanvas.create_image(75,325,image=checkPhoto)
            else:
                signInCanvas.create_image(75,325,image=xPhoto)
            if lc == "X":
                signInCanvas.create_image(225,325,image=checkPhoto)
            else:
                signInCanvas.create_image(225,325,image=xPhoto)
            if sold == "X":
                signInCanvas.create_image(365,325,image=checkPhoto)
            else:
                signInCanvas.create_image(365,325,image=xPhoto)
            if pt == "X":
                signInCanvas.create_image(530,325,image=checkPhoto)
            else:
                signInCanvas.create_image(530,325,image=xPhoto)
            signInCanvas.create_text(width/2,155,font=("Roboto Mono",42),text=fullName,fill="black")
            signInCanvas.pack()
            currentCanvas = "signInCanvas"
            signInCanvas.focus_set()

def returnMain(event):
    global pid, currentCanvas, firstName, lastName, email, community, year, cnc, lc, sold, pt, fullName
    pid, firstName, lastName, email, community, year, cnc, lc, sold, pt, fullName = "", "", "", "", "", "", "", "", "", "", ""
    signInCanvas.forget()
    signOutCanvas.forget()
    fillOutCanvas.forget()
    manualEntryCanvas.forget()
    confirmedSignInCanvas.forget()
    confirmedSignOutCanvas.forget()
    mainMenuCanvas.pack()
    currentCanvas = "mainMenuCanvas"
    mainMenuCanvas.focus_set()
    
def returnFromError(event):
    global pid, currentCanvas, firstName, lastName, email, community, year, cnc, lc, sold, pt, fullName
    pid, firstName, lastName, email, community, year, cnc, lc, sold, pt, fullName = "", "", "", "", "", "", "", "", "", "", ""
    cardReadErrorCanvas.forget()
    confirmedSignInCanvas.forget()
    confirmedSignOutCanvas.forget()
    signInCanvas.forget()
    signOutCanvas.forget()
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
    fillOutCanvas.forget()
    currentCanvas = "confirmedSignInCanvas"
    confirmedSignInCanvas.focus_set()
    
def signOutConfirmed():
    global currentCanvas, firstName, lastName, email, community, year, pid, cnc, lc, sold, pt, entranceData
    currentTime, currentDate = hp.timeDate()
    checkForSignIn, wb1, ws1 = hp.loadExcel(entranceData[0],entranceData[1])
    checkForSignIn['ID Number'] = checkForSignIn['ID Number'].astype(str)
    containsPID2 = checkForSignIn[checkForSignIn['ID Number']==pid]
    lastRow = containsPID2.tail(1)
    indexCell = lastRow.index.item() + 2 
    hp.signOut(firstName, lastName, currentTime, indexCell, ws1, wb1, entranceData[0])   
    signOutCanvas.forget()
    confirmedSignOutCanvas.pack()
    currentCanvas = "confirmedSignOutCanvas"
    confirmedSignOutCanvas.focus_set()
    
def fillOutConfirmed():
    global currentCanvas, firstName, lastName, email, community, year, pid, cnc, lc, sold, pt, entranceData, studentData
    data, wb, ws = hp.loadExcel(studentData[0],studentData[1])
    firstName, lastName, email, community, year = firstNameEntry.get(),lastNameEntry.get(), emailEntry.get(), communityEntry.get(), yearEntry.get()
    hp.addNewUserWithData(firstName, lastName, email, community, year, pid, studentData[0], ws, wb)
    firstNameEntry.delete(0, tk.END),lastNameEntry.delete(0, tk.END), emailEntry.delete(0, tk.END), communityEntry.delete(0, tk.END), yearEntry.delete(0, tk.END)
    signInConfirmed()
    
def confirmBut(event):
    if currentCanvas == "signInCanvas":
        signInConfirmed()
    elif currentCanvas == "signOutCanvas":
        signOutConfirmed()
    elif currentCanvas == "fillOutCanvas":
        fillOutConfirmed()

def cancelBut(event):
    returnMain(True)
    
def test(event):
    global firstName, lastName
    firstName, lastName = firstNameEntry.get(),lastNameEntry.get()
    print(firstName,lastName)
    
def manualEntryCommand(event):
    global currentCanvas
    mainMenuCanvas.forget()
    manualEntryCanvas.pack()
    currentCanvas = "manualEntryCanvas"
    manualEntryCanvas.focus_set()
    
def exitCommand(event):
    currentTime, currentDate = hp.timeDate()
    global entranceData
    checkForDate, wb1, ws1 = hp.loadExcel(entranceData[0],entranceData[1])
    hp.autoFillSignOut(checkForDate,entranceData[0],ws1,wb1, currentTime, currentDate)
    exit()
    
def manualSignIn(event):
    global pid
    pid = ""
    pid = pidEntry.get()
    if len(pid) == 9:
        print(pid)
        manualEntryCanvas.forget()
        pidEntry.delete(0, tk.END)
        swipe(True)
    else:
        print("Not correct size")
    
clock()

mainMenuCanvas.pack()
currentCanvas = "mainMenuCanvas"
mainMenuCanvas.focus_set()

returnBut.bind("<Button-1>", returnMain)
enterBut.bind("<Button-1>", manualSignIn)
exitBut.bind("<Button-1>", exitCommand)
manualEntry.bind("<Button-1>", manualEntryCommand)
confirm.bind("<Button-1>", confirmBut)
cancel.bind("<Button-1>", cancelBut)
confirm1.bind("<Button-1>", confirmBut)
cancel1.bind("<Button-1>", cancelBut)
confirm2.bind("<Button-1>", confirmBut)
cancel2.bind("<Button-1>", cancelBut)
mainMenuCanvas.bind("<Key>",idNum)
mainMenuCanvas.bind("<Return>",swipe)
cardReadErrorCanvas.bind("<Button-1>",returnFromError)
confirmedSignOutCanvas.bind("<Button-1>",cancelBut)
confirmedSignInCanvas.bind("<Button-1>",cancelBut)

# Create a mainloop
tk.mainloop()
