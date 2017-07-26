from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import BooleanField, TextField, PasswordField, SelectField
from wtforms.validators import InputRequired, Email, Length
import json

# Initialize app
app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = "Development"

# Questionnair route
# Accepts GET and POST requests
@app.route('/', methods=['GET','POST'])
def questionnaire():
	""" Render template with form fields."""
	# check if data was sent
	if request.method == 'POST':
		# get the data from the form
		result = request.form
		# open json file
		with open('data.json', 'w+') as json_file:
			# write data to json file
			json.dump(result, json_file)
		# return complete  message page after form submition
		return redirect(url_for('complete'))
	else:
		# display questionnaire by default
		with open("static/init.json", "r") as init_data:
			data = json.load(init_data)

		return render_template('questionnaire.html', data=data, text="Hello World")

@app.route('/complete')
def complete():
	""" Render template with complete message."""
	return render_template('complete.html')

@app.route('/json')
def part():
	with open("static/init.json", "r") as init_data:
		data = json.load(init_data)
	return url_for('static', filename='init.josn')

@app.route('/test')
def test():
	return render_template('test.html', name="WORLD")



########## WTF ##################
def getJson():
	with open("static/draft.json", "r") as init_data:
		data = json.load(init_data)
	return data


class Mirror(Form):
	data = getJson()
	print "{}".format(data)
	options = [
		("1","distrib-coffee.ipsl.jussieu.fr/pub/esgf"),
		("2","dist.ceda.ac.uk/esgf"),
		("3","aims1.llnl.gov/esgf"),
		("4","esg-dn2.nsc.liu.se/esgf")]
	distribution_mirror = SelectField(data['Sets']['mirror']['title'], choices=options)

class Node(Mirror):
	email = TextField('Email', validators=[InputRequired(), Email(message="Invalid Email Address")])
	password = PasswordField('Password', [InputRequired(), Length(min=8)])

@app.route('/wt_form', methods=['GET','POST'])
def test_wtform():
	form = Node()
	if form.validate_on_submit():
		return "Finally!!"
	return render_template('wtf_test.html', form=form)

# Run this program if called directly
# if __name__ == "__main__":
# 	app.secret_key = 'secret'
# 	app.run(debug=True)