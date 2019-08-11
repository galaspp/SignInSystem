import os
import json
import urllib.request
from flask import render_template, flash, redirect, url_for, request
from werkzeug.utils import secure_filename
from app import app
from app.forms import LoginForm, HomePage, OrderPage, ManufactureForm, ManufacturingProgressPage

users = ''
FINAL_UPLOAD_FOLDER = 'Manufacturing'
MANUFACTURING_UPLOAD_FOLDER = 'Manufacturing/Part'
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = LoginForm()
    global users
    if form.validate_on_submit():
        flash('Login requested for user {}'.format(
            form.username.data))
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
    return render_template('login.html', title='Sign Up', form=form)

@app.route('/index', methods=['GET', 'POST'])
def index():
	form2 = HomePage()
	user = {'username': users}
	if request.method == 'POST':
		return redirect(url_for('signup'))
	return render_template('index.html', title='Home', user=user, form=form2)

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
	return render_template('order.html', title='Order Form', form=form3)
	
@app.route('/manufactureform', methods=['GET', 'POST'])
def manufactureform():
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

			with open(os.path.join(FINAL_UPLOAD_FOLDER, "AllPartInfo.json"), "a+") as e:
				data={}
				dueDate = "%s/%s/%s"%(form4.manufactureMonth.data, form4.manufactureDay.data, form4.manufactureYear.data)
				data['Part']=[]
				data['Part'].append({'name': form4.manufactureFirstName.data, 'subteam': form4.manufactureSubteam.data, 'date': dueDate, 'qty': form4.manufactureQTY.data, 'file': filename, 'status': 'Not Started', 'hours': '0'})
				json.dump(data, e)

			flash('File successfully uploaded')
			return redirect(url_for('manufactureform'))
	return render_template('manufactureform.html', title='Manufacture Part Form', form=form4)

@app.route('/manufacture', methods=['GET', 'POST'])
def manufacturingShowcase():
	form5 = ManufacturingProgressPage()
	return render_template('manufacture.html', title='Manufacture Progress', form=form5)