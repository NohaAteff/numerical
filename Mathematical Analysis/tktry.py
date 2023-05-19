# from tkinter import *
# from tkinter import ttk
# import ttkbootstrap as tb
# import false as fa
# import newton as n
# import secant as s
# import bisection as bi
# import fixed as fi
# window = tb.Window(themename='superhero')
# window.title('ComboBox')
# iterations_lable = []
# labelx0 = Label(window,text="x0: ")
# x0 = tb.Entry(window,width=45,bootstyle='dark')

# labelx1 = Label(window,text="x1:")
# x1 = tb.Entry(window,width=45,bootstyle='dark')

# labele = Label(window,text="e: ")
# e = tb.Entry(window,width=45,bootstyle='dark')

# labelgx=Label(window,text="g(x): ")
# g = tb.Entry(window,width=45,bootstyle='dark')
        
# labelnn = Label(window,text="N:")
# nn = tb.Entry(window,width=45,bootstyle='dark')
# labelx = Label(window)
# label = Label(window)
# labeli = Label(window)
# lab = Label(window)
# def root():
#     global labelx , labeli, iterations_lable
#     labelx.destroy()
#     labeli.destroy()
    
#     for i in iterations_lable:
#         i.destroy()
#     iterations_lable = []
#     try:
#         if cb1.get()=='False position':
#             iterations , x2 = fa.falsePosition(f.get(),x0.get(),x1.get(),e.get())
#             for i in range(0,len(iterations)):
#                 labeli = Label(window,text=iterations[i])
#                 labeli.grid(row=(8+i),column=3,padx=(0,15))
#                 iterations_lable.append(labeli)
#             labelx = tb.Label(window,text=f"root {x2}",bootstyle="warning")
#             labelx.grid(row=(10+len(iterations)),column=3,padx=(0,15))
            
#         elif cb1.get()=='Newton Raphson':
#             iterations , xk = n.newtonRaphson(f.get(),x0.get(),e.get(),nn.get())
#             for i in range(0,len(iterations)):
#                 labeli = Label(window,text=iterations[i])
#                 labeli.grid(row=(8+i),column=3,padx=(0,15))
#                 iterations_lable.append(labeli)
#             labelx = tb.Label(window,text=f"root {xk}",bootstyle="warning")
#             labelx.grid(row=(10+len(iterations)),column=3,padx=(0,15))
            
#         elif cb1.get()=='secant':
#             iterations , xs = s.secant(f.get(),x0.get(),x1.get(),e.get(),nn.get())
#             for i in range(0,len(iterations)):
#                 labeli = Label(window,text=iterations[i])
#                 labeli.grid(row=(9+i),column=3,padx=(0,15))
#                 iterations_lable.append(labeli)   
#             labelx = Label(window,text=f"root {xs}")
#             labelx.grid(row=(11+len(iterations)),column=3,padx=(0,15))
            
#         elif cb1.get()=='Bisection':
#             iterations , x2 = bi.bisection(f.get(),x0.get(),x1.get(),e.get())
#             for i in range(0,len(iterations)):
#                 labeli = Label(window,text=iterations[i])
#                 labeli.grid(row=(8+i),column=3,padx=(0,15))
#                 iterations_lable.append(labeli)
#             labelx = tb.Label(window,text=f"root {x2}",bootstyle="warning")
#             labelx.grid(row=(10+len(iterations)),column=3,padx=(0,15))
            
#         elif cb1.get()=='Simple fixed point':
#             iterations , x2 = fi.fixedPointIteration(f.get(),g.get(),x0.get(),e.get(),nn.get())
#             for i in range(0,len(iterations)):
#                 labeli = Label(window,text=iterations[i])
#                 labeli.grid(row=(8+i),column=3,padx=(0,15))
#                 iterations_lable.append(labeli)
#             labelx = tb.Label(window,text=f"root {x2}",bootstyle="warning")
#             labelx.grid(row=(10+len(iterations)),column=3,padx=(0,15))
#     except:
#         lab = tb.Label (window,text='Error',bootstyle="danger").grid(row=8,column=3,padx=(0,10),pady=10)   
    
