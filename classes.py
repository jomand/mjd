class Project:
	def __init__(self, rootWin, status):
		tk = __import__('tkinter')
		
		self.projectData={}
		self.numFields = 15
		self.status = status
		self.displayProjectWindow(rootWin)
		self.formFields = ["Project Name", "Start Date", "End Date", "Grow Space", "Lights", "Light Schedule",
			"Nutrients Brand", "Nutrients Level", "Feed Frequency", "Group 1 Strain", "Group 1 Number", "Group 2 Strain",
			"Group 2 Number", "Group 3 Strain", "Group 3 Number"]
		
		if self.status == "New":
			self.startNewProject()
		elif self.status == "Current":
			self.openCurrentProject()
		elif self.status == "Archived":
			self.openArchivedProject()

	def displayProjectWindow(self, rootWin):
		from graphics import color_rgb
		tk = __import__('tkinter')

		img = tk.PhotoImage(file="..\images\leaf01.ppm")
		
		self.projectWin = tk.Toplevel(rootWin)
		self.projectWin.wm_title("Mary Jane's Diary")
		
		# color_rgb(0, 50, 0))
		projectMenu = tk.Menu(self.projectWin)
		self.projectWin.wm_title("Mary Jane's Diary")
		screenWidth = int(rootWin.winfo_screenwidth())
		screenHeight = int(rootWin.winfo_screenheight())
		xOffset = int((screenWidth-758)/2)
		yOffset = int((screenHeight-416)/2)
		self.projectWin.geometry('{}x{}+{}+{}'.format(int(758), int(416), xOffset, yOffset))
		
		plantMenu = tk.Menu(projectMenu)
		projectMenu.add_cascade(label="Plants", menu=plantMenu)
		plantMenu.add_command(label="Add Group", command=self.addGroup)
		plantMenu.add_command(label="Remove Group", command=self.removeGroup)
		plantMenu.add_command(label="Add to Group", command=self.addToGroup)
		plantMenu.add_command(label="Remove from Group", command=self.removeFromGroup)
		plantMenu.add_command(label="Transplant Group", command=self.transplantGroup)

		logMenu = tk.Menu(projectMenu)
		projectMenu.add_cascade(label="Logs", menu=logMenu)
		logMenu.add_command(label="New Log Entry", command=self.newLogEntry)
		logMenu.add_command(label="Edit Log Entry", command=self.editLogEntry)

		dataMenu = tk.Menu(projectMenu)
		projectMenu.add_cascade(label="Project Data", menu=dataMenu)
		dataMenu.add_command(label="Edit Project Data", command=self.editProjectData)
		
		quitMenu = tk.Menu(projectMenu)
		projectMenu.add_cascade(label="Save", menu=quitMenu)
		quitMenu.add_command(label="Save Data", command=self.saveProjectData)
		quitMenu.add_command(label="Return to Main Menu", command=self.returnToMain)
		
		self.projectWin.config(menu=projectMenu)
				
	def startNewProject(self):
		tk = __import__("tkinter")

		self.numFields = 15
		self.projectStrVars = {}
		img = tk.PhotoImage(file="..\images\leaf01.ppm")
		
		projectSetupFrame = tk.LabelFrame(self.projectWin, width=800, height=400, text="Project Setup: ")
		projectSetupFrame.grid(row=0, column=0, columnspan=3, sticky='WE', padx=5, pady=5, ipadx=5, ipady=5)

		# input and store all project data from user.
			# Name
			# Start Date
			# End (Harvest) Date (initially set to NONE) Number of days total is calculated from these
			# Grow Space (which cabinet, compartment, etc. Pre-defined ones are listed. User selects. "Add" at bottom of list goes to createGrowSpace(), then back here)
			# Light (which light - will be part of the Grow Space)
			# Light Schedule
			# Nutrients brand
			# Nutrients Level
			# Nutrients Frequency
			# Group 1 Strain
			# Group 1 Number
			# Group 2 Strain
			# Group 2 Number
			# Group 3 Strain
			# Group 3 Number
			
		for i in range(0, self.numFields):
			tk.Label(projectSetupFrame, text=self.formFields[i]).grid(row = i+1, column = 0)
			self.projectStrVars[i] = tk.StringVar()
			entry = tk.Entry(projectSetupFrame, textvariable = self.projectStrVars[i]).grid(row = i+1, column = 1)
		
		imageLabel = tk.Label(projectSetupFrame, image=img)
		imageLabel.photo = img
		imageLabel.grid(row=1, column=3, rowspan=16, padx=5, pady=5)
		
		createButton = tk.Button(projectSetupFrame, text="Create!", command=self.storeNewProjectData)
		createButton.grid(row=20, column=0, columnspan=2)

	def storeNewProjectData(self):
		# Getting data from user requires a different approach than reading from a file.
		# The form entry field values (given by user) are stored in the list projectStrVars[]
		# The .get() accesses that entry so it can be stored in the dictionary for use by the program.
		
		# self.name = self.projectStrVars[0].get()
		self.start = self.projectStrVars[1].get()
		self.end = self.projectStrVars[2].get()
		self.space = self.projectStrVars[3].get()
		self.light = self.projectStrVars[4].get()
		self.sched = self.projectStrVars[5].get()
		self.brand = self.projectStrVars[6].get()
		self.level = self.projectStrVars[7].get()
		self.freq = self.projectStrVars[8].get()
		self.grp1strn = self.projectStrVars[9].get()
		self.grp1num = self.projectStrVars[10].get()
		self.grp2strn = self.projectStrVars[11].get()
		self.grp2num = self.projectStrVars[12].get()
		self.grp3strn = self.projectStrVars[13].get()
		self.grp3num = self.projectStrVars[14].get()

		self.projectData.clear()
		self.projectData = dict([('Project Name',self.projectStrVars[0].get()), ('Start Date', self.start), ('End Date', self.end), ('Grow Space', self.space),
			('Lights', self.light), ('Light Schedule', self.sched), ('Nutrients Brand', self.brand), ('Nutrients Level', self.level), ('Feed Frequency', self.freq),
			('Group 1 Strain', self.grp1strn), ('Group 1 Number', self.grp1num), ('Group 2 Strain', self.grp2strn), ('Group 2 Number', self.grp2num),
			('Group 3 Strain', self.grp3strn), ('Group 3 Number', self.grp3num)])

	def openCurrentProject(self):
		tk = __import__("tkinter")
		from tkinter import filedialog
		
		openFileOptions = {}
		openFileOptions['defaultextension'] = '.mjd'
		openFileOptions['filetypes'] = [("Active Project", ".mjd")]
		filename = filedialog.askopenfilename(parent=self.projectWin, **openFileOptions)
		
		with open(filename) as self.projectFile:
			for line in self.projectFile:
				key, value = line.partition(",")[::2]
				value = value.rstrip('\n')
				self.projectData.update({key:value})
		
		self.displayData(self.projectData)

	def openArchivedProject(self):
		tk = __import__("tkinter")
		from tkinter import filedialog
		
		openFileOptions = {}
		openFileOptions['defaultextension'] = '.mjb'
		openFileOptions['filetypes'] = [("Archived Project", ".mjb")]
		filename = filedialog.askopenfilename(parent=self.projectWin, **openFileOptions)
		
		with open(filename) as self.projectFile:
			for line in self.projectFile:
				key, value = line.partition(",")[::2]
				value = value.rstrip('\n')
				self.projectData.update({key:value})


	def returnToMain(self):
		self.saveProjectData()		# save data to appropriate file (.mjd or .mjb)
		self.projectWin.destroy()	# close the toplevel window and return to the main window.
		

	def editProjectData(self):
		pass
		
	def displayData(self, data):
		tk = __import__("tkinter")

		self.projectData = data
		self.projectStrVars = {}
		img = tk.PhotoImage(file="..\images\leaf01.ppm")		

		dataFrame = tk.LabelFrame(self.projectWin, width=800, height=458, text="Project Data: ")
		dataFrame.grid(row=0, column=0, columnspan=2, sticky='WE', padx=5, pady=5, ipadx=5, ipady=5)
		
		for index in range(self.numFields):
			key = self.formFields[index]
			value = self.projectData[key]
			tk.Label(dataFrame, text=key).grid(row = index+1, column = 0)
			self.projectStrVars[index] = tk.StringVar()
			entry = tk.Entry(dataFrame, textvariable = self.projectStrVars[index]).grid(row = index+1, column = 1)
			self.projectStrVars[index].set(value)

		imageLabel = tk.Label(dataFrame, image=img)
		imageLabel.photo = img
		imageLabel.grid(row=1, column=3, rowspan=16, padx=5, pady=5)
		
		updateButton = tk.Button(dataFrame, text="Update", command=self.storeNewProjectData)
		updateButton.grid(row=20, column=0, columnspan=2)
			
			
			
			
		
	def saveProjectData(self):
	
		# if the status is NEW or CURRENT, save as name.mjd, output 
		if self.status == "New" or self.status == "Current":
			self.fileName = self.projectData['Project Name'] + ".mjd"
			with open (self.fileName, mode="w") as self.projectFile:
				for key, value in iter(self.projectData.items()):
					self.projectFile.write(key + ',' + value + '\n')
				
		elif self.status == "Archived":
			self.fileName = self.projectData['Project Name'] + ".mjb"
			with open (self.fileName, mode="w") as self.projectFile:
				for key, value in iter(self.projectData.items()):
					self.projectFile.write(key + ',' + value + '\n')

	
	def newLogEntry(self):
		pass
		# displays fields and inputs data

	def editLogEntry(self):
		pass
		# displays log entries in a menu
		# user selects entry
		# data loaded into form for user to edit

	def addGroup(self):
		pass
		# user prompted for:
			# name of strain
			# number to add
			# date (this is a list used to track when changes occur **NOT SURE HOW BEST TO IMPLEMENT**)
			# all other data is the same
		
	def removeGroup(self):
		pass
		# existing groups are shown (call showMenu)
		# user selects group
		# confirmation ("cursor" set to Yes)
		# that group is removed from groups (the list of group objects)

	def addToGroup(self):
		pass
		# existing groups are shown
		# user selects group
		# user prompted for number to add
		# group updated with new number

	def removeFromGroup(self):
		pass
		# existing groups are shown
		# user selects group
		# user prompted for number to remove
		# group updated with new number

	def transplantGroup(self):
		pass
		# existing groups shown, user selects (standard controls)
		# the following fields are shown: (default to current)
			# phase (seedling and clone not shown; sprout, veg, flower)
			# container (puck not shown; cup, pot, rootbag, pail)
			# date (to add to list of dates - how to keep them straight?)




# CLASS lightArray
		
class lightArray:
	def __init__(self):
		# input all data for the light array
		    pass
			# Name
			# Number
			# Type (list: LED, CFL, T5, MH, HPS, Other - usually a bulb used for clones or something)
			# Wattage
			
	def editLight(self):
		pass
		# displays form with data loaded and ready for editing

		
		

class growSpace:
	def __init__(self):
		pass
		# inputs data from user and stores it
			# Name
			# Lights (this is the default light for this grow space)
			# surfaceArea
	
	def editGrowSpace(self):
		pass
		# displays form with data loaded and ready for editing
	
	
	
	
class plantGroup:		# a group is 1 or more of the same strain. each group has its own start date (default is project start date)
	def __init__(self):
		pass
		# input all data for the plantGroup
			# Phase (seedling, clone, sprout, veg, flower, harvested, dead)
			# Number
			# Strain
			# Container
		# need a way to track the changes (against date) 
			
	def editPlantGroup(self):
		pass
		# displays form with data loaded and ready for editing

		
		
