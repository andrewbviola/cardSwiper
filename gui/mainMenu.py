import tkinter as tk
import helpers as hp
from tkinter import font

# Create a root
root = tk.Tk()
root.resizable(False, False)

width = 600
height = 500
pid = ""

# Set initial size
mainMenuCanvas = tk.Canvas(root, width=width, height=height)
signInCanvas = tk.Canvas(root, width=width, height=height)

# Background color
mainMenuCanvas.configure(bg="#C64600")
signInCanvas.configure(bg="#FFE484")

# Top Bar
mainMenuCanvas.create_rectangle(0, 0, width, 50, fill="#861F41", outline="#861F41")
mainMenuCanvas.create_text(width/2,25,font=("Roboto Mono",24),text="inVenTs Studio Sign In/Out",fill="white")
mainMenuCanvas.create_text(width/2,height/2,font=("Roboto Mono Bold",36),text="Swipe your HokieP",fill="white")
mainMenuCanvas.create_text(width/2,90,font=("Roboto Mono",12),text="We're glad you're here!",fill="white")

# Time and Date
time = tk.Label(mainMenuCanvas)
date = tk.Label(mainMenuCanvas)
time.pack()
date.pack()

def clock():
    time.config(font=("Roboto Mono Bold",24,),text=hp.guiTime(),bg="#C64600",fg="white")
    time.place(x=width-160,y=height-47)
    date.config(font=("Roboto Mono Bold",24,),text=hp.guiDate(),bg="#C64600",fg="white")
    date.place(x=width-(width-5),y=height-47)
    print("clock")
    root.after(1000,clock)
    
def idNum(event):
    global pid
    if event.char == "Return":
        return
    pid = pid + event.char
  
def enter(event):
    print(pid)
    mainMenuCanvas.forget()
    signInCanvas.pack()
    signInCanvas.focus_set()

clock()

mainMenuCanvas.pack()
mainMenuCanvas.focus_set()

mainMenuCanvas.bind("<Key>",idNum)
mainMenuCanvas.bind("<Return>",enter)

# Create a mainloop
tk.mainloop()
