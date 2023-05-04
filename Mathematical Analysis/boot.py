from tkinter import *
import numpy as np
import sys
import gaussianelimination as ge
root = Tk()
root.title('entry boxes')
root.geometry('700x400')
myentries = []
o=0
p=0
f = []
n = 3
label = Label(root)
def ss():
    global f
    for i in range(len(myentries)):
        f.append(int(str(myentries[i].get())))
    a = ge.slice(f) 
    global o,p
    for i in a:
        for j in i:
            print(round(j,3), end = ' ')
            q = round(j,3)
            label = Label(root,text=q)
            label.grid(row=8+o,column=p)
            p+=1
        p=0
        o+=1
        print()
for i in range(n):
    for j in range(n+1):
        myentry = Entry(root)
        myentry.grid(row=i,column=j,padx=5,pady=5)
        myentries.append(myentry)
        

# def g():
#     a = ge.slice(f) 
#     global o
#     for i in a:
#         for j in i:
#             print(round(j,3), end = ' ')
#             q = round(j,3)
#             label = Label(root,text=q)
#             label.grid(row=8+o,column=0)
#             o+=1
#         print()
mb = Button(root,text='click me!',command=ss)
mb.grid(row=6,column=0)

# mb2 = Button(root,text='click me!',command=g)
# mb2.grid(row=7,column=0)


root.mainloop()