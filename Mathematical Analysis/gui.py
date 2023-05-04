from tkinter import *
from tkinter import ttk
import false as fa
import newton as n
window = Tk()
window.title('ComboBox')
#window.geometry('350x300')
labelx0 = Label(window,text="x0: ")
x0 = Entry(window,width=45)

labelx1 = Label(window,text="x1: ")
x1 = Entry(window,width=45)

labele = Label(window,text="e: ")
e = Entry(window,width=45)

labelnn = Label(window,text="N: ")
nn = Entry(window,width=45)

labelx = Label(window)
 
def root():
    if cb1.get()=='false':
        iterations , x2 = fa.falsePosition(f.get(),x0.get(),x1.get(),e.get())
        for i in range(0,len(iterations)):
            labeli = Label(window,text=iterations[i])
            labeli.grid(row=(8+i),column=3,padx=(0,15))
        label = Label(window,text=f"root {x2}",bg='navy',fg='#00ff00')
        label.grid(row=(10+len(iterations)),column=3,padx=(0,15))
        # if cb1.get()!='false':
        #     for i in range(0,len(iterations)):
        #         labeli.config(text='')

    elif cb1.get()=='newton':
        iterations , xk = n.newtonRaphson(f.get(),x0.get(),e.get(),nn.get())
        for i in range(0,len(iterations)):
            labeli = Label(window,text=iterations[i])
            labeli.grid(row=(8+i),column=3,padx=(0,15))
        label = Label(window,text=f"root {xk}",bg='#00ff00',fg='navy')
        label.grid(row=(10+len(iterations)),column=3,padx=(0,15))
    else:
        lab = Label(window,text="Implement the functions")
def selected(event):
    if cb1.get() == 'false' or cb1.get() == 'bisection':
        labelx0.grid(row=3,column=2)
        x0.grid(row=3,column=3,padx=(0,10))
        labelx1.grid(row=4,column=2)
        x1.grid(row=4,column=3,padx=(0,10))
        labele.grid(row=5,column=2)
        e.grid(row=5,column=3,padx=(0,10))
        nn.grid_forget()
        labelnn.grid_forget()
            
    elif cb1.get()=='newton':
        labelx0.grid(row=3,column=2)
        x0.grid(row=3,column=3)
        labele.grid(row=4,column=2)
        e.grid(row=4,column=3)
        labelnn.grid(row=5,column=2)
        nn.grid(row=5,column=3)
        x1.grid_forget()
        labelx1.grid_forget()
    elif cb1.get()=='secant':
        labelx0.grid(row=3,column=2)
        x0.grid(row=3,column=3)
        labelx1.grid(row=4,column=2)
        x1.grid(row=4,column=3)
        labele.grid(row=5,column=2)
        e.grid(row=5,column=3)
        labelnn.grid(row=6,column=2)
        nn.grid(row=6,column=3)
    else:
        labelx0.grid(row=3,column=2)
        x0.grid(row=3,column=3)
        labele.grid(row=4,column=2)
        e.grid(row=4,column=3)
        labelnn.grid(row=5,column=2)
        nn.grid(row=5,column=3)
        x1.grid_forget()
        labelx1.grid_forget()
options = ['false','newton','bisection','simple fixed point','secant']

clicked = StringVar()
clicked.set('')

labelfx = Label(window,text="F(x): ").grid(row=1,column=2,padx=5)
f = Entry(window,width=45)
f.grid(row=1,column=3,padx=(0,10))

cb1 = ttk.Combobox(window,values=options,width=30)
cb1.bind("<<ComboboxSelected>>",selected)
cb1.grid(row=2,column=3,padx=(0,10))

button = Button(window,text='solve',command=root).grid(row=7,column=3,padx=(0,10))
window.mainloop()
