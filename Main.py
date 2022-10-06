# Import needed modules
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter.font import *
import Text
import Constants
import MenuFunctions


# Window setup
root = Tk()
root.title(f"The Most Complete Charting Program - V{Constants.version}")
root.iconbitmap('GUI/icon.ico')
root.geometry("1280x768")
root.state('zoomed')
root.configure(bg='#292D3E')
root.minsize(720, 480)

# Base menu item
baseMenu = Menu(root, activebackground='#AABBFF')
root.config(menu=baseMenu)

# Empty command (placeholder)
def noCommand():
    pass

# ======================================================================================================
# IMAGE FILE DECLARATIONS
# 
# FILE MENU
# ======================================================================================================
# File > New Chart File
newFileImage = ImageTk.PhotoImage(Image.open('GUI/fileMenu/new_file.ico'))

# File > Open Chart File
openFileImage = ImageTk.PhotoImage(Image.open('GUI/fileMenu/open_file.ico'))

# File > Save Chart File
saveFileImage = ImageTk.PhotoImage(Image.open('GUI/fileMenu/save_file.ico'))

# File > Save Chart As
saveFileAsImage = ImageTk.PhotoImage(Image.open('GUI/fileMenu/save_file_as.ico'))

# File > Export Chart Package
exportImage = ImageTk.PhotoImage(Image.open('GUI/fileMenu/export_file.ico'))

# File > Export Chart Package > As CHART
exportChartImage = ImageTk.PhotoImage(Image.open('GUI/fileMenu/export_as_chart.ico'))

# File > Export Chart Package > As MID/MIDI
exportMIDIImage = ImageTk.PhotoImage(Image.open('GUI/fileMenu/export_as_midi.ico'))

# File > Export Chart Package > GH3
exportGH3Image = ImageTk.PhotoImage(Image.open('GUI/exportLogos/gh3.ico'))

# File > Export Chart Package > GHWTDE
exportWTDEImage = ImageTk.PhotoImage(Image.open('GUI/exportLogos/wtde.ico'))

# File > Export Chart Package > RB2/3
exportRBImage = ImageTk.PhotoImage(Image.open('GUI/exportLogos/rb.ico'))

# File > Export Chart Package > CH
exportCHImage = ImageTk.PhotoImage(Image.open('GUI/exportLogos/ch.ico'))

# File > Close MCP
closeImage = ImageTk.PhotoImage(Image.open('GUI/fileMenu/exit_program.ico'))

# ======================================================================================================
# EDIT MENU
# ======================================================================================================
# Edit > Undo
undoImage = ImageTk.PhotoImage(Image.open('GUI/editMenu/undo.ico'))

# Edit > Redo
redoImage = ImageTk.PhotoImage(Image.open('GUI/editMenu/redo.ico'))

# Edit > Action History
actionHistoryImage = ImageTk.PhotoImage(Image.open('GUI/editMenu/action_history.ico'))

# Edit > Cut
cutImage = ImageTk.PhotoImage(Image.open('GUI/editMenu/cut.ico'))

# Edit > Copy
copyImage = ImageTk.PhotoImage(Image.open('GUI/editMenu/copy.ico'))

# Edit > Paste
pasteImage = ImageTk.PhotoImage(Image.open('GUI/editMenu/paste.ico'))

# Edit > Delete
deleteImage = ImageTk.PhotoImage(Image.open('GUI/editMenu/delete.ico'))

# Edit > Empty Copy Buffer
emptyCopyImage = ImageTk.PhotoImage(Image.open('GUI/editMenu/empty_copy_buffer.ico'))

# Edit > Select All
selectAllImage = ImageTk.PhotoImage(Image.open('GUI/editMenu/select_all.ico'))

# Edit > Deselect All
deselectAllImage = ImageTk.PhotoImage(Image.open('GUI/editMenu/deselect_all.ico'))

# Edit > Find
findImage = ImageTk.PhotoImage(Image.open('GUI/editMenu/find.ico'))

# Edit > Replace
replaceImage = ImageTk.PhotoImage(Image.open('GUI/editMenu/replace.ico'))

# Edit > Edit Preferences
settingsImage = ImageTk.PhotoImage(Image.open('GUI/editMenu/settings.ico'))

# ======================================================================================================
# VIEW MENU
# ======================================================================================================
# View > Zoom In
zoomInImage = ImageTk.PhotoImage(Image.open('GUI/viewMenu/zoom_in.ico'))

