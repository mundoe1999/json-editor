import os
from tkinter import *
from tkinter import filedialog

window = Tk() # Instantiate instance of window
window.geometry("420x420")
window.title("Json Editor GUI")

def openFile():
  filepath = filedialog.askopenfilename(
    initialdir= os.getcwd(),
    title= "Open JSON Template file",
    filetypes= (
                ("JSON file type","*.json"),
                ("All files", "*.*")
                )
    )
  print(filepath)

label = Label(window, text="Testing")
label.pack()

button = Button(text="Open Json file", command=openFile)
button.pack()

window.mainloop() # place window and listen to events

