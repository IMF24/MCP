from tkinter import *
from PIL import Image, ImageTk
from tkinter.font import *
import webbrowser
import Constants

def openAboutInfo():
    aboutRoot = Tk()
    aboutRoot.title("About MCP and Credits")
    aboutRoot.iconbitmap('GUI/icon.ico')
    aboutRoot.configure(bg='#292D3E')

    logoImage = ImageTk.PhotoImage(Image.open('GUI/icon.png'))

    logoLabel = Label(aboutRoot, image=logoImage).grid(row=0, column=0)

    infoVersionLabel = Label(aboutRoot, text=f"About The Most Complete Charting Program\n\nVersion {Constants.version}")

    aboutRoot.mainloop()