#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 15:25:13 2022

@author: clockshield
"""
from tkinter import *
import random
from PIL import ImageTk, Image
import os
from tkinter import filedialog
root=Tk()
root.title("lol")
root.minsize(650, 650)
root.maxsize(650, 650)


open_file_img = ImageTk.PhotoImage(Image.open ("open.png"))
exit_file_img = ImageTk.PhotoImage(Image.open ("exit.jpg"))
save_file_img = ImageTk.PhotoImage(Image.open ("save.png"))
    
file_name = Label(root, text = "File Name:")
file_name.place(relx = 0.35, rely = 0.05, anchor=CENTER)

file_name_input = Entry(root)
file_name_input.place(relx = 0.45, rely = 0.05, anchor = CENTER)



text_area = Text(root, width = 80, height=35)
text_area.place(relx = 0.5, rely = 0.55, anchor = CENTER)

name = ""
def openFile():
    global name
    text_area.delete(1.0, END)
    file_name_input.delete(0, END)
    text_file = filedialog.askopenfilename(title = "Open File" ,
                                           filetypes = (("Text Files","*.txt"),))
    name = os.path.basename(text_file)
    print(name)
    formatted_name = name.split(".")[0]
    root.title(formatted_name)
    file_name_input.insert(END, formatted_name)
    text_file = open(name,'r')
    paragraph = text_file.read()
    print(paragraph)
    text_area.insert(END, paragraph)
    text_file.close()
    

def save():
    file_input = file_name_input.get()
    file = open(file_input + ".txt", "w")
    data = text_area.get(1.0, END)
    print(data)
    file.write(data)
    file_name_input.delete(0, END)
    text_area.delete(1.0, END)
    messagebox.showinfo("Update", "Success")
def destroy():
    root.destroy()

    
open_file_btn = Button(root, image=open_file_img, command = openFile)
open_file_btn.place(relx = 0.05, rely = 0.05, anchor = CENTER)

exit_file_btn = Button(root, image=exit_file_img, command = destroy)
exit_file_btn.place(relx = 0.15, rely = 0.05, anchor = CENTER)

save_file_btn = Button(root, image=save_file_img, command = save)
save_file_btn.place(relx = 0.10, rely = 0.05, anchor = CENTER)
root.mainloop()