# View > Zoom Out
zoomOutImage = ImageTk.PhotoImage(Image.open('GUI/viewMenu/zoom_out.ico'))

# View > Fit to Screen
fitToScreenImage = ImageTk.PhotoImage(Image.open('GUI/viewMenu/fit_to_screen.ico'))

# View > Reset Aspect Ratio
resetAspectRatioImage = ImageTk.PhotoImage(Image.open('GUI/viewMenu/reset_aspect_ratio.ico'))

# View > Editing Interface
editingInterfaceImage = ImageTk.PhotoImage(Image.open('GUI/viewMenu/editing_brush.ico'))

# View > Set Scroll Speed
scrollSpeedImage = ImageTk.PhotoImage(Image.open('GUI/viewMenu/scroll_speed.ico'))

# View > Merge Local and Global Tracks
mergeEditingTracksImage = ImageTk.PhotoImage(Image.open('GUI/viewMenu/merge_tracks.ico'))

# View > Show/Hide Strike Line
strikeLineVisiblityImage = ImageTk.PhotoImage(Image.open('GUI/viewMenu/show_hide_strike_line.ico'))

# View > Set Opacity
chartOpacityImage = ImageTk.PhotoImage(Image.open('GUI/viewMenu/highway_opacity.ico'))

# ======================================================================================================
# TOOLS MENU
# ======================================================================================================
# Tools > Mouse/Select Tool
mouseImage = ImageTk.PhotoImage(Image.open('GUI/toolsMenu/mouse.ico'))

# Tools > Add Note
noteToolImage = ImageTk.PhotoImage(Image.open('GUI/toolsMenu/note.ico'))

# Tools > Add Star Power Phrase
spToolImage = ImageTk.PhotoImage(Image.open('GUI/toolsMenu/sp.ico'))

# Tools > Add BPM
bpmToolImage = ImageTk.PhotoImage(Image.open('GUI/toolsMenu/bpm.ico'))

# Tools > Add Time Signature
tsToolImage = ImageTk.PhotoImage(Image.open('GUI/toolsMenu/time_signature.ico'))

# Tools > Add Section
sectionToolImage = ImageTk.PhotoImage(Image.open('GUI/toolsMenu/section.ico'))

# Tools > Add Global Event
globalEventToolImage = ImageTk.PhotoImage(Image.open('GUI/toolsMenu/global_event.ico'))

# Tools > Add Local Event
localEventToolImage = ImageTk.PhotoImage(Image.open('GUI/toolsMenu/local_event.ico'))

# Tools > Erase/Delete Tool
eraseToolImage = ImageTk.PhotoImage(Image.open('GUI/toolsMenu/erase.ico'))

# Tools > BPM Calculator
bpmCalcToolImage = ImageTk.PhotoImage(Image.open('GUI/toolsMenu/bpm_calc.ico'))

# Tools > Tempo Metronome
metronomeToolImage = ImageTk.PhotoImage(Image.open('GUI/toolsMenu/metronome.ico'))

# Tools > Note Hit Clap
clapToolImage = ImageTk.PhotoImage(Image.open('GUI/toolsMenu/note_clap.ico'))

# Tools > Use Extended Sustains
extSustainsToolImage = ImageTk.PhotoImage(Image.open('GUI/toolsMenu/extended_sustains.ico'))

# Tools > Use Note Tool in Keys Mode
keysModeToolImage = ImageTk.PhotoImage(Image.open('GUI/toolsMenu/keys_mode.ico'))

# Tools > Multiply BPM
bpmMultiplyImage = ImageTk.PhotoImage(Image.open('GUI/toolsMenu/bpm_multiply.ico'))

# ======================================================================================================
# NOTE MENU
# ======================================================================================================
# Note > Add Note to Track
addNoteImage = ImageTk.PhotoImage(Image.open('GUI/noteMenu/add_note.ico'))

# Note > Note Properties
notePropertiesImage = ImageTk.PhotoImage(Image.open('GUI/noteMenu/note_properties.ico'))

# Note > Nudge Note
noteNudgeIconImage = ImageTk.PhotoImage(Image.open('GUI/noteMenu/note_nudge.ico'))

# ======================================================================================================
# TRACK MENU
# ======================================================================================================
# Track > Select Track
trackSelectImage = ImageTk.PhotoImage(Image.open('GUI/trackMenu/track.ico'))

