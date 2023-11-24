import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

def convert() -> None:
    mile_input = entry_int.get()
    km_output = mile_input * 1.61
    ouput_string.set(km_output)

# windoe
window = ttk.Window(themename='darkly')
window.title('Miles to Kilometer converter')
window.geometry('400x200')

# title
title_lable = ttk.Label(master=window, text= 'Miles to Kilometers', font= 'Calibri 24 bold')
title_lable.pack()

#input field
input_frame = ttk.Frame(master= window)
entry_int = tk.IntVar()
entry = ttk.Entry(master= input_frame,textvariable= entry_int)
button = ttk.Button(master= input_frame, text= 'Convert', command= convert)
entry.pack(side= 'left',padx= 10)
button.pack(side= 'left')
input_frame.pack(pady= 10)

#output
ouput_string = tk.StringVar()
output_lable = ttk.Label(
    master=window, 
    text= 'Output', 
    font= 'Calibri 24 bold', 
    textvariable= ouput_string)
output_lable.pack(pady= 5)

# run 
window.mainloop()