# def selected(event):
#     if cb1.get() == 'False position' or cb1.get() == 'Bisection':
#         labelx0.grid(row=3,column=2)
#         x0.grid(row=3,column=3,padx=(0,10),pady=(1,0))
#         labelx1.grid(row=4,column=2)
#         x1.grid(row=4,column=3,padx=(0,10),pady=(1,0))
#         labele.grid(row=5,column=2)
#         e.grid(row=5,column=3,padx=(0,10),pady=(1,0))
#         nn.grid_forget()
#         labelnn.grid_forget()
#         labelgx.grid_forget()
#         g.grid_forget()
#     elif cb1.get()=='Newton Raphson':
#         labelx0.grid(row=3,column=2)
#         x0.grid(row=3,column=3,padx=(0,10),pady=(1,0))
#         labele.grid(row=4,column=2)
#         e.grid(row=4,column=3,padx=(0,10),pady=(1,0))
#         labelnn.grid(row=5,column=2)
#         nn.grid(row=5,column=3,padx=(0,10),pady=(1,0))
#         x1.grid_forget()
#         labelx1.grid_forget()
#         labelgx.grid_forget()
#         g.grid_forget()
#     elif cb1.get()=='secant':
#         labelx0.grid(row=3,column=2)
#         x0.grid(row=3,column=3,padx=(0,10),pady=(1,0))
#         labelx1.grid(row=4,column=2)
#         x1.grid(row=4,column=3,padx=(0,10),pady=(1,0))
#         labele.grid(row=5,column=2)
#         e.grid(row=5,column=3,padx=(0,10),pady=(1,0))
#         labelnn.grid(row=6,column=2)
#         nn.grid(row=6,column=3,padx=(0,10),pady=(1,0))
#         labelgx.grid_forget()
#         g.grid_forget()
#     else:
#         labelgx.grid(row=3,column=2)
#         g.grid(row=3,column=3,padx=(0,10),pady=(1,0))
#         labelx0.grid(row=4,column=2)
#         x0.grid(row=4,column=3,padx=(0,10),pady=(1,0))
#         labele.grid(row=5,column=2)
#         e.grid(row=5,column=3,padx=(0,10),pady=(1,0))
#         labelnn.grid(row=6,column=2)
#         nn.grid(row=6,column=3,padx=(0,10),pady=(1,0))
#         x1.grid_forget()
#         labelx1.grid_forget()
# options = ['False position','Newton Raphson','Bisection','Simple fixed point','secant']

# clicked = StringVar()
# clicked.set('')

# labelfx = Label(window,text="F(x): ").grid(row=1,column=2,padx=5)
# f = tb.Entry(window,width=45,bootstyle='primary')
# f.grid(row=1,column=3,padx=(0,10),pady=10)

# cb1 = tb.Combobox(window,values=options,width=30)
# cb1.bind("<<ComboboxSelected>>",selected)
# cb1.grid(row=2,column=3,padx=(0,10))

# button = tb.Button(window,text='solve',bootstyle='primary outline',command=root).grid(row=7,column=3,padx=(0,10),pady=10)

# window.mainloop()
from tkinter import *
from tkinter import ttk,messagebox
import ttkbootstrap as tb
import false as fal
import newton as ne
import secant as se
import bisection as bi
import fixed as fi
# import gaussPartial as gep
import gauss as ge
import Lu as lu
import cramer as cr
import gaussianelimination as op
window = tb.Window(themename='superhero')
window.title('Numerical Analysis')

note = ttk.Notebook(window)
note.grid(row=0,column=0)
tab1 = ttk.Frame(note)
tab2 = ttk.Frame(note)



iterations_lable = []
labelx0 = Label(tab1,text="x0: ")
x0 = tb.Entry(tab1,width=45,bootstyle='dark')

labelx1 = Label(tab1,text="x1:")
x1 = tb.Entry(tab1,width=45,bootstyle='dark')

