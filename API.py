from tkinter import *
from tkinter.messagebox import askyesno,showinfo
from tkinter.simpledialog import askstring, askinteger

class RestAPI:
    def __init__(self):
        self.anime_name = str()
        self.man = str()
        self.resolution = ''
        self.back=bool(False)
        self.storage_capacity = bool()
        self.first_episode = int()
        self.last_episode = int()
        self.confirm_download = bool()

    def DownloadState(self):
        #self.anime_name = askstring(title="Anime Name", prompt="Name")
        #self.resolution = askinteger(title="Anime Resolution", prompt="Resolution [Enter 360/720/1080]")
        self.storage_capacity = askyesno(title="View Capacity", message="View Anime Video Size")
        #self.first_episode = askstring(title="Anime Episode", prompt="First Episode")
        #self.last_episode = askstring(title="Anime Episode", prompt="Last Episode")
    def set_value(self):
        self.back=True
    def confirm(self,list2,tkin_root=None):
        roo=Toplevel()
        ace="Select anime"
        con=StringVar()
        con.set(ace)
        print(con.get())
        print("ace",ace)
        confirm_download = OptionMenu(roo, con,*list2).pack()
        roo.geometry("300x150")
        button=Button(roo, text="Back",font="Arial 12", command=lambda *args:(self.set_value(),roo.destroy())).pack(side=BOTTOM,ipadx=10,ipady=7)
        button=Button(roo, text="Enter",font="Arial 12", command=lambda *args:(self.DownloadState(),tkin_root.destroy())).pack(side=BOTTOM,ipadx=10,ipady=7)
        self.man=con
        roo.mainloop()
    def show_storage(self,x,y="is"):
        ace=showinfo("Download size","The download %s %sMB"%(y,x))
i=RestAPI()
i.confirm("Aight")
#i.show_storage(100)