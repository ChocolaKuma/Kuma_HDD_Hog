from tkinter import *
from tkinter import ttk
import os
import bla

ZoomAMT = 10 #10 small, 20 med, 30 large logoSize
DeBug = True
CK = True #changes from regular qurys to pirate mode

def about_program():
    GHX_Backend.openURL("https://github.com/ChocolaKuma/Kuma_HDD_Hog/blob/master/README.md")
def help_HelpDocs():
    GHX_Backend.openURL("https://github.com/ChocolaKuma/Kuma_HDD_Hog")
   
    
def hog(event):
    print("click")
    bla.main()

root = Tk()
r = root
var = IntVar()

r.title("MemHog by J.Hinebrook")

##if(DeBug == False):
##    #TODO Remove scaler and resize logo img
##    #TODO ADD random logo art
##    logo = PhotoImage(file="img/2.png")
##    logo = logo.zoom(ZoomAMT) 
##    logo = logo.subsample(40)
##    logoPNG = Label(root, image=logo).grid(row=1,sticky=N,pady=4)

f = Frame(r)



Label(r,text="Mem Hog").grid(row=2,sticky=N,pady=4)




b = Button(r,text="Start")
b.bind("<Button-1>",hog)
b.grid(row=5,sticky=N,pady=4)

m = Menu(r)
fm = Menu(m)
fm.add_command(label="About Program",command = about_program)
m.add_cascade(label="About",menu=fm)

hm = Menu(m)
hm.add_command(label="Help Docs",command = help_HelpDocs)
m.add_cascade(label="Help",menu=hm)
r.config(menu=m)




r.mainloop()