labele = Label(tab1,text="e: ")
e = tb.Entry(tab1,width=45,bootstyle='dark')

labelgx=Label(tab1,text="g(x): ")
g = tb.Entry(tab1,width=45,bootstyle='dark')
        
labelnn = Label(tab1,text="N:")
nn = tb.Entry(tab1,width=45,bootstyle='dark')
labelx = Label(tab1)
label = Label(tab1)
labeli = Label(tab1)
lab = Label(tab1)
def root():
    global labelx , labeli, iterations_lable, lab
    labelx.destroy()
    labeli.destroy()
    lab.destroy()
    for i in iterations_lable:
        i.destroy()
    iterations_lable = []
    try:
        if cb1.get()=='False position':
            iterations , x2 = fal.falsePosition(f.get(),x0.get(),x1.get(),e.get())
            for i in range(0,len(iterations)):
                labeli = Label(tab1,text=iterations[i],font=(12))
                labeli.grid(row=(8+i),column=3,padx=(0,15))
                iterations_lable.append(labeli)
            labelx = tb.Label(tab1,text=f"root {x2}",bootstyle="warning")
            labelx.grid(row=(10+len(iterations)),column=3,padx=(0,15))
            
        elif cb1.get()=='Newton Raphson':
            try:
                iterations , xk = ne.newtonRaphson(f.get(),x0.get(),e.get())
            except:
                iterations , xk = ne.newtonRaphson(f.get(),x0.get(),nn.get())
            for i in range(0,len(iterations)):
                labeli = Label(tab1,text=iterations[i],font=(12))
                labeli.grid(row=(8+i),column=3,padx=(0,15))
                iterations_lable.append(labeli)
            labelx = tb.Label(tab1,text=f"root {xk}",bootstyle="warning")
            labelx.grid(row=(10+len(iterations)),column=3,padx=(0,15))
            
        elif cb1.get()=='secant':
            try:
                iterations , xs = se.secant(f.get(),x0.get(),x1.get(),e.get())
            except:
                iterations , xs = se.secant(f.get(),x0.get(),x1.get(),nn.get())
            for i in range(0,len(iterations)):
                labeli = Label(tab1,text=iterations[i],font=(12))
                labeli.grid(row=(9+i),column=3,padx=(0,15))
                iterations_lable.append(labeli)   
            labelx = Label(tab1,text=f"root {xs}")
            labelx.grid(row=(11+len(iterations)),column=3,padx=(0,15))
            
        elif cb1.get()=='Bisection':
            iterations , x2 = bi.bisection(f.get(),x0.get(),x1.get(),e.get())
            for i in range(0,len(iterations)):
                labeli = Label(tab1,text=iterations[i],font=(12))
                labeli.grid(row=(8+i),column=3,padx=(0,15))
                iterations_lable.append(labeli)
            labelx = tb.Label(tab1,text=f"root {x2}",bootstyle="warning")
            labelx.grid(row=(10+len(iterations)),column=3,padx=(0,15))
            
        elif cb1.get()=='Simple fixed point':
            try:
                iterations , x2 = fi.fixedPointIteration(f.get(),g.get(),x0.get(),e.get())
            except:
                iterations , x2 = fi.fixedPointIteration(f.get(),g.get(),x0.get(),nn.get())
            for i in range(0,len(iterations)):
                labeli = Label(tab1,text=iterations[i],font=(11))
                labeli.grid(row=(8+i),column=3,padx=(0,15),pady=3)
                iterations_lable.append(labeli)
            labelx = tb.Label(tab1,text=f"root {x2}",bootstyle="warning")
            labelx.grid(row=(10+len(iterations)),column=3,padx=(0,15))
    except:
        messagebox.showerror("Error","Check your entries")   
    
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

labelfx = Label(tab1,text="F(x): ").grid(row=1,column=2,padx=5)
f = tb.Entry(tab1,width=45,bootstyle='primary')
f.grid(row=1,column=3,padx=(0,10),pady=10)

