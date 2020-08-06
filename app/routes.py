import os
import csv
import urllib.request
from flask import render_template, flash, redirect, url_for, request
from werkzeug.utils import secure_filename
from app import app
from app.forms import LoginForm, HomePage, OrderPage, ManufactureForm, ManufacturingProgressPage, taskForm, taskProgressPage

users = ''
FINAL_UPLOAD_FOLDER = 'Manufacturing'
MANUFACTURING_UPLOAD_FOLDER = 'Manufacturing/Part'
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = LoginForm()
    global users
    if form.validate_on_submit():
        flash('Login requested for user {}'.format(form.username.data))
        users = form.firstName.data
        f = open("UserInfo.txt", "a+")
        f.write("Username: %s \r\n" %(form.username.data))
        f.write("First and Last Name: %s %s \r\n"%(form.firstName.data, form.lastName.data))
        f.write("Interests: Frame:%s Handling:%s Powertrain:%s Electrical:%s \r\n"%(form.frame.data, form.handling.data, form.powertrain.data, form.electrical.data))
        f.write("Major: %s \r\n"%(form.major.data))
        f.write("Year: %s \r\n"%(form.year.data))
        f.write("Experience: %s \r\n"%(form.experience.data))
        f.write("Remeberance: %s \r\n"%form.remeberance.data)
        f.write("\r\n")
        f.close()
        e = open("Email.txt", "a+")
        e.write("%s@rose-hulman.edu, " %(form.username.data))
        e.close()
        return redirect(url_for('index'))
    return render_template('page-renderer.html',body_layout='body1.html',content='login.html', title='Sign Up', form=form, links=get_links())

def has_no_empty_params(rule):
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)

def get_links():
    links = []
    for rule in app.url_map.iter_rules():
        # Filter out rules we can't navigate to in a browser
        # and rules that require parameters
        if "GET" in rule.methods and has_no_empty_params(rule):
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            links.append({'url':url, 'title':rule.endpoint})
    # links is now a list of url, endpoint tuples
    return links

@app.route("/sitemap")
def sitemap():
	links = get_links()
	return render_template('sitemap.html',title='Site Map',links=links)

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
	form2 = HomePage()
	user = {'username': users}
	if request.method == 'POST':
		return redirect(url_for('signup'))
	return render_template('page-renderer.html',body_layout='index.html', title='Home', user=user, form=form2, links=get_links())

@app.route('/order', methods=['GET', 'POST'])
def order():
	form3 = OrderPage()
	if request.method == 'POST' and form3.validate_on_submit():
		f = open("OrderForm.txt", "a+")
		f.write("First and Last Name: %s %s \r\n"%(form3.orderFirstName.data, form3.orderLastName.data))
		f.write("Subteam: %s \r\n"%(form3.subteam.data))
		f.write("QTY: %s  Link: %s \r\n"%(form3.qty.data, form3.link.data))
		f.write("QTY: %s  Link: %s \r\n"%(form3.qty1.data, form3.link1.data))
		f.write("QTY: %s  Link: %s \r\n"%(form3.qty2.data, form3.link2.data))
		f.write("QTY: %s  Link: %s \r\n"%(form3.qty3.data, form3.link3.data))
		f.write("QTY: %s  Link: %s \r\n"%(form3.qty4.data, form3.link4.data))
		f.write("QTY: %s  Link: %s \r\n"%(form3.qty5.data, form3.link5.data))
		f.write("QTY: %s  Link: %s \r\n"%(form3.qty6.data, form3.link6.data))
		f.write("QTY: %s  Link: %s \r\n"%(form3.qty7.data, form3.link7.data))
		f.write("QTY: %s  Link: %s \r\n"%(form3.qty8.data, form3.link8.data))
		f.write("QTY: %s  Link: %s \r\n"%(form3.qty9.data, form3.link9.data))
		f.close()
		e = open("OrderLinks.txt", "a+")
		e.write("QTY: %s  Link: %s \r\n"%(form3.qty.data, form3.link.data))
		e.write("QTY: %s  Link: %s \r\n"%(form3.qty1.data, form3.link1.data))
		e.write("QTY: %s  Link: %s \r\n"%(form3.qty2.data, form3.link2.data))
		e.write("QTY: %s  Link: %s \r\n"%(form3.qty3.data, form3.link3.data))
		e.write("QTY: %s  Link: %s \r\n"%(form3.qty4.data, form3.link4.data))
		e.write("QTY: %s  Link: %s \r\n"%(form3.qty5.data, form3.link5.data))
		e.write("QTY: %s  Link: %s \r\n"%(form3.qty6.data, form3.link6.data))
		e.write("QTY: %s  Link: %s \r\n"%(form3.qty7.data, form3.link7.data))
		e.write("QTY: %s  Link: %s \r\n"%(form3.qty8.data, form3.link8.data))
		e.write("QTY: %s  Link: %s \r\n"%(form3.qty9.data, form3.link9.data))
		e.close()
		return redirect(url_for('order'))
	return render_template('page-renderer.html',body_layout='order.html', title='Order Form', form=form3, links=get_links())
	
