import tkinter as tk
import helpers as hp
import os
import time


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

# Background color
mainMenuCanvas.configure(bg="#C64600")
signInCanvas.configure(bg="#FFE484")
fillOutCanvas.configure(bg="#FFE484")
cardReadErrorCanvas.configure(bg="#F74242")

# Top Bar
hp.topBar(mainMenuCanvas,width, height)
hp.topMessage(mainMenuCanvas,width,height, "We're glad you're here", "white")
hp.middleMessage(mainMenuCanvas,width,height, "Swipe your Hokie P", "white")
hp.topBar(signInCanvas,width, height)
hp.topBar(cardReadErrorCanvas,width, height)
hp.topMessage(cardReadErrorCanvas,width,height, "Press \"enter\" to return to the main menu", "black")
hp.middleMessage(cardReadErrorCanvas,width,height, "Card Reader Error", "black")
signInCanvas.create_text(width/2,200,font=("Roboto Mono",42),text="Signing in:",fill="black")

# Buttons
confirm = tk.Button(signInCanvas, padx=20, pady=20)
confirm.pack()


# Time and Date
timer = tk.Label(root)
date = tk.Label(root)
timer.pack()
date.pack()

def clock():
    color, textColor = hp.determineBG(currentCanvas)
    timer.config(font=("Roboto Mono",24,),text=hp.guiTime(),bg=color,fg=textColor)
    timer.place(x=width-120,y=height-47)
    date.config(font=("Roboto Mono",24,),text=hp.guiDate(),bg=color,fg=textColor)
    date.place(x=width-(width-5),y=height-47)
    root.after(1000,clock)
    
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
        mainMenuCanvas.forget()
        name = firstName + " " + lastName
        signInCanvas.create_text(width/2,height/2,font=("Roboto Mono",42),text=name,fill="black")
        signInCanvas.pack()
        currentCanvas = "signInCanvas"
        signInCanvas.focus_set()

def returnMain(event):
    global pid, currentCanvas
    pid = ""
    signInCanvas.forget()
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

clock()

mainMenuCanvas.pack()
currentCanvas = "mainMenuCanvas"
mainMenuCanvas.focus_set()

mainMenuCanvas.bind("<Key>",idNum)
mainMenuCanvas.bind("<Return>",swipe)
cardReadErrorCanvas.bind("<Return>",returnFromError)

# Create a mainloop
tk.mainloop()
