from tkinter import *
from tkinter.messagebox import askyesno
from tkinter.simpledialog import askstring, askinteger

class RestAPI:
    def __init__(self):
        self.anime_name = str()
        self.resolution = ''
        self.storage_capacity = bool()
        self.first_episode = int()
        self.last_episode = int()
        self.confirm_download = bool()

    def DownloadState(self):
        self.anime_name = askstring(title="Anime Name", prompt="Name")
        self.resolution = askinteger(title="Anime Resolution", prompt="Resolution [Enter 360/720/1080]")
        self.storage_capacity = askyesno(title="View Capacity", message="View Anime Video Size")
        self.first_episode = askstring(title="Anime Episode", prompt="First Episode")
        self.last_episode = askstring(title="Anime Episode", prompt="Last Episode")
    
    def confirm(self,ace,root):
        roo=Toplevel()
        con=StringVar()
        con.set(ace)
        print(con.get())
        print("ace",ace)
        confirm_download = OptionMenu(roo, con,*["C++", "Java","Python","JavaScript","Rust","GoLang"]).pack()
        roo.geometry("360x130")
        button=Button(roo, text="quit", command=lambda *args:(root.destroy())).pack()
        button=Button(roo, text="back", command=lambda *args:(roo.destroy())).pack()
        roo.mainloop()
        return con.get()
    