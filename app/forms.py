import os
import csv
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired

allMajors = [('NA', 'N/A'), ('ME', 'Mechanical Engineering'), ('EE', 'Electrical Engineering'), ('CPE', 'Computer Engineering'), ('CS', 'Computer Science'), ('SW', 'Software Engineering'), ('Other', 'Other')]
allYears = [('F', 'Freshman'), ('S', 'Sophomore'), ('J', 'Junior'), ('SN', 'Senior'), ('G', 'Graduate'), ('A', 'Alum')]
allSubteams = [('NA', 'N/A'), ('Aero', 'Aero'), ('Chassis', 'Chassis'), ('Cooling', 'Cooling'), ('Drivetrain', 'Drivetrain'), ('Electrical','Electrical'), ('Engine', 'Engine'), ('Suspension', 'Suspension'), ('Unsprung', 'Unsprung')]
progress = (['Not Started', 'Not Started'], ['In Progress', 'In Progress'], ['Completed', 'Completed'])

FINAL_UPLOAD_FOLDER = 'Manufacturing'

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    firstName = StringField('First Name', validators=[DataRequired()])
    lastName = StringField('Last Name', validators=[DataRequired()])
    
    frame = BooleanField('Frame and Body')
    handling = BooleanField('Handling')
    powertrain = BooleanField('Powertrain')
    electrical = BooleanField('Electrical')

    major = SelectField('Majors', choices=allMajors, default='NA')
    year = SelectField('Year', choices=allYears, default='F')

    experience = TextAreaField("Past Experiences")
    remeberance = TextAreaField("Something to Remember You By")

    submit = SubmitField('Sign In')

class HomePage(FlaskForm):
	sumbitReload = SubmitField('Go To Sign Up', validators=[DataRequired()])

class OrderPage(FlaskForm):
	orderFirstName = StringField('First Name', validators=[DataRequired()])
	orderLastName = StringField('Last Name', validators=[DataRequired()])

	subteam = SelectField('Subteam', choices=allSubteams, validators=[DataRequired()])

	qty = StringField('QTY')
	link = StringField('Link')

	qty1 = StringField('QTY')
	link1 = StringField('Link')

	qty2 = StringField('QTY')
	link2 = StringField('Link')

	qty3 = StringField('QTY')
	link3 = StringField('Link')

	qty3 = StringField('QTY')
	link3 = StringField('Link')

	qty3 = StringField('QTY')
	link3 = StringField('Link')

	qty4 = StringField('QTY')
	link4 = StringField('Link')

	qty5 = StringField('QTY')
	link5 = StringField('Link')

	qty6 = StringField('QTY')
	link6 = StringField('Link')

	qty7 = StringField('QTY')
	link7 = StringField('Link')

	qty8 = StringField('QTY')
	link8 = StringField('Link')

	qty9 = StringField('QTY')
	link9 = StringField('Link')

	submitOrder = SubmitField('Submit Order')

class ManufactureForm(FlaskForm):
	manufactureFirstName = StringField('First Name', validators=[DataRequired()])
	manufactureLastName = StringField('Last Name', validators=[DataRequired()])

	manufactureSubteam = SelectField('Subteam', choices=allSubteams, validators=[DataRequired()])

	manufactureMonth = StringField('Month')
	manufactureDay = StringField('Day')
	manufactureYear = StringField('Year')

	manufactureQTY = StringField('QTY')

	submitPart = SubmitField('Submit Part')

class ManufacturingProgressPage(FlaskForm):
	manufacturingName = []
	manufacturingSubteam = []
	manufacturingDate = []
	manufacturingQty = []
	manufacturingFile = []
	manufacturingStatus = []
	if os.path.exists('Manufacturing/AllPartInfo.txt'):
		with open('Manufacturing/AllPartInfo.txt', 'r') as e:
			data = csv.reader(e, delimiter=',')
			lineCount = 0
			for p in data:
				if lineCount == 0:
					lineCount+=1
				else:
					manufacturingName.append(p[0])
					manufacturingSubteam.append(p[1])
					manufacturingDate.append(p[2])
					manufacturingQty.append(p[3])
					manufacturingFile.append(p[4])
					manufacturingStatus.append(p[5])
					lineCount+=1

	allNotCompletedTasks = []
	for (status,file) in zip(manufacturingStatus, manufacturingFile):
		if status != "Completed":
			allNotCompletedTasks.append([file,file])

	remainingTasks = SelectField('Tasks', choices=allNotCompletedTasks, validators=[DataRequired()])
	progressOnTask = SelectField('Progress', choices=progress, validators=[DataRequired()])
	redirectToForm = SubmitField('Create Part Request')
	submitChange = SubmitField('Submit Change')

	def updateForm(self):
		self.manufacturingName.clear()
		self.manufacturingSubteam.clear()
		self.manufacturingDate.clear()
		self.manufacturingQty.clear()
		self.manufacturingFile.clear()
		self.manufacturingStatus.clear()
		self.allNotCompletedTasks.clear()
		if os.path.exists('Manufacturing/AllPartInfo.txt'):
			with open('Manufacturing/AllPartInfo.txt', 'r') as e:
				data = csv.reader(e, delimiter=',')
				lineCount = 0
				for p in data:
					if lineCount == 0:
						lineCount+=1
					else:
						self.manufacturingName.append(p[0])
						self.manufacturingSubteam.append(p[1])
						self.manufacturingDate.append(p[2])
						self.manufacturingQty.append(p[3])
						self.manufacturingFile.append(p[4])
						self.manufacturingStatus.append(p[5])
						lineCount+=1

		for (status,file) in zip(self.manufacturingStatus, self.manufacturingFile):
			if status != 'Completed':
				self.allNotCompletedTasks.append([file, file])


	def updateProgress(self, submitFile, updatedProgress):
		lineCount = 1
		for files in self.manufacturingFile:
			if files == submitFile:
				break
			else:
				lineCount+=1
		if os.path.exists('Manufacturing/AllPartInfo.txt'):
			file = csv.reader(open('Manufacturing/AllPartInfo.txt'))
			lines = list(file)
			lines[lineCount][5] = updatedProgress

			writer = csv.writer(open('Manufacturing/AllPartInfo.txt', 'w'))
			writer.writerows(lines)