cb1 = tb.Combobox(tab1,values=options,width=30)
cb1.bind("<<ComboboxSelected>>",selected)
cb1.grid(row=2,column=3,padx=(0,10))

button = tb.Button(tab1,text='solve',bootstyle='primary outline',command=root).grid(row=7,column=3,padx=(0,10),pady=10)

#-----------------------------------------------------------------------------------------------------------------------------#
#ch2
myentries = []
o=0
p=0
arr = []
luarr = []

label = Label(tab2)
label2 = Label(tab2)
labelb = Label(tab2)
brac = Label(tab2)
brac = Label(tab2)
a = []
xx = []
iterappend = []
b_label = []
def delmat():
    global myentries
    [widget.grid_forget() for widget in myentries if isinstance(widget, Entry)]
    
def clear():
    [widget.delete(0, END) for widget in myentries if isinstance(widget, Entry)]

def clearLabel():
    global iterappend,b_label
    [widget.destroy() for widget in iterappend if isinstance(widget, Label)]
    [widget.destroy() for widget in b_label if isinstance(widget, Label)]
def createmat():
    global n,b_label
    delmat()
    clearLabel()
    
    b_label=[]
    try:
        n = int(varn.get())
        for i in range(n):
            brac1 = Label(tab2,text='[')
            brac1.grid(row=i+2,column=0,padx=(15,0))
            b_label.append(brac1)
            for j in range(n+1):
                myentry = Entry(tab2,width=10)
                myentry.grid(row=i+2,column=j+1,padx=5,pady=5)
                myentries.append(myentry)
            brac2 = Label(tab2,text=']')
            brac2.grid(row=i+2,column=j+2)
            b_label.append(brac2)
    except:
        messagebox.showerror("Error","Error,Enter a valid no of integers")          
varn = tb.Entry(tab2)
varn.grid(row=0,column=1,columnspan=4,pady=10)
matbut = Button(tab2,text="Show matrix",command=createmat)
matbut.grid(row=0,column=5,padx=10)
clearbut = tb.Button(tab2,text='clear',bootstyle='primary outline',command=clear)
clearbut.grid(row=6,column=4)
# iterappend = []