@app.route('/manufactureform', methods=['GET', 'POST'])
def manufactureform():
	manufacturearray=[]
	form4 = ManufactureForm()
	if request.method == 'POST' and form4.validate_on_submit():
		if 'file' not in request.files:
			flash('No file part')
			return redirect(url_for('manufactureform'))

		file = request.files['file']

		UPLOAD_FOLDER = MANUFACTURING_UPLOAD_FOLDER + file.filename
		os.makedirs(UPLOAD_FOLDER)
		app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

		if file.filename == '':
			flash('No file selected')
			return redirect(url_for('manufactureform'))
		else:
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

			with open(os.path.join(UPLOAD_FOLDER,"PartInfo.txt"), "a+") as f:
				f.write("First and Last Name: %s %s \r\n"%(form4.manufactureFirstName.data, form4.manufactureLastName.data))
				f.write("Subteam: %s \r\n"%(form4.manufactureSubteam.data))
				f.write("Due Date: %s/%s/%s \r\n"%(form4.manufactureMonth.data, form4.manufactureDay.data, form4.manufactureYear.data))
				f.write("QTY: %s \r\n"%(form4.manufactureQTY.data))
				f.close()

			if not os.path.exists('Manufacturing/AllPartInfo.txt'):
				with open(os.path.join(FINAL_UPLOAD_FOLDER, "AllPartInfo.txt"), "a+") as d:
					d.write("name,subteam,date,qty,file,progress\r\n")
					d.close()
			if os.path.exists('Manufacturing/AllPartInfo.txt'):
				with open('Manufacturing/AllPartInfo.txt', 'r') as e:
					data = csv.reader(e, delimiter=',')
					lineCount = 0
					for p in data:
						if lineCount == 0:
							lineCount+=1
						else:
							manufacturearray.append(p[4])
							lineCount+=1

				if filename in manufacturearray:
					newManufactureName = filename
					count = 1
					while newManufactureName in manufacturearray:
						newManufactureName = filename + str(count)
						count+=1

					with open(os.path.join(FINAL_UPLOAD_FOLDER, "AllPartInfo.txt"), "a+") as e:
						dueDate = "%s/%s/%s"%(form4.manufactureMonth.data, form4.manufactureDay.data, form4.manufactureYear.data)
						e.write("%s,%s,%s,%s,%s,Not Started\r\n"%(form4.manufactureFirstName.data, form4.manufactureSubteam.data, dueDate,form4.manufactureQTY.data, newManufactureName))
						e.close()
				else:
					with open(os.path.join(FINAL_UPLOAD_FOLDER, "AllPartInfo.txt"), "a+") as e:
						dueDate = "%s/%s/%s"%(form4.manufactureMonth.data, form4.manufactureDay.data, form4.manufactureYear.data)
						e.write("%s,%s,%s,%s,%s,Not Started\r\n"%(form4.manufactureFirstName.data, form4.manufactureSubteam.data, dueDate,form4.manufactureQTY.data, filename))
						e.close()

			flash('File successfully uploaded')
			return redirect(url_for('manufacturingShowcase'))
	return render_template('page-renderer.html',body_layout='manufactureform.html', title='Manufacture Part Form', form=form4, links=get_links())

