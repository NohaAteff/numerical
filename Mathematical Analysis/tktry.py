from tkinter import *
from tkinter import ttk
import ttkbootstrap as tb
import false as fa
import newton as n
import secant as s
import bisection as bi
import fixed as fi
window = tb.Window(themename='superhero')
window.title('ComboBox')
iterations_lable = []
labelx0 = Label(window,text="x0: ")
x0 = tb.Entry(window,width=45,bootstyle='dark')

labelx1 = Label(window,text="x1:")
x1 = tb.Entry(window,width=45,bootstyle='dark')

labele = Label(window,text="e: ")
e = tb.Entry(window,width=45,bootstyle='dark')

labelgx=Label(window,text="g(x): ")
g = tb.Entry(window,width=45,bootstyle='dark')
        
labelnn = Label(window,text="N:")
nn = tb.Entry(window,width=45,bootstyle='dark')
labelx = Label(window)
label = Label(window)
labeli = Label(window)
lab = Label(window)
def root():
    global labelx , labeli, iterations_lable
    labelx.destroy()
    labeli.destroy()
    
    for i in iterations_lable:
        i.destroy()
    iterations_lable = []
    try:
        if cb1.get()=='False position':
            iterations , x2 = fa.falsePosition(f.get(),x0.get(),x1.get(),e.get())
            for i in range(0,len(iterations)):
                labeli = Label(window,text=iterations[i])
                labeli.grid(row=(8+i),column=3,padx=(0,15))
                iterations_lable.append(labeli)
            labelx = tb.Label(window,text=f"root {x2}",bootstyle="warning")
            labelx.grid(row=(10+len(iterations)),column=3,padx=(0,15))
            
        elif cb1.get()=='Newton Raphson':
            iterations , xk = n.newtonRaphson(f.get(),x0.get(),e.get(),nn.get())
            for i in range(0,len(iterations)):
                labeli = Label(window,text=iterations[i])
                labeli.grid(row=(8+i),column=3,padx=(0,15))
                iterations_lable.append(labeli)
            labelx = tb.Label(window,text=f"root {xk}",bootstyle="warning")
            labelx.grid(row=(10+len(iterations)),column=3,padx=(0,15))
            
        elif cb1.get()=='secant':
            iterations , xs = s.secant(f.get(),x0.get(),x1.get(),e.get(),nn.get())
            for i in range(0,len(iterations)):
                labeli = Label(window,text=iterations[i])
                labeli.grid(row=(9+i),column=3,padx=(0,15))
                iterations_lable.append(labeli)   
            labelx = Label(window,text=f"root {xs}")
            labelx.grid(row=(11+len(iterations)),column=3,padx=(0,15))
            
        elif cb1.get()=='Bisection':
            iterations , x2 = bi.bisection(f.get(),x0.get(),x1.get(),e.get())
            for i in range(0,len(iterations)):
                labeli = Label(window,text=iterations[i])
                labeli.grid(row=(8+i),column=3,padx=(0,15))
                iterations_lable.append(labeli)
            labelx = tb.Label(window,text=f"root {x2}",bootstyle="warning")
            labelx.grid(row=(10+len(iterations)),column=3,padx=(0,15))
            
        elif cb1.get()=='Simple fixed point':
            iterations , x2 = fi.fixedPointIteration(f.get(),g.get(),x0.get(),e.get(),nn.get())
            for i in range(0,len(iterations)):
                labeli = Label(window,text=iterations[i])
                labeli.grid(row=(8+i),column=3,padx=(0,15))
                iterations_lable.append(labeli)
            labelx = tb.Label(window,text=f"root {x2}",bootstyle="warning")
            labelx.grid(row=(10+len(iterations)),column=3,padx=(0,15))
    except:
        lab = tb.Label (window,text='Error',bootstyle="danger").grid(row=8,column=3,padx=(0,10),pady=10)   
    
def selected(event):
    if cb1.get() == 'False position' or cb1.get() == 'Bisection':
        labelx0.grid(row=3,column=2)
        x0.grid(row=3,column=3,padx=(0,10),pady=(1,0))
        labelx1.grid(row=4,column=2)
        x1.grid(row=4,column=3,padx=(0,10),pady=(1,0))
        labele.grid(row=5,column=2)
        e.grid(row=5,column=3,padx=(0,10),pady=(1,0))
        nn.grid_forget()
        labelnn.grid_forget()
        labelgx.grid_forget()
        g.grid_forget()
    elif cb1.get()=='Newton Raphson':
        labelx0.grid(row=3,column=2)
        x0.grid(row=3,column=3,padx=(0,10),pady=(1,0))
        labele.grid(row=4,column=2)
        e.grid(row=4,column=3,padx=(0,10),pady=(1,0))
        labelnn.grid(row=5,column=2)
        nn.grid(row=5,column=3,padx=(0,10),pady=(1,0))
        x1.grid_forget()
        labelx1.grid_forget()
        labelgx.grid_forget()
        g.grid_forget()
    elif cb1.get()=='secant':
        labelx0.grid(row=3,column=2)
        x0.grid(row=3,column=3,padx=(0,10),pady=(1,0))
        labelx1.grid(row=4,column=2)
        x1.grid(row=4,column=3,padx=(0,10),pady=(1,0))
        labele.grid(row=5,column=2)
        e.grid(row=5,column=3,padx=(0,10),pady=(1,0))
        labelnn.grid(row=6,column=2)
        nn.grid(row=6,column=3,padx=(0,10),pady=(1,0))
        labelgx.grid_forget()
        g.grid_forget()
    else:
        labelgx.grid(row=3,column=2)
        g.grid(row=3,column=3,padx=(0,10),pady=(1,0))
        labelx0.grid(row=4,column=2)
        x0.grid(row=4,column=3,padx=(0,10),pady=(1,0))
        labele.grid(row=5,column=2)
        e.grid(row=5,column=3,padx=(0,10),pady=(1,0))
        labelnn.grid(row=6,column=2)
        nn.grid(row=6,column=3,padx=(0,10),pady=(1,0))
        x1.grid_forget()
        labelx1.grid_forget()
options = ['False position','Newton Raphson','Bisection','Simple fixed point','secant']

clicked = StringVar()
clicked.set('')

labelfx = Label(window,text="F(x): ").grid(row=1,column=2,padx=5)
f = tb.Entry(window,width=45,bootstyle='primary')
f.grid(row=1,column=3,padx=(0,10),pady=10)

cb1 = tb.Combobox(window,values=options,width=30)
cb1.bind("<<ComboboxSelected>>",selected)
cb1.grid(row=2,column=3,padx=(0,10))

button = tb.Button(window,text='solve',bootstyle='primary outline',command=root).grid(row=7,column=3,padx=(0,10),pady=10)

window.mainloop()
