import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
# import ttkbootstrap as ttk
from symmetric_encryption import *

def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("Text files","*.txt*"),("all files","*.*")))
      
    # Change label contents

def take_text():
    text = 'Hello'
    # text = entry.get()
    greeting_label.config(text=f"Hello, {text}!")


# app
app = tk.Tk()
app.title("Magpie")
# app.geometry("300x150") # for 730p 'ish screens
app.geometry('400x500')
app.minsize(width= 350,height= 500)

#lable
greeting_label = ttk.Label(app, text="Welcome to")
greeting_label.pack()

#title
title_lable = ttk.Label(app,text='CHAT Encrypter', font='calibri 24 bold')
title_lable.pack()

# Left frame
left_frame = tk.Frame(app, border= '10px')

input_lable = ttk.Label(left_frame, text = 'Enter text to Encrypt.')
input_lable.pack(expand= True)

input_text_field = tk.Text(left_frame, width= 50, height= 10, background= 'light blue')
input_text_field.pack(expand= True)

input_button = ttk.Button(left_frame)
input_button.pack()

left_frame.pack(side= 'left',expand= True)

# Start the main event loop
app.mainloop()
