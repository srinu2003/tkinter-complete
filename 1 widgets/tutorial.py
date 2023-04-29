from tkinter import * # type: ignore
from tkinter import ttk
from tkinter import filedialog
# import ttkboottrap

def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("Text files","*.txt*"),("all files","*.*")))
      
    # Change label contents

def show():
    text = top_text_field.get("1.0", "end-1c")    
    botttom_text_field.insert('end',text) 
#app
app = Tk()
app.title("APP NAME")
# app.geometry("300x150")
app.geometry('400x600')
app.minsize(width=350,height=500)

#lable
greeting_label = ttk.Label(app, text="Enter your name:")
greeting_label.pack()
#title
title_lable = ttk.Label(master=app,text='CHAT DECRYPTION', font='calibri 24 bold')
title_lable.pack()

# # this is Entry using tkinter
# text_entry = Entry(app,width= 20)
# text_entry.pack()
# this is entry using ttk
 
# top enetry field
top_text_field = Text(app,width=50,height=10, background='light blue') #widget
top_text_field.pack(fill='x',padx=5,pady=2)
# top_text_field.pack(side = 'top', expand = True, fill = 'both', padx = 10, pady = 10) #layout

#input field 
key_frame = ttk.Frame(master=app)
key_lable = ttk.Label(master = key_frame, text="Enter your KEY:")
key_lable.pack(side='left',pady=0)
entry = ttk.Entry(master = key_frame,show=u"\u25CF",width=32)#,textvariable='hellll')
entry.pack(side='left',padx=10)
key_frame.pack(pady=10,side='top')

#button field
button_frame = Frame(master=app)
encrypt = ttk.Button(master=button_frame, text= 'Encrypt',command=show).pack(side='left',padx=10)#.place(x=30,y=20)#
decrypt = ttk.Button(master=button_frame, text= 'Decrypt',command = browseFiles).pack(side='left',padx=10)
button_frame.pack()

# bottom enetry field
botttom_text_field = Text(app,width=50,height=10, background = 'light yellow') #widget
botttom_text_field.pack(fill='x',padx=5,pady=2)
# botttom_text_field.pack(side = 'top', expand = True, fill = 'both', padx = 10, pady = 10) #layout
#output 
top = 5
botttom = 5
output_lable = ttk.Label(master=app,text='output', font='calibri 24',textvariable='sinu')
output_lable.pack(side = 'top',pady=[top,botttom])

#run
app.mainloop()