def solve():
    global luarr,iterappend,label,label2,labelb,b_label
    global o,p
    luarr = []
    clearLabel()
    b_label = []
    iterappend = []
    
    # try:
    for i in range(len(myentries)):
        arr.append(int(str(myentries[i].get()))) 
    for j in range(len(myentries)):
        luarr.append(int(str(myentries[j].get())))        

    if(cb2.get()=='GE with partial pivoting'):
            a,xx = op.slice(arr)
            
            for i in a:
                labelb = Label(tab2,text='[     ')
                labelb.grid(row=8+o,column=p)
                b_label.append(labelb)
                # iterappend.append(labelb)
                for j in i:
                    print(round(j,3), end = ' ')
                    q = round(j,3)
                    label = Label(tab2,text=(q))
                    label.grid(row=8+o,column=p+1)
                    iterappend.append(label)
                    p+=1
                labelb1 = Label(tab2,text=']')
                labelb1.grid(row=8+o,column=p+1)
                b_label.append(labelb1)
                # iterappend.append(labelb)
                p=0
                o+=1
                print()
            for i in range(len(xx)):
                label2 = Label(tab2,text=('x%d= ' % (i+1)+str(int(xx[i]))))
                label2.grid(row=15,column=1+i)
                iterappend.append(label2)
                print(xx[i])
            o=0
            p=0
    elif(cb2.get()=='Gaussian elimination'):
        a,xx=ge.slice(n,arr)
        
        for i in a:
            labelb = Label(tab2,text='[     ')
            labelb.grid(row=8+o,column=p)
            b_label.append(labelb)
            # iterappend.append(labelb)
            for j in i:
                print(round(j,3), end = ' ')
                q = round(j,3)
                label = Label(tab2,text=(q))
                label.grid(row=8+o,column=p+1)
                iterappend.append(label)
                p+=1
            labelb1 = Label(tab2,text=']')
            labelb1.grid(row=8+o,column=p+1)
            b_label.append(labelb1)
            # iterappend.append(labelb)
            p=0
            o+=1
            print()
        for i in range(len(xx)):
            label2 = Label(tab2,text=('x%d= ' % (i+1)+str(int(xx[i]))))
            label2.grid(row=15,column=1+i)
            iterappend.append(label2)
            print(xx[i])
        o=0
        p=0
    elif(cb2.get()=='LU decomposition'):
        a,xx,lul=lu.luu(luarr)
        print(a)
        print(xx)
        print(lul)
        
        label=Label(tab2,text='LU:')
        label.grid(row=8,column=1)
        b_label.append(label)
        for i in a:
            label1 = Label(tab2,text='[           ')
            label1.grid(row=8+o,column=p+2)
            b_label.append(label1)
            for j in i:
                print(round(j,3), end = ' ')
                q = round(j,3)
                labelq = Label(tab2,text=(q))
                labelq.grid(row=8+o,column=p+2)
                iterappend.append(labelq)
                p+=1
            label_2 = Label(tab2,text=']')
            label_2.grid(row=8+o,column=p+2)
            b_label.append(label_2)
            
            p=0
            o+=1
            print()
        label3=Label(tab2,text='---------------------------------')
        label3.grid(row=11,column=1,columnspan=5)
        b_label.append(label3)
        label4=Label(tab2,text='L:')
        label4.grid(row=13,column=1)
        b_label.append(label4)
        for i in lul:
            label5 = Label(tab2,text='[           ')
            label5.grid(row=11+o,column=p+2)
            b_label.append(label5)
            for j in i:
                print(round(j,3), end = ' ')
                q = round(j,3)
                labelq1 = Label(tab2,text=(q))
                labelq1.grid(row=11+o,column=p+2)
                iterappend.append(labelq1)
                p+=1
            label6 = Label(tab2,text=']')
            label6.grid(row=11+o,column=p+2)
            b_label.append(label6)
            p=0
            o+=1
            print()
        for i in range(len(xx)):
            label2 = Label(tab2,text=('x%d= ' % (i+1)+str(round(xx[i],3))))
            label2.grid(row=20,column=2+i)
            iterappend.append(label2)
            print(xx[i])
        label7=Label(tab2,text='---------------------------------')
        label7.grid(row=17,column=1,columnspan=5)
        b_label.append(label7)
        
        o=0
        p=0
    elif(cb2.get()=='Cramer'):
        a,xx=cr.cramer(n,arr)
        for i in range(len(a)):
            labela = Label(tab2,text='A%d= '%(o+1),font = (12))
            labela.grid(row=8+o,column=p+2)
            iterappend.append(labela)
            labeli = Label(tab2,text=a[i],font = (12))
            labeli.grid(row=8+o,column=p+3)
            iterappend.append(labeli)
            p=0
            o+=1
            print()
        
        for i in range(len(xx)):
            label2 = Label(tab2,text=('x%d= ' % (i+1)+str(int(xx[i]))),font=(12))
            label2.grid(row=20,column=2+i)
            iterappend.append(label2)
            print(xx[i])
        o=p=0
    # except:
    #     messagebox.showerror("Error","Error,check your entries")
    
    arr.clear()

mb = tb.Button(tab2,text='Solve',command=solve)
mb.grid(row=6,column=3)


options2 = ['Gaussian elimination','GE with partial pivoting','LU decomposition','Cramer'] 

labee = Label(tab2,text='No of var: ')
labee.grid(row=0,column=1)
labe = tb.Label(tab2,text='')
labe.grid(row=0,column=4)
cb2 = tb.Combobox(tab2,values=options2,width=30)
cb2.bind("<<ComboboxSelected>>",selected)
cb2.grid(row=1,column=2,columnspan=3,padx=(0,10),pady=5)

methodlab = Label(tab2,text='Method: ').grid(row=1,column=1)
note.add(tab1,text='Finding the root')
note.add(tab2,text='solving matrix')

window.mainloop()