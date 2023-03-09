from API import RestAPI
from tkinter import *
from tkinter import ttk
from Ult_web2 import Ani_Installer
import tkinter.font as font
root=Tk()
root.title("Pahe Downloader")

pop='720'
api=RestAPI()
def Asvalue(x):
    global pop
    pop=x
root.geometry("560x300")
Label(root, text="Welcome to Pahe Downloader", font="Arial 20 bold", fg = "black").pack()

my_font2=font.Font(font="Arial 13")
my_font=font.Font(size=15)
ani_name=StringVar()
frame = Frame(root)
frame.pack()
prom=Label(frame, text="Enter anime name:", font="Arial 13", fg = "blue").pack(side="left", pady=10)
entry1 = ttk.Entry(frame, justify = LEFT,)
entry1['font']=my_font2
fram = Frame(root)
fram.pack()
prom2=Label(fram, text="Enter first episode:", font="Arial 13", fg = "blue").pack(side="left", pady=10)
entry2 = ttk.Entry(fram, justify = LEFT,)
entry2['font']=my_font2
fra= Frame(root)
fra.pack()
prom3=Label(fra, text="Enter last episode:", font="Arial 13", fg = "blue").pack(side="left", pady=10)
entry3 = ttk.Entry(fra, justify = LEFT,)
entry3['font']=my_font2
entry1.pack(side = 'left', ipadx = 100, ipady = 3, pady=1)
entry2.pack(side = 'left', ipadx = 100, ipady = 3, pady=1)
entry3.pack(side = 'left', ipadx = 100, ipady = 3, pady=1)
frame1= Frame(root)
frame1.pack()
frame3= Frame(root)
frame3.pack(side=BOTTOM)

b1 = Button(frame1, text="360p", font=10, width=7, command=lambda *args: Asvalue("360p"))
b2 = Button(frame1, text="720p", font=10, width=7, command=lambda *args: Asvalue("720p"))
b3 = Button(frame1, text="1080p", font=10, width=7, command=lambda *args: Asvalue("1080p"))
b5 = Button(frame3, text="exit ",bg="red", font=10, width=7, command=lambda *args: root.quit())
frame2=Frame(root)
frame2.pack()
web=Ani_Installer()
def set_para(x):
    x.sea=entry1.get()
    x.resol=pop
    x.fe=int(entry2.get())
    x.le=int(entry3.get())
    x.downloader(root)

b4 = Button(frame3, text="Enter",height=1,width=10,bg='#0052cc', command=lambda *args:(set_para(web)))#,root.destroy()))
b4['font']=my_font
b5['font']=my_font

b1.pack(side=LEFT, padx=20)
b2.pack(side=LEFT, padx=20)
b3.pack(padx=20)
b4.pack(side=LEFT, padx=10)
b5.pack(side=LEFT, padx=10)
root.mainloop()