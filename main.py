from flask import flash, Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import BooleanField, TextField, PasswordField, SelectField, TextAreaField, RadioField
from wtforms.validators import InputRequired, Email, Length
import json

# Initialize app
app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = "Development"

def getJson():
	with open("static/init.json", "r") as init_data:
		data = json.load(init_data)
	return data

# Global list
yes_no = [('','Select'),("yes","Yes"), ("no","No")]

class Mirror(FlaskForm):
	data = getJson() # get questions from json data
	#print "{}".format(data)

	# Mirror options to choose from
	options = [
		("1","distrib-coffee.ipsl.jussieu.fr/pub/esgf"),
		("2","dist.ceda.ac.uk/esgf"),
		("3","aims1.llnl.gov/esgf"),
		("4","esg-dn2.nsc.liu.se/esgf")]

	distribution_mirror = SelectField(data['mirror']['title'], choices=options)

class Node(Mirror):
	""" Creates a form with all node related questions.
	The questions are extracted from the init.json file found in the static folder."""
	data = getJson()
	organization_name = TextField(data['node'][0]['title'], validators=[InputRequired()])
	organization_id = TextField(data['node'][1]['title'], validators=[InputRequired()])
	short_name = TextField(data['node'][2]['title'], validators=[InputRequired()])
	long_name = TextField(data['node'][3]['title'], validators=[InputRequired()])
	namespace = TextField(data['node'][4]['title'], validators=[InputRequired()])
	peer_group = TextField(data['node'][5]['title'], validators=[InputRequired()])
	default_peer_node = TextField(data['node'][6]['title'], validators=[InputRequired()])
	hostname = TextField(data['node'][7]['title'], validators=[InputRequired()])
	ip_address = TextField(data['node'][8]['title'], validators=[InputRequired()])
	qualifie_domain = TextField(data['node'][9]['title'], validators=[InputRequired()])
	email = TextField(data['node'][10]['title'], validators=[InputRequired(), Email(message="Invalid Email Address")])
	password = PasswordField(data['node'][11]['title'], [InputRequired(), Length(min=8)])
	password_confirm = PasswordField(data['node'][12]['title'], [InputRequired(), Length(min=8)])
	complete_with_root_pass = BooleanField("Contniue using root pasword for the rest of the installation?")

class Database(Node):
	""" Creates a form with database related questions.
	The questions are extracted from the init.json file found in the static folder."""
	data = getJson()

	is_external = SelectField(data['database'][0]['title'], choices=yes_no, default='')
	db_con_string = TextField(data['database'][1]['title'], validators=[InputRequired()])
	low_priv_acc = TextField(data['database'][2]['title'], validators=[InputRequired()])
	password_p_usr = PasswordField(data['database'][3]['title'], [InputRequired(), Length(min=8)])
	password_postgress = PasswordField(data['database'][4]['title'], [InputRequired(), Length(min=8)])
	db_port = TextField(data['database'][6]['title'], validators=[InputRequired()])

class Tomcat(Database):
	""" Creates a form with tomcat related questions.
	The questions are extracted from the init.json file found in the static folder."""
	data = getJson()

	install_tomcat = SelectField(data['tomcat'][0]['title'], choices=yes_no, default=1)
	tomcat_usr = TextField(data['tomcat'][1]['title'], validators=[InputRequired()])
	tomcat_password = PasswordField(data['tomcat'][2]['title'], [InputRequired(), Length(min=8)])
	add_more_usrs = TextAreaField(data['tomcat'][3]['title'])
	redirect_to_manager = SelectField(data['tomcat'][4]['title'], choices=yes_no)

class DomainName(Tomcat):
	""" Creates a form with domainname related questions.
	The questions are extracted from the init.json file found in the static folder."""
	data = getJson()

	dn_to_use = TextField(data['domainName'][0]['title'], validators=[InputRequired()])
	keystore_password = PasswordField(data['domainName'][1]['title'], [InputRequired(), Length(min=8)])
	keystore_password_confirm = PasswordField(data['domainName'][2]['title'], [InputRequired(), Length(min=8)])
	cleared_ip = TextField(data['domainName'][3]['title'], validators=[InputRequired()])
	additional_ips = TextAreaField(data['domainName'][4]['title'])

class Globus(DomainName):
	""" Creates a form with globus related questions.
	The questions are extracted from the init.json file found in the static folder."""
	data = getJson()

	install_globus = SelectField(data['globus'][0]['title'], choices=yes_no, default=1)
	backup_globus = SelectField(data['globus'][1]['title'], choices=yes_no)
	register_gridftp = SelectField(data['globus'][2]['title'], choices=yes_no)
	myproxi_gridftp = SelectField(data['globus'][3]['title'], choices=yes_no)
	globus_usr = TextField(data['globus'][4]['title'], validators=[InputRequired()])
	globus_password = PasswordField(data['globus'][5]['title'], [InputRequired(), Length(min=8)])

class Optional_Installations(Globus):
	""" Creates a form with other installations related questions.
	The questions are extracted from the init.json file found in the static folder."""
	data = getJson()

	# options for esgcet - this creates a list of tuples
	options = [(x, x) for x in data['extras'][0]['options']]

	esgcet = SelectField(data['extras'][0]['title'], choices=options)
	thredds = BooleanField(data['extras'][1]['title'])
	dashboard = BooleanField(data['extras'][2]['title'])
	openid = BooleanField(data['extras'][3]['title'])
	openid_bkup = SelectField(data['extras'][4]['title'], choices=yes_no)
	security = BooleanField(data['extras'][5]['title'])
	idp = BooleanField(data['extras'][6]['title'])
	search = BooleanField(data['extras'][7]['title'])
	security_schema = BooleanField(data['extras'][8]['title'])
	security_schema_bkup = SelectField(data['extras'][9]['title'], choices=yes_no)

class Certificate(Optional_Installations):
	""" Creates a form with certificate related questions.
	The questions are extracted from the init.json file found in the static folder."""
	data = getJson()

	gen_certificate = SelectField(data['certificate'][0]['title'], choices=yes_no)
	host_ip = TextField(data['certificate'][1]['title'], validators=[InputRequired()])
	public_ip = TextField(data['certificate'][2]['title'], validators=[InputRequired()])
	use_external_idp = SelectField(data['certificate'][3]['title'], choices=yes_no)
	fqdn = TextField(data['certificate'][4]['title'], validators=[InputRequired()])
	keystore_certificate = TextField(data['certificate'][5]['title'], validators=[InputRequired()])
	regenerate_certificate = SelectField(data['certificate'][6]['title'], choices=yes_no)


@app.route('/', methods=['GET','POST'])
@app.route('/esgfForm', methods=['GET','POST'])
def esfgForm():
	"""
		Display main webpage and handles both get and post request.
		If "GET" request, display form.
		If "POST" request, dump form data into a .json file and render complete.html
	"""

	# Initialize forms
	form = Certificate() # TOFIX: Once you get the installation format, add logic to only render the needed fields 
	print "Form Created"

	if request.method == 'POST':
		# Check for erros
		#print form.errors
		result = request.form
		with open('data.json', 'w+') as json_file:
			json.dump(result, json_file)
		return redirect(url_for('complete'))
	return render_template('esgfForm.html', form=form)


@app.route('/complete')
def complete():
	""" Render template with complete message."""
	return render_template('complete.html')