@app.route('/manufacture', methods=['GET', 'POST'])
def manufacturingShowcase():
	form5 = ManufacturingProgressPage()
	if request.method == 'GET':
		form5.updateForm()
	if form5.redirectToForm.data:
		return redirect(url_for('manufactureform'))
	if request.method == 'POST' and form5.validate_on_submit() and form5.submitChange.data:
		form5.updateProgress(form5.remainingTasks.data, form5.progressOnTask.data)
		form5.updateForm()
		return redirect(url_for('manufacturingShowcase'))
	return render_template('page-renderer.html',body_layout='manufacture.html', title='Manufacture Progress', form=form5, len=len(form5.manufacturingName), links=get_links())

@app.route('/taskform', methods=['GET', 'POST'])
def taskform():
	taskarray=[]
	form6 = taskForm()
	if request.method == 'POST' and form6.validate_on_submit():
		with open("taskInfo.txt", "a+") as f:
			f.write("Task Name: %s \r\n"%(form6.taskName.data))
			f.write("First and Last Name: %s %s \r\n"%(form6.taskFirstName.data, form6.taskLastName.data))
			f.write("Assigned To: %s \r\n"%(form6.assignTo.data))
			f.write("Subteam: %s \r\n"%(form6.taskSubteam.data))
			f.write("Due Date: %s/%s/%s \r\n"%(form6.taskMonth.data, form6.taskDay.data, form6.taskDay.data))
			f.write("Task Description: %s \r\n"%(form6.taskDescription.data))
			f.close()

		if not os.path.exists('AllTaskInfo.txt'):
			with open("AllTaskInfo.txt", "a+") as d:
				d.write("name,taskname,assign,subteam,date,description,hours,progress\r\n")
				d.close()

		if os.path.exists('AllTaskInfo.txt'):
			with open('AllTaskInfo.txt', 'r') as e:
				data = csv.reader(e, delimiter=',')
				lineCount = 0
				for p in data:
					if lineCount == 0:
						lineCount+=1
					else:
						taskarray.append(p[0])
						lineCount+=1

			if form6.taskName.data in taskarray:
				newTaskName = form6.taskName.data
				count = 1
				while newTaskName in taskarray:
					newTaskName = form6.taskName.data + str(count)
					count+=1
				with open("AllTaskInfo.txt", "a+") as e:
					dueDate = "%s/%s/%s"%(form6.taskMonth.data,form6.taskDay.data, form6.taskDay.data)
					e.write("%s,%s,%s,%s,%s,%s,0,Not Started\r\n"%(newTaskName,form6.taskFirstName.data, form6.assignTo.data, form6.taskSubteam.data, dueDate, form6.taskDescription.data))
					e.close()
			else:
				with open("AllTaskInfo.txt", "a+") as e:
					dueDate = "%s/%s/%s"%(form6.taskMonth.data,form6.taskDay.data, form6.taskDay.data)
					e.write("%s,%s,%s,%s,%s,%s,0,Not Started\r\n"%(form6.taskName.data,form6.taskFirstName.data, form6.assignTo.data, form6.taskSubteam.data, dueDate, form6.taskDescription.data))
					e.close()

		return redirect(url_for('taskShowcase'))
	return render_template('page-renderer.html',body_layout='taskform.html', title='Task Form', form=form6, links=get_links())

@app.route('/task', methods=['GET', 'POST'])
def taskShowcase():
	form = taskProgressPage()
	if request.method == 'GET':
		form.updateForm()
	if form.redirectToForm.data:
		return redirect(url_for('taskform'))
	if request.method == 'POST' and form.validate_on_submit() and form.submitChange.data:
		form.updateProgress(form.remainingTasks.data, form.progressOnTask.data, form.hoursWorked.data)
		form.updateForm()
		return redirect(url_for('taskShowcase'))
	return render_template('page-renderer.html',body_layout='task.html', title='Task Progress', form=form, len=len(form.taskName), links=get_links())



if __name__ == '__main__':
	app.run(host="0.0.0.0", port=8000, debug=True)
	CACHE_TIME=0
else:
	app.run(host="0.0.0.0", port=8000, debug=True)
	CACHE_TIME=0