# Track > Select Track > Guitar Hero > Lead Guitar - PART GUITAR
partGuitarImage = ImageTk.PhotoImage(Image.open('GUI/trackMenu/guitar.ico'))

# Track > Select Track > Guitar Hero > Bass Guitar - PART BASS
partBassImage = ImageTk.PhotoImage(Image.open('GUI/trackMenu/bass.ico'))

# Track > Select Track > Guitar Hero > Drums - PART DRUMS
partDrumsImage = ImageTk.PhotoImage(Image.open('GUI/trackMenu/drums.ico'))

# Track > Select Track > Guitar Hero > Vocals - PART VOCALS
partVocalsImage = ImageTk.PhotoImage(Image.open('GUI/trackMenu/vocals.ico'))

# Track > Select Track > Guitar Hero > Difficulty
diffBeginnerImage = ImageTk.PhotoImage(Image.open('GUI/trackMenu/beginner.ico'))

# Track > Select Track > Guitar Hero > Difficulty > Easy
diffEasyImage = ImageTk.PhotoImage(Image.open('GUI/trackMenu/easy.ico'))

# Track > Select Track > Guitar Hero > Difficulty > Medium
diffMediumImage = ImageTk.PhotoImage(Image.open('GUI/trackMenu/medium.ico'))

# Track > Select Track > Guitar Hero > Difficulty > Hard
diffHardImage = ImageTk.PhotoImage(Image.open('GUI/trackMenu/hard.ico'))

# Track > Select Track > Guitar Hero > Difficulty > Expert
diffExpertImage = ImageTk.PhotoImage(Image.open('GUI/trackMenu/expert.ico'))

# Track > Audio Time Shift
audioShiftImage = ImageTk.PhotoImage(Image.open('GUI/trackMenu/audio_shift.ico'))

# Track > Show/Hide Audio Waveform
audioWavesImage = ImageTk.PhotoImage(Image.open('GUI/trackMenu/audio_waveform.ico'))

# ======================================================================================================
# HELP MENU
# ======================================================================================================
# Help > About MCP and Credits
aboutIconImage = ImageTk.PhotoImage(Image.open('GUI/helpMenu/about.ico'))

# Help > Legal Information
alertIconImage = ImageTk.PhotoImage(Image.open('GUI/helpMenu/alert.ico'))

# Help > Help
helpIconImage = ImageTk.PhotoImage(Image.open('GUI/helpMenu/help.ico'))

# Help > IMF Games Hub & Support
discordIconImage = ImageTk.PhotoImage(Image.open('GUI/helpMenu/discord_logo.ico'))

# ======================================================================================================
# MENU DEFINITION
# ======================================================================================================
# File Menu
fileMenu = Menu(baseMenu, tearoff=0, activebackground='#AABBFF', activeforeground='#000000')
baseMenu.add_cascade(label=Text.fileMenuName, menu=fileMenu)
fileMenu.add_command(label=" New Chart File...", command=MenuFunctions.newChart, accelerator="(CTRL + N)", compound='left', image=newFileImage)
root.bind_all('<Control-n>', MenuFunctions.newChart)
fileMenu.add_command(label=" Open Chart File...", command=MenuFunctions.openChart, accelerator="(CTRL + O)", compound='left', image=openFileImage)
fileMenu.add_command(label=" Save Chart File", command=noCommand, accelerator="(CTRL + S)", compound='left', image=saveFileImage)
fileMenu.add_command(label=" Save Chart As...", command=noCommand, accelerator="(CTRL + SHIFT + S)", compound='left', image=saveFileAsImage)

# Sub menu under File > Export Chart Package
fileImportMenu = Menu(fileMenu, tearoff=0, activebackground='#AABBFF', activeforeground='#000000')
fileMenu.add_cascade(label=" Export Chart Package", menu=fileImportMenu, compound='left', image=exportImage)
fileImportMenu.add_command(label=" As CHART...", command=noCommand, accelerator="(CTRL + E)", compound='left', image=exportChartImage)
fileImportMenu.add_command(label=" As MID/MIDI...", command=noCommand, accelerator="(CTRL + SHIFT + E)", compound='left', image=exportMIDIImage)
fileImportMenu.add_separator()
fileImportMenu.add_command(label=" Guitar Hero III/III: Aerosmith Package...", command=noCommand, compound='left', image=exportGH3Image)
fileImportMenu.add_command(label=" GH World Tour Definitive Edition Package...", command=noCommand, compound='left', image=exportWTDEImage)
fileImportMenu.add_command(label=" Rock Band 2/3 Package...", command=noCommand, compound='left', image=exportRBImage)
fileImportMenu.add_command(label=" Clone Hero (CH) Package...", command=noCommand, compound='left', image=exportCHImage)

