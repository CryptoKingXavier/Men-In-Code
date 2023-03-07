from tkinter.messagebox import askyesno
from tkinter.simpledialog import askstring, askinteger

class RestAPI:
    def __init__(self):
        self.anime_name = str()
        self.resolution = ''
        self.storage_capacity = bool()
        self.first_episode = str()
        self.last_episode = str()
        self.confirm_download = bool()

    def DownloadState(self):
        self.anime_name = askstring(title="Anime Name", prompt="Name")
        resolution = askinteger(title="Anime Resolution", prompt="Resolution [Enter 360/720/1080]")
        self.storage_capacity = askyesno(title="View Capacity", message="View Anime Video Size")
        self.first_episode = askstring(title="Anime Episode", prompt="First Episode")
        self.last_episode = askstring(title="Anime Episode", prompt="Last Episode")
        self.confirm_download = askyesno(title="Confirm Download", message="Start Download!")

        if not resolution or resolution > 1080:
            self.resolution = str(720)
        else:
            self.resolution = str(resolution)

api = RestAPI()
api.DownloadState()
