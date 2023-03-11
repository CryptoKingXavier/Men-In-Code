from API import RestAPI
import threading
from tkinter import *
from tkinter import ttk
from Ult_web2 import Ani_Installer
import tkinter.font as font
web=Ani_Installer()
root=Tk()
root.title("Pahe Downloader")
root.configure(bg="sky blue")

pop=''
api=RestAPI()
style_1 = {'foreground': 'black', 'background': 'RoyalBlue3'}#, 'activebackground':'gray71', 'activeforeground': 'gray71'}
def Asvalue(x,y,a,b):
    global pop
    pop=x
    a['style']="W.TButton"
    b['style']="W.TButton"
    y['style']="A.TButton"
root.geometry("560x300")

Label(root,bg='sky blue', text="Welcome to Pahe Downloader", font="Arial 20 bold", fg = "black").pack()
style_2=ttk.Style()
style_2.theme_use('alt')
style_2.configure('A.TButton', font =('Arial', 17),foreground='#6a6c6e',background='black')
style_2.map('A.TButton', foreground = [('active', '!disabled', '#6a6c6e')], background = [('active', 'black')])
style=ttk.Style()
style.theme_use('alt')
style.configure('W.TButton', font =('Arial', 17))
style.map('W.TButton', foreground = [('active', '!disabled', '#6a6c6e')], background = [('active', 'black')])
my_font2=font.Font(font="Arial 13")
my_font=font.Font(size=15)
ani_name=StringVar()
frame = Frame(root)
frame.pack()
frame.configure(bg="sky blue")
prom=Label(frame,bg="sky blue", text="Enter anime name:", font="Arial 13", fg = "black").pack(side="left", pady=10)
entry1 = ttk.Entry(frame, justify = LEFT,)
entry1['font']=my_font2
fram = Frame(root)
fram.pack()
fram.configure(bg="sky blue")
prom2=Label(fram,bg="sky blue", text="Enter first episode:", font="Arial 13", fg = "black").pack(side="left", pady=10)
entry2 = ttk.Entry(fram, justify = LEFT,)
entry2['font']=my_font2
fra= Frame(root)
fra.pack()
fra.configure(bg="sky blue")
prom3=Label(fra,bg="sky blue", text="Enter last episode:", font="Arial 13", fg = "black").pack(side="left", pady=10)
entry3 = ttk.Entry(fra, justify = LEFT,)
entry3['font']=my_font2
entry1.pack(side = 'left', ipadx = 100, ipady = 3, pady=1)
entry2.pack(side = 'left', ipadx = 100, ipady = 3, pady=1)
entry3.pack(side = 'left', ipadx = 100, ipady = 3, pady=1)
frame1= Frame(root)
frame1.pack()
frame1.configure(bg="sky blue")
frame3= Frame(root)
frame3.pack(side=BOTTOM)
frame3.configure(bg="sky blue")

b1 = ttk.Button(frame1,style="W.TButton", text="360p", width=7, command=lambda *args: Asvalue("360p",b1,b2,b3))
b2 = ttk.Button(frame1,style="W.TButton", text="720p", width=7, command=lambda *args: Asvalue("720p",b2,b1,b3))
b3 = ttk.Button(frame1,style="W.TButton", text="1080p", width=7, command=lambda *args: Asvalue("1080p",b3,b1,b2))
b5 = Button(frame3, text="exit ",bg="red", font=10, width=7, command=lambda *args: root.quit())
frame2=Frame(root)
frame2.pack()
frame2.configure(bg="sky blue")
def set_para(x):
    x.sea=entry1.get()
    x.resol=pop
    print(pop)
    if entry2.get().strip()=="":
        x.fe=float(1)
    else:
        x.fe=float(entry2.get())
    if entry3.get().strip()=="":
        x.le=x.fe
    else:
        x.le=float(entry3.get())
    #x.search(root)
    x.downloader(root)

b4 = Button(frame3, text="Enter",height=1,width=10,bg='#0052cc', command=lambda *args:(set_para(web)))#,root.destroy()))
b4['font']=my_font
b5['font']=my_font
b1.state(['!pressed'])
b1.pack(side=LEFT, padx=20)
b2.pack(side=LEFT, padx=20)
b3.pack(padx=20)
b4.pack(side=LEFT, padx=10)
b5.pack(side=LEFT, padx=10)
b2.invoke()
root.mainloop()
print(web.restart)
