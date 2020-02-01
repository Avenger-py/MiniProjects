from tkinter import *
area=Tk()
def areaOfTriangle(event):
    a=float(p.get())
    b=float(q.get())
    c=float(r.get())
    s=float()
    s=(a+b+c)/2
    print("Area of the triangle is {}".format((s*(s-a)*(s-b)*(s-c))**0.5))
A=Label(area, text="Side 1:")
B=Label(area, text="Side 2:")
C=Label(area, text="Side 3:")

A.grid(row=0)
B.grid(row=1)
C.grid(row=2)


p=Entry(area)
q=Entry(area)
r=Entry(area)
Ar=Button(area, text="OK")

Ar.grid(row=3, columnspan=2)
p.grid(row=0, column=1)
q.grid(row=1, column=1)
r.grid(row=2, column=1)

Ar.bind("<Button-1>", areaOfTriangle)
'''a.bind(areaOfTriangle)
b.bind(areaOfTriangle)
c.bind(areaOfTriangle)'''

area.mainloop()
    