fileMenu.add_separator()
fileMenu.add_command(label=" Close MCP", command=root.quit, accelerator="(CTRL + ESC) (ALT + F4)", compound='left', image=closeImage)


# Edit Menu
editMenu = Menu(baseMenu, tearoff=0, activebackground='#AABBFF', activeforeground='#000000')
baseMenu.add_cascade(label="Edit", menu=editMenu)

editMenu.add_command(label=" Undo", command=noCommand, accelerator="(CTRL + Z)", compound='left', image=undoImage)
editMenu.add_command(label=" Redo", command=noCommand, accelerator="(CTRL + Y)", compound='left', image=redoImage)
editMenu.add_command(label=" Action History...", command=noCommand, accelerator="(CTRL + SHIFT + Z)", compound='left', image=actionHistoryImage)
editMenu.add_separator()
editMenu.add_command(label=" Cut", command=noCommand, accelerator="(CTRL + X)", compound='left', image=cutImage)
editMenu.add_command(label=" Copy", command=noCommand, accelerator="(CTRL + C)", compound='left', image=copyImage)
editMenu.add_command(label=" Paste", command=noCommand, accelerator="(CTRL + V)", compound='left', image=pasteImage)
editMenu.add_command(label=" Delete", command=noCommand, accelerator="(DEL)", compound='left', image=deleteImage)
editMenu.add_command(label=" Empty Copy Buffer", command=noCommand, accelerator="(CTRL + ALT + X)", compound='left', image=emptyCopyImage)
editMenu.add_separator()
editMenu.add_command(label=" Select All", command=noCommand, accelerator="(CTRL + A)", compound='left', image=selectAllImage)
editMenu.add_command(label=" Deselect All", command=noCommand, accelerator="(CTRL + SHIFT + A)", compound='left', image=deselectAllImage)
editMenu.add_separator()
editMenu.add_command(label=" Find...", command=noCommand, accelerator="(CTRL + F)", compound='left', image=findImage)
editMenu.add_command(label=" Replace...", command=noCommand, accelerator="(CTRL + G)", compound='left', image=replaceImage)
editMenu.add_separator()
editMenu.add_command(label=" Edit Preferences", accelerator="(F2)", compound='left', image=settingsImage)

# View Menu
viewMenu = Menu(baseMenu, tearoff=0, activebackground='#AABBFF', activeforeground='#000000')
baseMenu.add_cascade(label="View", menu=viewMenu)

viewMenu.add_command(label=" Zoom In", command=noCommand, accelerator="(CTRL + +)", compound='left', image=zoomInImage)
viewMenu.add_command(label=" Zoom Out", command=noCommand, accelerator="(CTRL + -)", compound='left', image=zoomOutImage)
viewMenu.add_command(label=" Fit to Screen", command=noCommand, accelerator="(CTRL + =)", compound='left', image=fitToScreenImage)
viewMenu.add_command(label=" Reset Aspect Ratio", command=noCommand, accelerator="(CTRL + SHIFT + =)", compound='left', image=resetAspectRatioImage)
viewMenu.add_separator()

# Sub menu under View > Editing Interface
viewInterfaceMenu = Menu(viewMenu, tearoff=0, activebackground='#AABBFF', activeforeground='#000000')
viewMenu.add_cascade(label=" Editing Interface", menu=viewInterfaceMenu, compound='left', image=editingInterfaceImage)
viewInterfaceMenu.add_command(label=" Set Scroll Speed...", command=noCommand, accelerator="(ALT + ↑)", compound='left', image=scrollSpeedImage)
viewInterfaceMenu.add_checkbutton(label=" Merge Local and Global Tracks", command=noCommand, accelerator="(CTRL + ALT + SHIFT + G)", compound='left', image=mergeEditingTracksImage)
viewInterfaceMenu.add_checkbutton(label=" Show/Hide Strike Line", command=noCommand, accelerator="(ALT + ↓)", compound='left', image=strikeLineVisiblityImage)
viewInterfaceMenu.add_command(label=" Set Opacity...", command=noCommand, accelerator="(ALT + O)", compound='left', image=chartOpacityImage)

