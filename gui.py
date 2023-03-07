from API import RestAPI
from tkinter import *
from tkinter import ttk
import tkinter.font as font
root=Tk()

pop=''
api=RestAPI()
def Asvalue(x):
    global pop
    pop=x
root.geometry("720x480")
Label(root, text="Welcome to Animepahe Downloader", font="Arial 20 bold", fg = "black").pack()
frame = Frame(root)
frame.pack()

my_font2=font.Font(font="Arial 10")
my_font=font.Font(size=15)
ani_name=StringVar()
prom=Label(frame, text="Enter anime name:", font="Arial 10", fg = "blue").pack(side="left")
entry1 = ttk.Entry(frame, text = ani_name, justify = LEFT,)
entry1['font']=my_font2
entry1.pack(side = 'left', ipadx = 100, ipady = 3, pady=1)
frame1= Frame(root)
frame1.pack()
frame3= Frame(root)
frame3.pack(side=BOTTOM)

b1 = Button(frame1, text="360p", font=10, width=7, command=lambda *args: Asvalue("360p"))
b2 = Button(frame1, text="720p", font=10, width=7, command=lambda *args: Asvalue("720p"))
b3 = Button(frame1, text="1080p", font=10, width=7, command=lambda *args: Asvalue("1080p"))
b5 = Button(frame3, text="exit", font=10, width=7, command=lambda *args: root.quit())
frame2=Frame(root)
frame2.pack()
b4 = Button(frame3, text="Enter",height=1,width=10,bg='#0052cc', command=lambda *args:(api.confirm(pop,root)))
#b4['font']=my_font

b1.pack(side=LEFT, padx=20)
b2.pack(side=LEFT, padx=20)
b3.pack(padx=20)
b4.pack(side=LEFT, padx=10)
b5.pack(side=LEFT, padx=10)
root.mainloop()
print(entry1.get())
print(ani_name.get())