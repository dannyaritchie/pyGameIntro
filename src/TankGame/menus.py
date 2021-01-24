import tkinter

class mainMenu(tkinter.Frame):
    def __init__(self, window):
        super().__init__()
        self.window = window
        self.titleLabel = tkinter.Label(self.window, text='Tank Game')
        self.titleLabel.grid(row=0, column=0, sticky='ew')
        self.titleLabel.configure(font=('Courier', '90'))
        self.quitButton = tkinter.Button(self.window, text='Quit', command=self.window.destroy)
        self.quitButton.grid(row=3, column=0, sticky='n')
        self.startButton = tkinter.Button(self.window, text='Start', command=self.window.destroy)
        self.startButton.grid(row=1, column=0, sticky='s')
        self.helpButton = tkinter.Button(self.window, text='How to play', command=self.window.destroy)
        self.helpButton.grid(row=2, column=0)

mainWindow = tkinter.Tk()
mainWindow.title('Tank Game')
mainWindow.geometry('700x500+400+100')
menu = mainMenu(mainWindow)
mainWindow.rowconfigure(0, weight=5)
mainWindow.rowconfigure(1, weight=1)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=5)
mainWindow.columnconfigure(0, weight=1)
while True:
    mainWindow.update()