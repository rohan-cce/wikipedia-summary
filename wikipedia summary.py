from tkinter import *
#Tkinter provides a fast and easy way to create GUI applications

import wikipedia
#Wikipedia is a Python library that makes it easy to access and parse data from Wikipedia

def on_click():
  
  q = get_q.get()
  #It is used to get the text written inside the widget.
  
  text.insert(INSERT, wikipedia.summary(q,sentences=8))
  #It is used to insert the specified string at the given index.

root = Tk()
#creates root window

question = Label(root, text="Article")
#implements a display box

question.pack()
#Pack geometry manager packs widgets in rows or columns

get_q = Entry(root, bd =5)
#The Entry widget is used to accept single-line text strings from a user.

get_q.pack()
#Pack geometry manager packs widgets in rows or columns

submit = Button(root,text='Submit',command=on_click)
#The Button widget is used to add buttons in a Python application

submit.pack()
#Pack geometry manager packs widgets in rows or columns

text = Text(root)
#The Text widget provides formatted text display.

text.pack()
#Pack geometry manager packs widgets in rows or columns

root.mainloop()
#mainloop() is an infinite loop used to run the application
