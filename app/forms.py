from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired

allMajors = [('NA', 'N/A'), ('ME', 'Mechanical Engineering'), ('EE', 'Electrical Engineering'), ('CPE', 'Computer Engineering'), ('CS', 'Computer Science'), ('SW', 'Software Engineering'), ('Other', 'Other')]
allYears = [('F', 'Freshman'), ('S', 'Sophomore'), ('J', 'Junior'), ('SN', 'Senior'), ('G', 'Graduate'), ('A', 'Alum')]
allSubteams = [('NA', 'N/A'), ('aero', 'Aero'), ('chass', 'Chassis'), ('cool', 'Cooling'), ('drive', 'Drivetrain'), ('ele','Electrical'), ('engine', 'Engine'), ('susp', 'Suspension'), ('unspr', 'Unsprung')]
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