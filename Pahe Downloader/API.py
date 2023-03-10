from tkinter import *
from tkinter.messagebox import askyesno,showinfo
from tkinter.simpledialog import askstring, askinteger

class RestAPI:
    def __init__(self):
        self.anime_name = str()
        self.man = str()
        self.resolution = ''
        self.back=bool(False)
        self.bac=bool(False)
        self.storage_capacity = bool()
        self.storage_check = bool()
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
    def set_value2(self):
        self.bac=True
    def confirm(self,list2,tkin_root=None):
        roo=Toplevel(tkin_root,bg="sky blue")
        frame=Frame(roo)
        frame.pack(side="bottom")
        frame.configure(bg='sky blue')
        ace="Select anime"
        con=StringVar()
        con.set(ace)
        confirm_download = OptionMenu(roo,con,*list2).pack()
        roo.geometry("430x150")
        button=Button(frame, text="Enter",font="Arial 12",bg="blue", command=lambda *args:(self.DownloadState(),tkin_root.destroy())).pack(side="left",ipadx=10,padx=10)
        button=Button(frame, text="Back",font="Arial 12",bg="red", command=lambda *args:(self.set_value(),tkin_root.quit(),roo.destroy())).pack(side="left",ipadx=10,padx=10)
        self.man=con
        roo.mainloop()
    def show_storage(self,x,y="is"):
        ace=showinfo("Download size","The download %s %sMB"%(y,x))
#i=RestAPI()

#i.show_storage(100)