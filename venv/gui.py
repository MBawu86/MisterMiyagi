# import library
from tkinter import *
import speech_recognition as sr
import datetime

# create tkinter object(parent window)
root = Tk()

# window title / dimensions
root.title('Mr. Miyagi')
root.geometry('400x500')
root.resizable(width=FALSE, height=FALSE)

main_menu = Menu(root)

# create submenu
main_menu.add_command(label='File')
main_menu.add_command(label='Edit')
main_menu.add_command(label='Quit')
root.config(menu=main_menu)

# run
root.mainloop()