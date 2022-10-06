"""
Menu functions module.

This module houses all functions for the various menus, as well as opening windows
for the various commands executed under the Top Menu.
"""

# Import needed modules
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import filedialog
from tkinter.font import *
import webbrowser
import Text
import Constants

# ======================================================================================================
# FILE MENU FUNCTIONS
# ======================================================================================================

# ======================================================================================================
# FILE MENU FUNCTIONS
# ======================================================================================================
# New Chart File
def newChart():
    '''Calls up the New Chart File window.'''

    # Set up window
    newChartRoot = Tk()
    newChartRoot.title("New Chart File")
    newChartRoot.iconbitmap('GUI/icon.ico')
    newChartRoot.geometry("1200x750")
    newChartRoot.configure(bg='#292D3E')
    newChartRoot.resizable(False, False)

    # Add the window title
    titleLabel = Label(newChartRoot, text="New Chart File", font=("Times New Roman", 12, BOLD), bg='#292D3E', fg='#FFFFFF').grid(row=0, column=0)

    # Input song title
    songTitleLabel = Label(newChartRoot, text="Name: ", font=("Times New Roman", 12, BOLD), bg='#292D3E', fg='#FFFFFF').grid(row=1, column=1)
    songTitle = Entry(newChartRoot, width=100, font=("Times New Roman", 12, BOLD), bg='#7581AF', fg='#000000').grid(row=1, column=2)

    # Input song artist
    songArtistLabel = Label(newChartRoot, text="Artist: ", font=("Times New Roman", 12, BOLD), bg='#292D3E', fg='#FFFFFF').grid(row=2, column=1)
    songArtist = Entry(newChartRoot, width=100, font=("Times New Roman", 12, BOLD), bg='#7581AF', fg='#000000').grid(row=2, column=2)

    # Input song year
    songYearLabel = Label(newChartRoot, text="Year: ", font=("Times New Roman", 12, BOLD), bg='#292D3E', fg='#FFFFFF').grid(row=3, column=1)
    songYear = Entry(newChartRoot, width=10, font=("Times New Roman", 12, BOLD), bg='#7581AF', fg='#000000').place(x=162, y=76)
    
    # Enter main loop
    newChartRoot.mainloop()

# Open Chart File
def openChart():
    '''Calls up the Open file dialog.'''
    # Set up initial 
    openChartRoot = Tk()
    openChartRoot.iconbitmap('GUI/icon.ico')
    openChartRoot.withdraw()

    # Call the open file dialog
    openChartRoot.filename = filedialog.askopenfilename(title="Select a Chart File to Open", initialdir="c:/", filetypes=[("All Chart Files", "*.chart *.mid")])

    # Close the extra other window that gets opened.
    openChartRoot.destroy()

    

    

# ======================================================================================================
# HELP MENU FUNCTIONS
# ======================================================================================================
# About MCP and Credits
def aboutProgram():
    '''Opens the dialog displaying info and credits about the program.'''
    aboutMCPRoot = Tk()
    aboutMCPRoot.title("About MCP and Credits")
    aboutMCPRoot.iconbitmap('GUI/icon.ico')
    aboutMCPRoot.configure(bg='#292D3E')
    aboutMCPRoot.resizable(False, False)

    imageLogo = ImageTk.PhotoImage(Image.open('c:/gui/icon.png'))
    
    aboutMCPTitleLabel = Label(aboutMCPRoot, text=f"About The Most Complete Charting Program\nBy IMF24\nVersion {Constants.version}", font=("Times New Roman", 12, BOLD), bg='#292D3E', fg='#FFFFFF', justify='left').grid(row=0, column=0)

    aboutMCPMainText = """
    \u00A9 2022 IMF24, Under GPL-3

    CREDITS
    Edit Preferences Icon, Note Hit Clap Icon
    By OpenMoji 14.0, under CC BY SA 4.0 International
    => https://creativecommons.org/licenses/by-sa/4.0
    => Scaled down to 16 X 16 ICO files to fit in the top menus

    Instrument Icons \u00A9 2008 Neversoft
    Difficulty Icons \u00A9 2008 Neversoft
    Guitar Hero III Logo \u00A9 2007 Neversoft
    Rock Band Logo \u00A9 Harmonix
    GHWT Definitive Edition Logo \u00A9 2021 WTDE Modding Team
    Original GH World Tour Logo \u00A9 2008 Neversoft
    Clone Hero Logo \u00A9 Clone Hero Team
    Discord Logo \u00A9 2020 Discord Inc.

    The instrument icons shown for the track selection menu
    consist only of simple geometric shapes and/or text.
    Therefore, they do not meet the threshold of originality
    that is needed for copyright protection and are in the
    public domain. Though free of copyright restrictions,
    these images may be subject to other restrictions.

    Any low-resolution rendering of these copyrighted
    images for informational or educational purposes
    constitutes fair use under United States copyright
    law. (Title 17, U.S.C.)

    To view the license terms of the GPL-3 License, go to
    Help > GNU General Public License.
    """

    mainTextLabel = Label(aboutMCPRoot, text=aboutMCPMainText, font=("Times New Roman", 12, BOLD), bg='#292D3E', fg='#FFFFFF', justify='left').grid(row=1, column=0)

    aboutMCPInfoOKButton = Button(aboutMCPRoot, text="OK", command=aboutMCPRoot.destroy, activebackground='#AABBFF', bg='#7581AF', activeforeground='#FFFFFF', fg='#000000', font=("Times New Roman", 12, BOLD), width=10).grid(row=2, column=0)

    aboutMCPRoot.mainloop()

