from API import RestAPI
from tkinter import *
from tkinter import ttk
from Web_scrapping import Ult_web2
import tkinter.font as font
root=Tk()

pop=''
api=RestAPI()
def Asvalue(x):
    global pop
    pop=x
root.geometry("500x300")
Label(root, text="Welcome to Animepahe Downloader", font="Arial 20 bold", fg = "black").pack()

my_font2=font.Font(font="Arial 10")
my_font=font.Font(size=15)
ani_name=StringVar()
frame = Frame(root)
frame.pack()
prom=Label(frame, text="Enter anime name:", font="Arial 13", fg = "blue").pack(side="left", pady=10)
entry1 = ttk.Entry(frame, text = ani_name, justify = LEFT,)
entry1['font']=my_font2
fram = Frame(root)
fram.pack()
prom2=Label(fram, text="Enter anime name:", font="Arial 13", fg = "blue").pack(side="left", pady=10)
entry2 = ttk.Entry(fram, text = ani_name, justify = LEFT,)
entry2['font']=my_font2
fra= Frame(root)
fra.pack()
prom3=Label(fra, text="Enter anime name:", font="Arial 13", fg = "blue").pack(side="left", pady=10)
entry3 = ttk.Entry(fra, text = ani_name, justify = LEFT,)
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
b4 = Button(frame3, text="Enter",height=1,width=10,bg='#0052cc', command=lambda *args:(api.confirm(pop,root)))
b4['font']=my_font
b5['font']=my_font

b1.pack(side=LEFT, padx=20)
b2.pack(side=LEFT, padx=20)
b3.pack(padx=20)
b4.pack(side=LEFT, padx=10)
b5.pack(side=LEFT, padx=10)
root.mainloop()
print(entry1.get())
print(ani_name.get())