# Tools Menu
toolsMenu = Menu(baseMenu, tearoff=0, activebackground='#AABBFF', activeforeground='#000000')
baseMenu.add_cascade(label="Tools", menu=toolsMenu)
toolsMenu.add_radiobutton(label=" Mouse/Select Tool", command=noCommand, accelerator="(J)", compound='left', image=mouseImage)
toolsMenu.add_radiobutton(label=" Add Note", command=noCommand, accelerator="(Y)",  compound='left', image=noteToolImage)
toolsMenu.add_radiobutton(label=" Add Star Power Phrase", command=noCommand, accelerator="(U)", compound='left', image=spToolImage)
toolsMenu.add_radiobutton(label=" Add BPM", command=noCommand, accelerator="(I)", compound='left', image=bpmToolImage)
toolsMenu.add_radiobutton(label=" Add Time Signature", command=noCommand, accelerator="(O)", compound='left', image=tsToolImage)
toolsMenu.add_radiobutton(label=" Add Section", command=noCommand, accelerator="(P)", compound='left', image=sectionToolImage)
toolsMenu.add_radiobutton(label=" Add Global Event", command=noCommand, accelerator="(L)", compound='left', image=globalEventToolImage)
toolsMenu.add_radiobutton(label=" Add Local Event", command=noCommand, accelerator="(;)", compound='left', image=localEventToolImage)
toolsMenu.add_radiobutton(label=" Erase/Delete Tool", command=noCommand, accelerator="(K)", compound='left', image=eraseToolImage)
toolsMenu.add_separator()
toolsMenu.add_checkbutton(label=" BPM Calculator", command=noCommand, accelerator="(CTRL + SHIFT + B)", compound='left', image=bpmCalcToolImage)
toolsMenu.add_checkbutton(label=" Tempo Metronome", command=noCommand, accelerator="(M)", compound='left', image=metronomeToolImage)
toolsMenu.add_checkbutton(label=" Note Hit Clap", command=noCommand, accelerator="(N)", compound='left', image=clapToolImage)
toolsMenu.add_separator()
toolsMenu.add_checkbutton(label=" Use Extended Sustains", command=noCommand, accelerator="(E)", compound='left', image=extSustainsToolImage)
toolsMenu.add_checkbutton(label=" Use Note Tool in Keys Mode", command=noCommand, accelerator="(GRAVE / `)", compound='left', image=keysModeToolImage)
toolsMenu.add_separator()
toolsMenu.add_command(label=" Multiply BPM...", command=noCommand, accelerator="(CTRL + *)", compound='left', image=bpmMultiplyImage)






# Note Menu
noteMenu = Menu(baseMenu, tearoff=0, activebackground='#AABBFF', activeforeground='#000000')
baseMenu.add_cascade(label="Note", menu=noteMenu)

noteMenu.add_command(label=" Add Note to Track...", command=noCommand, compound='left', image=addNoteImage)
noteMenu.add_command(label=" Note Properties...", command=noCommand, compound='left', image=notePropertiesImage)
noteMenu.add_command(label=" Nudge Note...", command=noCommand, accelerator="(ALT + →)", compound='left', image=noteNudgeIconImage)
noteMenu.add_command(label=" Reset Note Properties", command=noCommand, accelerator="(ALT + R)")
noteMenu.add_separator()
noteMenu.add_command(label=" Delete Note", command=noCommand, accelerator="(DEL)", compound='left')

# Track Menu
trackMenu = Menu(baseMenu, tearoff=0, activebackground='#AABBFF', activeforeground='#000000')
baseMenu.add_cascade(label="Track", menu=trackMenu)

# Sub menu under Track > Select Track
trackSelectMenu = Menu(trackMenu, tearoff=0, activebackground='#AABBFF', activeforeground='#000000')
trackMenu.add_cascade(label=" Select Track", menu=trackSelectMenu, compound='left', image=trackSelectImage)

