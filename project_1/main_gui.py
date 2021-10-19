import tkinter
import tkinter.messagebox
import cv2
import matplotlib.pyplot as plt
import Pmw
from PIL import Image, ImageTk
import main


class APP():
    ''' GUI '''
    def __init__(self, win):
        self.bt_team = tkinter.Button(win, text='Team buildup', command=self.show_team)
        self.bt_team_window = canvas.create_window(80, 400, anchor=tkinter.NW, window=self.bt_team)
        self.bt_news = tkinter.Button(win, text='Latest News', command=self.show_news)
        self.bt_news_window = canvas.create_window(430, 400, anchor=tkinter.NW, window=self.bt_news)
        self.bt_image = tkinter.Button(win, text='Player image', command=self.show_image)
        self.bt_image_window = canvas.create_window(330, 450, anchor=tkinter.NW, window=self.bt_image)
        self.bt_song = tkinter.Button(win, text='Related songs', command=self.show_song)
        self.bt_song_window = canvas.create_window(180, 450, anchor=tkinter.NW, window=self.bt_song)

    def show_news(self):
        new_m = main.get_news()
        news_content = '\n'.join(new_m)
        Pmw.MessageDialog(win, title="FCB latest news", message_text=news_content)

    def show_team(self):
        name_lis, image_d = main.get_team()
        name_content = '\n'.join(name_lis)
        Pmw.MessageDialog(win, title="FCB team buildup", message_text=name_content)

    def show_image(self):
        name = var.get()
        main.download_image(name)
        img = cv2.imread(name + '.jpg')
        plt.imshow(img)
        plt.show()

    def show_song(self):
        name = var.get()
        song_n = main.itunes(name)
        song_content = '\n'.join(song_n)
        Pmw.MessageDialog(win, title="FCB team buildup", message_text=song_content)


# create a main window
win = tkinter.Tk()
win.title('About FCB')
win.iconbitmap('FCB.ico')
win.geometry('600x534+400+50')


# set background image
canvas = tkinter.Canvas(win, width=600, height=534)
canvas.pack()
img = ImageTk.PhotoImage(Image.open('fcb.png').resize((600, 534), Image.ANTIALIAS))
canvas.background = img
bg = canvas.create_image(0, 0, anchor=tkinter.NW, image=img)


# enable input on GUI
var = tkinter.StringVar()
entry = tkinter.Entry(win, textvariable=var, bd=3)
entry_window = canvas.create_window(230, 400, anchor=tkinter.NW, window=entry)

app = APP(win)

win.mainloop()