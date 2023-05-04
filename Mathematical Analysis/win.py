from tkinter import *

import newton as n

window = Tk()
window.title("Math analysis")

labelfx = Label(window,text="F(x): ").grid(padx=5,row=0,column=1)
f = Entry(window,width=45)
f.grid(row=0,column=2,padx=10)
#drop down menu

labelx0 = Label(window,text="x0: ").grid(row=1,column=1)
x0 = Entry(window,width=45)
x0.grid(row=1,column=2)

labele = Label(window,text="e: ").grid(row=2,column=1)
e = Entry(window,width=45)
e.grid(row=2,column=2)

labelnn = Label(window,text="N: ").grid(row=3,column=1)
nn = Entry(window,width=45)
nn.grid(row=3,column=2)

def root():
    iterations , x1 = n.newtonRaphson(f.get(),x0.get(),e.get(),nn.get())
    for i in range(0,len(iterations)):
        label = Label(window,text=iterations[i])
        label.grid(row=(5+i),column=2)
    label = Label(window,text=f"root {x1}")
    label.grid(row=(7+len(iterations)),column=2)
    
        


button = Button(window,text="solve",command=root).grid(row=4,column=2)


window.mainloop()