# Sub menu under Track > Select Track > Guitar Hero
trackSelectGHMenu = Menu(trackSelectMenu, tearoff=0, activebackground='#AABBFF', activeforeground='#000000')
trackSelectMenu.add_cascade(label=" Guitar Hero", menu=trackSelectGHMenu)
trackSelectGHMenu.add_radiobutton(label=" Lead Guitar - PART GUITAR", command=noCommand, compound='left', image=partGuitarImage)
trackSelectGHMenu.add_radiobutton(label=" Bass Guitar - PART BASS", command=noCommand, compound='left', image=partBassImage)
trackSelectGHMenu.add_radiobutton(label=" Drums - PART DRUMS", command=noCommand, compound='left', image=partDrumsImage)
trackSelectGHMenu.add_radiobutton(label=" Vocals - PART VOCALS", command=noCommand, compound='left', image=partVocalsImage)

trackSelectGHMenu.add_separator()

# Difficulty Selection
trackSelectGHDiffMenu = Menu(trackSelectGHMenu, tearoff=0, activebackground='#AABBFF', activeforeground='#000000')
trackSelectGHMenu.add_cascade(label=" Difficulty", menu=trackSelectGHDiffMenu, compound='left', image=diffBeginnerImage)
trackSelectGHDiffMenu.add_radiobutton(label=" Easy", command=noCommand, accelerator="(SHIFT + F5)", compound='left', image=diffEasyImage)
trackSelectGHDiffMenu.add_radiobutton(label=" Medium", command=noCommand, accelerator="(SHIFT + F6)", compound='left', image=diffMediumImage)
trackSelectGHDiffMenu.add_radiobutton(label=" Hard", command=noCommand, accelerator="(SHIFT + F7)", compound='left', image=diffHardImage)
trackSelectGHDiffMenu.add_radiobutton(label=" Expert", command=noCommand, accelerator="(SHIFT + F8)", compound='left', image=diffExpertImage)

trackMenu.add_separator()

# Sub menu under Track > Add Item
trackAddEventMenu = Menu(trackMenu, tearoff=0, activebackground='#AABBFF', activeforeground='#000000')
trackMenu.add_cascade(label=" Add Item", menu=trackAddEventMenu)
trackAddEventMenu.add_command(label=" BPM", command=noCommand, accelerator="(SHIFT + I)")

trackMenu.add_separator()
trackMenu.add_command(label=" Audio Time Shift...", command=noCommand, accelerator="(SHIFT + TAB)", compound='left', image=audioShiftImage)
trackMenu.add_checkbutton(label=" Show/Hide Waveform", command=noCommand, accelerator="(F3)", compound='left', image=audioWavesImage)

# Song Menu
songMenu = Menu(baseMenu, tearoff=0, activebackground='#AABBFF', activeforeground='#000000')
baseMenu.add_cascade(label="Song", menu=songMenu)
songMenu.add_command(label=" Play from Cursor", command=noCommand, accelerator="(SPACE)")
songMenu.add_command(label=" Play from Last Section", command=noCommand, accelerator="(ALT + SPACE)")
songMenu.add_command(label=" Play from Beginning", command=noCommand, accelerator="(CTRL + SHIFT + SPACE)")
songMenu.add_separator()
songMenu.add_command(label=" Pause Preview", command=noCommand, accelerator="(SPACE)")
songMenu.add_command(label=" Stop Preview", accelerator="(ALT + SPACE)")
songMenu.add_checkbutton(label=" Return Cursor After Preview", command=noCommand)


# Help Menu
helpMenu = Menu(baseMenu, tearoff=0, activebackground='#AABBFF', activeforeground='#000000')
baseMenu.add_cascade(label="Help", menu=helpMenu)
helpMenu.add_command(label=" About MCP and Credits", command=MenuFunctions.aboutProgram, compound='left', image=aboutIconImage)
helpMenu.add_command(label=" Legal Information", command=MenuFunctions.legalInfo, compound='left', image=alertIconImage)
helpMenu.add_command(label=" GNU General Public License", command=MenuFunctions.licenseTermsOpen, compound='left')
helpMenu.add_separator()
helpMenu.add_command(label=" Help (User Documentation)", command=noCommand, accelerator="(F1)", compound='left', image=helpIconImage)
helpMenu.add_command(label=" IMF Games Hub & Support", command=MenuFunctions.openDiscordServer, compound='left', image=discordIconImage)
helpMenu.add_command(label=" Send Bug Report/Support Ticket", command=MenuFunctions.openTicketSubmit, compound='left')


# Enter main loop
root.mainloop()