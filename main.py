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
	data = getJson() # get questions from json data
	#print "{}".format(data)

	# Mirror options to choose from
	options = [
		("1","distrib-coffee.ipsl.jussieu.fr/pub/esgf"),
		("2","dist.ceda.ac.uk/esgf"),
		("3","aims1.llnl.gov/esgf"),
		("4","esg-dn2.nsc.liu.se/esgf")]

	# TODO - Dynamically create a list of tuples.
	# test = [(data['mirror']['options'], x) for x in data['mirror']['options']]
	# print "BIG HALT!!! {}".format(test)

	distribution_mirror = SelectField(data['mirror']['title'], choices=options)

class Node(Mirror):
	""" Creates a form with all node related questions.
	The questions are extracted from the init.json file found in the static folder."""
	data = getJson()

	organization_name = TextField(data['node'][0]['title'], validators=[InputRequired()])
	short_name = TextField(data['node'][1]['title'], validators=[InputRequired()])
	long_name = TextField(data['node'][2]['title'], validators=[InputRequired()])
	namespace = TextField(data['node'][3]['title'], validators=[InputRequired()])
	peer_group = TextField(data['node'][4]['title'], validators=[InputRequired()])
	default_peer_node = TextField(data['node'][5]['title'], validators=[InputRequired()])
	hostname = TextField(data['node'][6]['title'], validators=[InputRequired()])
	ip_address = TextField(data['node'][7]['title'], validators=[InputRequired()])
	qualifie_domain = TextField(data['node'][8]['title'], validators=[InputRequired()])
	email = TextField(data['node'][9]['title'], validators=[InputRequired(), Email(message="Invalid Email Address")])
	password = PasswordField(data['node'][10]['title'], [InputRequired(), Length(min=8)])
	use_root_pass = BooleanField('Use this password for the rest of the configuration?')

class Database(Form):
	""" Creates a form with database related questions.
	The questions are extracted from the init.json file found in the static folder."""
	pass

class Tomcat(Form):
	""" Creates a form with tomcat related questions.
	The questions are extracted from the init.json file found in the static folder."""
	data = getJson()

	organization_name = TextField(data['node'][0]['title'], validators=[InputRequired()])

class Globus(Form):
	""" Creates a form with globus related questions.
	The questions are extracted from the init.json file found in the static folder."""
	pass

class Certificate(Form):
	""" Creates a form with certificate related questions.
	The questions are extracted from the init.json file found in the static folder."""
	pass

class DomainName(Form):
	""" Creates a form with domainname related questions.
	The questions are extracted from the init.json file found in the static folder."""
	pass

class Optional_Installations(Form):
	""" Creates a form with other installations related questions.
	The questions are extracted from the init.json file found in the static folder."""
	pass


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