class taskForm(FlaskForm):
	taskName = StringField('Task Name', validators=[DataRequired()])
	taskFirstName = StringField('First Name', validators=[DataRequired()])
	taskLastName = StringField('Last Name', validators=[DataRequired()])
	assignTo = StringField('Assign To', validators=[DataRequired()])

	taskSubteam = SelectField('Subteam', choices=allSubteams, validators=[DataRequired()])

	taskMonth = StringField('Month')
	taskDay = StringField('Day')
	taskYear = StringField('Year')

	taskDescription = TextAreaField("Task Description")

	submitTask = SubmitField('Submit Task')

class taskProgressPage(FlaskForm):
	taskName = []
	taskFirstName = []
	taskSubteam = []
	taskDate = []
	assigned = []
	taskHours = []
	taskStatus = []
	if os.path.exists('AllTaskInfo.txt'):
		with open('AllTaskInfo.txt', 'r') as e:
			data = csv.reader(e, delimiter=',')
			lineCount = 0
			for p in data:
				if lineCount == 0:
					lineCount+=1
				else:
					taskName.append(p[0])
					taskFirstName.append(p[1])
					assigned.append(p[2])
					taskSubteam.append(p[3])
					taskDate.append(p[4])
					taskHours.append(p[6])
					taskStatus.append(p[7])
					lineCount+=1

	allNotCompletedTasks = []
	for (status,task) in zip(taskStatus, taskName):
		if status != "Completed":
			allNotCompletedTasks.append([task,task])

	remainingTasks = SelectField('Tasks', choices=allNotCompletedTasks, validators=[DataRequired()])
	progressOnTask = SelectField('Progress', choices=progress, validators=[DataRequired()])
	hoursWorked = StringField('hoursWorked', validators=[DataRequired()])
	redirectToForm = SubmitField('Create Task')
	submitChange = SubmitField('Submit Change')

	def updateForm(self):
		self.taskName.clear()
		self.taskFirstName.clear()
		self.taskSubteam.clear()
		self.taskDate.clear()
		self.assigned.clear()
		self.taskHours.clear()
		self.taskStatus.clear()
		self.allNotCompletedTasks.clear()
		if os.path.exists('AllTaskInfo.txt'):
			with open('AllTaskInfo.txt', 'r') as e:
				data = csv.reader(e, delimiter=',')
				lineCount = 0
				for p in data:
					if lineCount == 0:
						lineCount+=1
					else:
						self.taskName.append(p[0])
						self.taskFirstName.append(p[1])
						self.taskSubteam.append(p[3])
						self.assigned.append(p[2])
						self.taskDate.append(p[4])
						self.taskHours.append(p[6])
						self.taskStatus.append(p[7])
						lineCount+=1

		for (status,task) in zip(self.taskStatus, self.taskName):
			if status != 'Completed':
				self.allNotCompletedTasks.append([task, task])


	def updateProgress(self, submitTask, updatedProgress, updatedHours):
		lineCount = 1
		for tasks in self.taskName:
			if tasks == submitTask:
				break
			else:
				lineCount+=1
		if os.path.exists('AllTaskInfo.txt'):
			file = csv.reader(open('AllTaskInfo.txt'))
			lines = list(file)
			lines[lineCount][6] = int(lines[lineCount][6]) + int(updatedHours)
			lines[lineCount][7] = updatedProgress

			writer = csv.writer(open('AllTaskInfo.txt', 'w'))
			writer.writerows(lines)
