from tkinter import *

import secant as s

window = Tk()
window.title("Math analysis")

labelfx = Label(window,text="F(x): ").grid(padx=5,row=0,column=1)
f = Entry(window,width=45)
f.grid(row=0,column=2,padx=10)
#drop down menu

labelx0 = Label(window,text="x-1: ").grid(row=1,column=1)
x0 = Entry(window,width=45)
x0.grid(row=1,column=2)

labelx1 = Label(window,text="x0: ").grid(row=2,column=1)
x1 = Entry(window,width=45)
x1.grid(row=2,column=2)

labele = Label(window,text="e: ").grid(row=3,column=1)
e = Entry(window,width=45)
e.grid(row=3,column=2)

labelnn = Label(window,text="N: ").grid(row=4,column=1)
nn = Entry(window,width=45)
nn.grid(row=4,column=2)

labeli = Label(window)
def root():
    global labeli
    labeli.destroy()
    iterations , xs = s.secant(f.get(),x0.get(),x1.get(),e.get(),nn.get())
    for i in range(0,len(iterations)):
        labeli = Label(window,text=iterations[i])
        labeli.grid(row=(6+i),column=2)
    labelx = Label(window,text=f"root {xs}")
    labelx.grid(row=(8+len(iterations)),column=2)
button = Button(window,text="solve",command=root).grid(row=5,column=2)


window.mainloop()
