import os
import json
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired

allMajors = [('NA', 'N/A'), ('ME', 'Mechanical Engineering'), ('EE', 'Electrical Engineering'), ('CPE', 'Computer Engineering'), ('CS', 'Computer Science'), ('SW', 'Software Engineering'), ('Other', 'Other')]
allYears = [('F', 'Freshman'), ('S', 'Sophomore'), ('J', 'Junior'), ('SN', 'Senior'), ('G', 'Graduate'), ('A', 'Alum')]
allSubteams = [('NA', 'N/A'), ('Aero', 'Aero'), ('Chassis', 'Chassis'), ('Cooling', 'Cooling'), ('Drivetrain', 'Drivetrain'), ('Electrical','Electrical'), ('Engine', 'Engine'), ('Suspension', 'Suspension'), ('Unsprung', 'Unsprung')]
progress = (['NotStarted', 'Not Started'], ['InProgress', 'In Progress'], ['Completed', 'Completed'])

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
	with open('Manufacturing/AllPartInfo.json') as e:
		data = json.loads(e.read())
		for p in data['Part']:
			manufacturingName.append(p['name'])
			manufacturingSubteam.append(p['subteam'])
			manufacturingDate.append(p['date'])
			manufacturingQty.append(p['qty'])
			manufacturingFile.append(p['file'])
			manufacturingStatus.append(p['status'])

	allNotCompletedTasks = []
	for (status,file) in zip(manufacturingStatus, manufacturingFile):
		if status != "Complete":
			allNotCompletedTasks.append(file)

	remainingTasks = SelectField('Tasks', choices=allNotCompletedTasks, validators=[DataRequired()])
	progressOnTask = SelectField('Progress', choices=progress, validators=[DataRequired()])
	submitChange = SubmitField('Submit Change')

	def updateForm(self):
		self.manufacturingName.clear()
		self.manufacturingSubteam.clear()
		self.manufacturingDate.clear()
		self.manufacturingQty.clear()
		self.manufacturingFile.clear()
		self.manufacturingStatus.clear()
		self.allNotCompletedTasks.clear()
		with open('Manufacturing/AllPartInfo.json') as e:
			data = json.loads(e.read())
			for p in data['Part']:
				self.manufacturingName.append(p['name'])
				self.manufacturingSubteam.append(p['subteam'])
				self.manufacturingDate.append(p['date'])
				self.manufacturingQty.append(p['qty'])
				self.manufacturingFile.append(p['file'])
				self.manufacturingStatus.append(p['status'])

		for (status,file) in zip(self.manufacturingStatus, self.manufacturingFile):
			if status != "Complete":
				self.allNotCompletedTasks.append(file)

