import tkinter
from tkinter import *
import tkinter.scrolledtext as tkst
from tkinter import messagebox
from tkinter import filedialog

root = tkinter.Tk(className="My Text Editor")
textPad = tkst.ScrolledText(root, width=100, height=80)

def opencommand():
    file = filedialog.askopenfile(parent=root, mode='rb', title='Select file to open')
    if file!=None:
        contents = file.read()
        textPad.insert('1.0', contents)
        file.close()

def savecommand():
    file = filedialog.asksavefile(mode='w')
    if file!=None:
        data = textPad.get('1.0', END+'-1c')
        file.write(data)
        file.close()

def exitcommand():
    if messagebox.askokcancel("Quit", "Do you really want to quit?"):
        root.destroy()


def aboutcommand():
    label = messagebox.showinfo("About", "TextPad Using Python \n Copyright: yatharthmishra01@gmail.com\n No rights left to reserve")

def dummy():
    print ("I am a Dummy Command, I will be removed in the next step")


menu = Menu(root)
root.config(menu=menu)
filemenu=Menu(menu)
menu.add_cascade(label="file", menu=filemenu)
filemenu.add_command(label="New", command=dummy)
filemenu.add_command(label="Open...", command=opencommand)
filemenu.add_command(label="Save", command=savecommand)
filemenu.add_separator()
filemenu.add_command(label="Exit", command= exitcommand)
filemenu.add_separator()
filemenu.add_command(label="About", command= aboutcommand)

textPad.pack()
root.mainloop()