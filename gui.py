from tkinter import *
from tkinter import ttk
import os
import bla
import webbrowser

ZoomAMT = 30 #10 small, 20 med, 30 large logoSize
DeBug = False
LOGO_ON = True #enables logo
DEBUG = DeBug

errCodes = {4:'Working DIR dose not exist. please make a directory tmp in root of the same folder'}

def about_program():
    webbrowser.open_new("https://github.com/ChocolaKuma/Kuma_HDD_Hog/blob/master/README.md")
def help_HelpDocs():
    webbrowser.open_new("https://github.com/ChocolaKuma/Kuma_HDD_Hog")
   
    
def hog(event):
    if (DEBUG == True):
        print("click")
    bla.main()
    
def stop(event):
    if (DEBUG == True):
        print("Ending")
    quit()

def opendirtobefilled(event):
    if (DEBUG == True):
        print("Opening")   
    try:
        os.startfile('tmp')
    except:
        messagebox.showinfo('ERROR 404',errCodes[4])

def filesize(event):
    try:
        size = os.stat('./tmp/')
    except:
        print("")
        

root = Tk()
r = root
var = IntVar()

r.title("MemHog by J.Hinebrook")
r.iconbitmap(r'img/icon.ico')

if(LOGO_ON == True):
    #TODO Remove scaler and resize logo img
    #TODO ADD random logo art
    logo = PhotoImage(file="img/logo.png")
    logo = logo.zoom(ZoomAMT) 
    logo = logo.subsample(40)
    logoPNG = Label(root, image=logo).grid(row=1,sticky=N,pady=4,column=2)

f = Frame(r)

pAth = os.path.realpath(__file__)

Label(r,text="Kuma_HDD_Hog.py",fg = "black",font = "Times").grid(row=2,sticky=N,pady=4,column=2)

Label(r,text="Use at your own risk",fg = "red",font = "Times").grid(row=3,sticky=N,pady=4,column=2)
Label(r,text=pAth,fg = "gray",font = ("Times",10)).grid(row=4,sticky=N,pady=4,column=2)


b = Button(r,text="Start")
b.bind("<Button-1>",hog)
b.grid(row=5,sticky=N,pady=4,column=1)

d = Button(r,text="Open Location to be filled")
d.bind("<Button-1>",opendirtobefilled)
d.grid(row=5,sticky=N,pady=4,column=2)

c = Button(r,text="Stop")
c.bind("<Button-1>",stop)
c.grid(row=5,sticky=N,pady=4,column=3)
m = Menu(r)

hm = Menu(m)
hm.add_command(label="Help Docs",command = help_HelpDocs)
m.add_cascade(label="Help",menu=hm)
r.config(menu=m)




r.mainloop()
