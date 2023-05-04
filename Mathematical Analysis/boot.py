from tkinter import *
import numpy as np
import sys
import gaussianelimination as ge
root = Tk()
root.title('entry boxes')
root.geometry('700x400')
# my_entries = []
myentries = []
# m = []
f = []
n = 3
def ss():
    global f
    for i in range(len(myentries)):
        f.append(int(str(myentries[i].get())))
    
    # global my_entries     
    # my_entries = np.reshape(np.array(f),(n,n+1))
    # print((my_entries))
    # m = iter(my_entries)
    # # my_entries=np.matrix(my_entries)
    # # print(type(my_entries))

for i in range(n):
    for j in range(n+1):
        myentry = Entry(root)
        myentry.grid(row=i,column=j,padx=5,pady=5)
        myentries.append(myentry)
        

def g():
    ge.slice(f) 
    print(ge.slice(f))
    
        
mb = Button(root,text='click me!',command=ss)
mb.grid(row=6,column=0)

mb2 = Button(root,text='click me!',command=g)
mb2.grid(row=7,column=0)


root.mainloop()