# Legal Information
def legalInfo():
    '''Opens the dialog displaying legal information when using the program.'''
    legalInfoRoot = Tk()
    legalInfoRoot.title("Legal Information")
    legalInfoRoot.iconbitmap('GUI/icon.ico')
    legalInfoRoot.configure(bg='#292D3E')
    legalInfoRoot.resizable(False, False)

    legalInfoText = """LEGAL INFORMATION
    
    You are liable for any unlawful use of this program. If
    you misuse this program to create custom charts that use
    pirated music tracks, IT IS NOT the fault of the applicable
    developer(s) of this application.

    By using this program, you are accepting legal responsiblity
    that piracy is a serious crime and that you can be fined
    up to $250,000 (by the Federal Bureau of Investigation under
    United States copyright law, Title 17, U.S.C.) if caught.
    """

    legalInfoTitleLabel = Label(legalInfoRoot, text=legalInfoText, font=("Times New Roman", 12, BOLD), bg='#292D3E', fg='#FFFFFF', justify='left').grid(row=0, column=0)

    legalInfoOKButton = Button(legalInfoRoot, text="OK", command=legalInfoRoot.destroy, activebackground='#AABBFF', bg='#7581AF', activeforeground='#FFFFFF', fg='#000000', font=("Times New Roman", 12, BOLD), width=10).grid(row=1, column=0)

    legalInfoRoot.mainloop()

# 
def licenseTermsOpen():
    '''Opens the dialog displaying program's license information when using the program.'''
    licenseTermsRoot = Tk()
    licenseTermsRoot.title("GNU General Public License")
    licenseTermsRoot.iconbitmap('GUI/icon.ico')
    licenseTermsRoot.configure(bg='#292D3E')
    licenseTermsRoot.geometry("740x480")
    licenseTermsRoot.resizable(False, False)

    # Open the file containing the GNU License terms.
    licenseTextFile = open("LICENSE.txt")
    licenseText = licenseTextFile.read()

    # Make the frame and canvas to hold the text in.
    licenseInfoFrame1 = Frame(licenseTermsRoot)
    licenseInfoFrame1.pack(fill='both', expand=1)

    licenseInfoCanvas = Canvas(licenseInfoFrame1)
    licenseInfoCanvas.pack(side='left', fill='both', expand=1)

    # Add the scroll bar.
    licenseInfoScrollBar = ttk.Scrollbar(licenseInfoFrame1, orient='vertical', command=licenseInfoCanvas.yview)
    licenseInfoScrollBar.pack(side='right', fill='y')

    # Configure the canvas and bind the scroll bar.
    licenseInfoCanvas.configure(yscrollcommand=licenseInfoScrollBar.set)
    licenseInfoCanvas.bind('<Configure>', lambda e: licenseInfoCanvas.configure(scrollregion=licenseInfoCanvas.bbox('all')))

    # Add the second frame.
    licenseInfoFrame2 = Frame(licenseInfoCanvas)
    licenseInfoCanvas.create_window((0, 0), window=licenseInfoFrame2, anchor='nw')

    # Add license text.
    licenseTextLabel = Label(licenseInfoFrame2, text=licenseText, font=("Times New Roman", 12, BOLD), bg='#292D3E', fg='#FFFFFF', justify='left').grid(row=0, column=0)

    # OK button.
    licenseInfoOKButton = Button(licenseTermsRoot, text="OK", command=licenseTermsRoot.destroy, activebackground='#AABBFF', bg='#7581AF', activeforeground='#FFFFFF', fg='#000000', font=("Times New Roman", 12, BOLD), width=10)

    licenseTermsRoot.mainloop()




def openDiscordServer():
    webbrowser.open('https://discord.gg/gUEWE325qT')
    pass

def openTicketSubmit():
    webbrowser.open('https://docs.google.com/forms/d/e/1FAIpQLSeFayYEkB52MXQYiljGSKNV3TihWEwtQn26RC0vxBKtWcTAbA/viewform')
    pass

