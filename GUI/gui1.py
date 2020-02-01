from tkinter import *

window = Tk()
topframe=Frame(window)
topframe.pack()
downframe=Frame(window)
downframe.pack(side=BOTTOM)
a=Label(topframe, text="Hello")
a.pack()
b1=Button(downframe, text="OK")
b2=Button(downframe, text="Cancel")
b1.pack(side=LEFT)
b2.pack()

window.mainloop()
