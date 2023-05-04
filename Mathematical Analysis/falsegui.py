from tkinter import *
import fixed as fi
import false as fa
window = Tk()
window.title("Math analysis false position")

labelfx = Label(window,text="F(x): ").grid(padx=5,row=0,column=1)
f = Entry(window,width=45)
f.grid(row=0,column=2,padx=10)

labelgx = Label(window,text="g(x): ").grid(padx=5,row=4,column=1)
g = Entry(window,width=45)
g.grid(row=4,column=2,padx=10)

labelx0 = Label(window,text="x0: ").grid(row=1,column=1)
x0 = Entry(window,width=45)
x0.grid(row=1,column=2)

labelx1 = Label(window,text="x1: ").grid(row=2,column=1)
x1 = Entry(window,width=45)
x1.grid(row=2,column=2)

labele = Label(window,text="e: ").grid(row=3,column=1)
e = Entry(window,width=45)
e.grid(row=3,column=2)
try:
    def root():
        iterations , x2 = fi.fixedPointIteration(f.get(),g.get(),x0.get(),x1.get(),e.get())
        for i in range(0,len(iterations)):
            label = Label(window,text=iterations[i])
            label.grid(row=(6+i),column=2)
        label = Label(window,text=f"root {x2}")
        label.grid(row=(8+len(iterations)),column=2)
except:
    label = Label(window,text='try agai')
    label.grid(row=(6),column=2)
button = Button(window,text='solve',command=root).grid(row=5,column=2)

window.mainloop()