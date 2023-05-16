# from tkinter import *
# import numpy as np
# import sys
# import gaussianelimination as ge
# import guii as ii
# tab2 = Tk()
# tab2.title('entry boxes')
# tab2.geometry('700x400')

# myentries = []
# o=0
# p=0
# f = []
# n = 3
# label = Label(tab2)
# label2 = Label(tab2)
# # an = Entry(tab2)
# # an.grid(row=12,column=0)
# # n=int(str(an.get()))
# def ss():
#     global f
#     for i in range(len(myentries)):
#         f.append(int(str(myentries[i].get())))
#     a,x = ge.slice(f) 
#     global o,p
#     for i in a:
#         label = Label(tab2,text='[           ').grid(row=8+o,column=p)
#         for j in i:
#             print(round(j,3), end = ' ')
#             q = round(j,3)
#             label = Label(tab2,text=(q))
#             label.grid(row=8+o,column=p)
#             p+=1
#         label = Label(tab2,text=']').grid(row=8+o,column=p)
#         p=0
#         o+=1
#         print()
#     for i in range(len(x)):
#         label2 = Label(tab2,text=('x%d= ' % (i+1)+str(int(x[i]))))
#         label2.grid(row=15,column=1+i)
#         print(x[i]) 
#         # print("{:.8f}".format(x[i]))
# for i in range(n):
#     for j in range(n+1):
#         myentry = Entry(tab2,width=15)
#         myentry.grid(row=i,column=j,padx=5,pady=5)
#         myentries.append(myentry)

# mb = Button(tab2,text='click me!',command=ss)
# mb.grid(row=6,column=0)

# # mb2 = Button(tab2,text='click me!',command=g)
# # mb2.grid(row=7,column=0)


# tab2.mainloop()
c = [1,2,3]
c = []
print(c)