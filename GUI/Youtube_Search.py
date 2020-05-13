#Enter keywords of a youtube video in the dialogue box and you will be directed to youtube search reesults
import webbrowser
from tkinter import *
yt_search = Tk()
def search(a):
    b=list(enter_keyword.get().split())
    c='+'.join(b)
    webbrowser.open('https://www.youtube.com/results?search_query={}'.format(c))
    
key=Label(yt_search ,text="Enter keywords:")
key.grid(row=0)

enter_keyword=Entry(yt_search)
enter_keyword.grid(row=0,column=1)

okay=Button(yt_search, text='Submit')
okay.grid(row=1, columnspan=2)

okay.bind("<Button-1>", search)

yt_search.mainloop()
