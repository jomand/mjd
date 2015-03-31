##########################
# Mary Jane's Diary v1.0 #
##########################

from classes import *
from tkinter import *
from sys import *
from tkinter.filedialog import *
from PIL import Image, ImageTk

def displayMainMenu(window):
	mainMenu = Menu(window)
	window.wm_title("Mary Jane's Diary")

	fileMenu = Menu(mainMenu)
	mainMenu.add_cascade(label="File", menu=fileMenu)
	fileMenu.add_command(label="New Project", command=newProject)
	fileMenu.add_command(label="Open Current Project", command=openCurrentProject)
	fileMenu.add_command(label="Open Archived Project", command=openArchivedProject)
	fileMenu.add_separator()
	fileMenu.add_command(label="Settings", command=settings)
	fileMenu.add_command(label="Exit", command=exitProgram)

	helpMenu = Menu(mainMenu)
	mainMenu.add_cascade(label="Help", menu=helpMenu)
	helpMenu.add_command(label="About...", command=about)
	helpMenu.add_command(label="Need Help?", command=helpMe)

	window.config(menu=mainMenu)


# The functions called by the File Menu

def newProject():
	project = Project(rootWin, "New")

def openCurrentProject():
	project = Project(rootWin, "Current")

def openArchivedProject():
	project = Project(rootWin, "Archived")

def settings():
	print ("This is where you change the default settings")

def exitProgram():
	rootWin.destroy()
	quit()


# The functions called by the Help Menu

def helpMe():			# tell the user to get way high more
	from tkinter import messagebox
	print('Running helpMe now.')
	helpMessage = "You're probably complicating things. Get way high more."
	messagebox.showinfo("Need help?", helpMessage)
	
def about():			#  display the program information:
	from tkinter import messagebox
	aboutMessage = "Author: Sum Yung Gai" + '\n' + "Copyright: what's that?"
	messagebox.showinfo("Mary Jane's Diary", aboutMessage)


########################### The Main Program ##############################

canvas_width = 800
canvas_height = 800

rootWin = Tk()
rootWin.attributes('-alpha', 0.0)   # This is to make the image invisible, so it doesn't appear to shift on the screen when centered.

screenWidth = int(rootWin.winfo_screenwidth())
screenHeight = int(rootWin.winfo_screenheight())
xOffset = int((screenWidth-454)/2)
yOffset = int((screenHeight-343)/2)

rootWin.geometry('{}x{}+{}+{}'.format(int(454), int(343), xOffset, yOffset))
rootWin.attributes('-alpha', 1.0)   # This makes the window visible again, after being centered.

topLeftFrame = Frame(rootWin)
topLeftFrame.grid(row=1, column=1)

topRightFrame = Frame(rootWin)
topRightFrame.grid(row=1, column=2)

bottomLeftFrame = Frame(rootWin)
bottomLeftFrame.grid(row=2, column=1)

bottomRightFrame = Frame(rootWin)
bottomRightFrame.grid(row=2, column=2)

img = PhotoImage(file="..\images\leaf01.ppm")
imageLabel1 = Label(topLeftFrame, image=img, text="Boy Howdy!!")
imageLabel1.grid(row=0, column=0)

displayMainMenu(rootWin)

rootWin.mainloop()
