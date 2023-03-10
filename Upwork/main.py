from tkinter import Tk, Button, Entry, Label, mainloop
from tkinter.font import Font

class API_CONFIG(object):
    def __init__(self):
        self.state = {
            'anchor': ['e', 'n', 's', 'w'],
            'expand': [False, True],
            'fill': [False, True],
            'root': [350, 0],
            'padx': 0,
            'pady': 7,
            'side': ['bottom', 'left', 'right', 'top'],
        }
        self.anime_name, self.resolution, self.first_episode, self.last_episode = '', '', '', ''
        self.master = self.Master(title='Download Preferences')
        self.ANCHOR, self.PADY, self.SIDE = self.state['anchor'][1], self.state['pady'], self.state['side'][3]
        self.default_font = Font(root=self.master, family='Helvetica', size=15, weight='bold')
        self.entry_font = Font(root=self.master, family='Helvetica', size=14, weight='normal')
        Label(self.master, text='On Data Entry, Click Submit!', font=Font(root=self.master, family='Times New Roman', size=13, weight='bold', slant='italic'), fg='red').pack(anchor=self.ANCHOR, side=self.SIDE)

    def Destroy(self):
        self.GetData()
        self.master.destroy()

    def Download(self):
        self.state['root'][1] += 60
        self.master.geometry(f"{self.state['root'][0]}x{self.state['root'][1]}")
        button = Button(self.master, text='Download', command=self.Destroy, font=self.default_font, fg='indigo', borderwidth=5, border=3, relief='ridge')
        button.pack(anchor=self.ANCHOR, pady=self.PADY, side=self.SIDE)

    def Master(self, setWidth:bool=False, setHeight:bool=False, title:str=''):
        root = Tk()
        root.geometry(f"{self.state['root'][0]}x{self.state['root'][1]}")
        root.resizable(width=setWidth, height=setHeight)
        root.title(title)
        return root

    def Frame(self, type:str='', label_text:str='', button_text:str=''):
        self.state['root'][1] += 150
        self.master.geometry(f"{self.state['root'][0]}x{self.state['root'][1]}")
        
        label = Label(self.master, text=label_text, font=self.default_font, fg='crimson')
        label.pack(anchor=self.ANCHOR, pady=self.PADY, side=self.SIDE)
        
        entry = Entry(self.master, font=self.entry_font, fg='gold')
        entry.pack(anchor=self.ANCHOR, pady=self.PADY, side=self.SIDE)
        
        def getEntry(): 
            if (type == 'anime_name'): self.anime_name = f'{entry.get()}'
            if (type == 'resolution'): 
                if (int(f'{entry.get()}') > 1080 or int(f'{entry.get()}') < 480):
                    self.resolution = '720'
                    print('Resolution Not Supported, Using Default!')
                else:
                    self.resolution = f'{entry.get()}'
            if (type == 'first_episode'): self.first_episode = f'{entry.get()}'
            if (type == 'last_episode'): self.last_episode = f'{entry.get()}'
            
        button = Button(self.master, text=button_text, command=getEntry, font=self.default_font, relief='ridge', borderwidth=5, border=3, fg='teal')
        button.pack(anchor=self.ANCHOR, pady=self.PADY, side=self.SIDE)

    def FetchAnime(self):
        self.Frame('anime_name', 'Anime Name'.upper(), 'Submit')
        self.Frame('resolution', 'Resolution [480/720/1080]'.upper(), 'Submit')
        self.Frame('first_episode', 'First Episode'.upper(), 'Submit')
        self.Frame('last_episode', 'Last Episode'.upper(), 'Submit')
        self.Download()

    def GetData(self):
        print(f'Name: {self.anime_name}\nResolution: {self.resolution}\nFirst Episode: {self.first_episode}\nLast Episode: {self.last_episode}')


if __name__ == '__main__':
    main = API_CONFIG()
    main.FetchAnime()
    mainloop()
