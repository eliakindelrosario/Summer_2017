from flask import Flask, render_template, request, redirect, url_for, flash, session
from wtforms import Form, StringField , SelectField, BooleanField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps
import json


app = Flask(__name__) # Initialize flask app
app.config['SECRET_KEY'] = "Development" # Set secrete key for form security

# Essentials 
with open("static/init.json", "r") as init_data:
		data = json.load(init_data) # open file with all the questions
yes_no = [('','Select'),("yes","Yes"), ("no","No")]# yes or no option list

def save_formdata(form):
	""" Check for post request and from validation.
		- open json file and append new data 
	"""
	if request.method == "POST" and form.validate():
		result = request.form # get form data
		app.logger.info("Form data: {}".format(result))

		# open json file 
		with open('data.json') as json_file:
			data = json.load(json_file)

		# convert data so it can be dumped in json file
		data.update(result)

		# open json file in write mode
		with open('data.json', 'w') as json_file:
			json.dump(data,json_file, indent=4, sort_keys=True) # write form data to json file
			app.logger.info("updated file!")

		return 'success'

############## FORMS ####################
class Mirror(Form):
	""" Create form that requests distribution mirror information. """
	options = [(x, x) for x in data['mirror'][0]['options']] # Mirror options to choose from
	distribution_mirror = SelectField(data['mirror'][0]['title'], [validators.data_required()], choices=options)

class Node(Form):
	""" Create form that requests node information."""
	organization_name = StringField(data['node'][0]['title'], [validators.data_required()])
	organization_id = StringField(data['node'][1]['title'], [validators.data_required()])
	short_name = StringField(data['node'][2]['title'], [validators.data_required()])
	long_name = StringField(data['node'][3]['title'], [validators.data_required()])
	namespace = StringField(data['node'][4]['title'], [validators.data_required()])
	peer_group = StringField(data['node'][5]['title'], [validators.data_required()])
	default_peer_node = StringField(data['node'][6]['title'], [validators.data_required()])
	hostname = StringField(data['node'][7]['title'], [validators.data_required()])
	ip_address = StringField(data['node'][8]['title'], [validators.data_required()])
	qualifie_domain = StringField(data['node'][9]['title'], [validators.data_required()])
	email = StringField(data['node'][10]['title'], [validators.data_required(), validators.Email('Invalid Email Address')])
	password = PasswordField(data['node'][11]['title'],  [
		validators.data_required(), 
		validators.EqualTo('password_confirm', message="Password do not match")
		])
	password_confirm = PasswordField(data['node'][12]['title'], [validators.data_required(), validators.Length(min=5)])
	#root_complete = SelectField("Contniue using root pasword for the rest of the installation?",choices=yes_no)
class Database(Form):
	""" Create form that requests database information"""
	is_external = SelectField(data['database'][0]['title'], choices=yes_no)
	db_con_string = StringField(data['database'][1]['title'])
	low_priv_acc = StringField(data['database'][2]['title'])
	db_port = StringField(data['database'][6]['title'])
	password_postgress = PasswordField(data['database'][3]['title'], [
		validators.data_required(), 
		validators.EqualTo('password_postgress_confirm', message="Password do not match")
		])
	password_postgress_confirm = PasswordField(data['database'][4]['title'], [validators.data_required()])
	

class Tomcat(Form):
	""" Create form that requests tomcat information """
	install_tomcat = SelectField(data['tomcat'][0]['title'], choices=yes_no)
	tomcat_usr = StringField(data['tomcat'][1]['title'])
	tomcat_password = PasswordField(data['tomcat'][2]['title'], [
		validators.data_required(), 
		validators.EqualTo('confirm_tomcat_password', message="Password do not match")
		])
	confirm_tomcat_password = PasswordField('Confirm Password', [validators.data_required()])
	redirect_to_manager = SelectField(data['tomcat'][4]['title'], choices=yes_no)

class DistinguishedName(Form):
	""" Create form that requests for distinguished name information."""
	dn_to_use = StringField(data['domainName'][0]['title'])
	keystore_password = PasswordField(data['domainName'][1]['title'], [
		validators.data_required(), 
		validators.EqualTo('keystore_password_confirm', message="Password do not match")
		])
	keystore_password_confirm = PasswordField(data['domainName'][2]['title'], [validators.data_required()])
	cleared_ip = StringField(data['domainName'][3]['title'])

class Globus(Form):
	""" Creates form that requests globus information."""
	install_globus = SelectField(data['globus'][0]['title'], choices=yes_no, default=1)
	backup_globus = SelectField(data['globus'][1]['title'], choices=yes_no)
	register_gridftp = SelectField(data['globus'][2]['title'], choices=yes_no)
	myproxi_gridftp = SelectField(data['globus'][3]['title'], choices=yes_no)
	globus_usr = StringField(data['globus'][4]['title'], [validators.data_required()])
	globus_password = PasswordField(data['globus'][5]['title'], [
		validators.data_required(), 
		validators.EqualTo('confirm_globus_password', message="Password do not match")
		])
	confirm_globus_password = PasswordField("Confirm Password", [validators.data_required()])

class ESGCET(Form):
	""" Create form that request for additional install informations."""

	# options for esgcet - create a list of tuples
	options = [(x, x) for x in data['extras'][0]['options']]
	options.insert(0,('','Select'))

	esgcet = SelectField(data['extras'][0]['title'], choices=options)
	thredds = SelectField(data['extras'][1]['title'],choices=yes_no)
	dashboard = SelectField(data['extras'][2]['title'],choices=yes_no)
	openid = SelectField(data['extras'][3]['title'],choices=yes_no)
	openid_bkup = SelectField(data['extras'][4]['title'], choices=yes_no)
	security = SelectField(data['extras'][5]['title'],choices=yes_no)
	idp = SelectField(data['extras'][6]['title'],choices=yes_no)
	search = SelectField(data['extras'][7]['title'],choices=yes_no)
	security_schema = SelectField(data['extras'][8]['title'],choices=yes_no)
	security_schema_bkup = SelectField(data['extras'][9]['title'], choices=yes_no)

class Certificate(Form):
	""" Creates form that request for certificate rendering."""
	gen_certificate = SelectField(data['certificate'][0]['title'], choices=yes_no)
	host_ip = StringField(data['certificate'][1]['title'])
	public_ip = StringField(data['certificate'][2]['title'])
	use_external_idp = SelectField(data['certificate'][3]['title'], choices=yes_no)
	fqdn = StringField(data['certificate'][4]['title'])
	keystore_certificate = StringField(data['certificate'][5]['title'])
	regenerate_certificate = SelectField(data['certificate'][6]['title'], choices=yes_no)



############# Security Features ######################
def is_authorized(f):
	# Prevent unauthorized entry to a form.
	@wraps(f)
	def wrap(*args, **kwargs):
		passed = ['authorized_node','authorized_db','authorized_tomcat','authorized_dn','authorized_globus','authorized_esgcet','authorized_cert']
		for x in passed:
			if x in session:
				return f(*args, **kwargs)
			else:
				flash("Unathorized Access", "danger")
				return redirect(url_for('select_mirror'))
	return wrap

	
################# ROUTES ####################
# - FIX: attach a session to everypage
# ESGF Mirror
@app.route('/', methods=['GET','POST'])
def select_mirror():
	# Create form 
	form = Mirror(request.form)
	# check if the request is post and the form is validated
	if request.method == "POST" and form.validate():
		result = request.form # get form data
		# create json file
		with open('data.json', 'w+') as json_file:
			json.dump(result, json_file) # write to json file
		session['authorized_node'] = True
		return redirect(url_for('node_setup'))

	return render_template('mirror.html', form=form)

# ESGF Node
@app.route('/node', methods=['GET','POST'])
@is_authorized
def node_setup():
	# Create form 
	form = Node(request.form)
	if save_formdata(form) != 'success':
		return render_template('node.html', form=form)
	else:
		return redirect(url_for('database_setup'))

#ESGF Database
@app.route('/database',methods=['GET','POST'])
@is_authorized
def database_setup():
	form = Database(request.form)
	if save_formdata(form) != 'success':
		return render_template('database.html', form=form)
	else:
		return redirect(url_for('tomcat_setup'))

#ESGF Tomcat
@app.route('/tomcat',methods=['GET','POST'])
@is_authorized
def tomcat_setup():
	form = Tomcat(request.form)
	if save_formdata(form) != 'success':
		return render_template('tomcat.html', form=form)
	else:
		return redirect(url_for('dn_setup'))

#ESGF Distinguished Name
@app.route('/disname',methods=['GET','POST'])
@is_authorized
def dn_setup():
	form = DistinguishedName(request.form)
	if save_formdata(form) != 'success':
		return render_template('disname.html', form=form)
	else:
		return redirect(url_for('globus_setup'))

#ESGF Globus
@app.route('/globus_setup',methods=['GET','POST'])
@is_authorized
def globus_setup():
	form = Globus(request.form)
	if save_formdata(form) != 'success':
		return render_template('globus.html', form=form)
	else:
		return redirect(url_for('esgcet_setup'))

# ESGCET
@app.route('/esgcet',methods=['GET','POST'])
@is_authorized
def esgcet_setup():
	form = ESGCET(request.form)
	if save_formdata(form) != 'success':
		return render_template('esgcet.html', form=form)
	else:
		return redirect(url_for('certificate_setup'))

# Certificate
@app.route('/certificate',methods=['GET','POST'])
@is_authorized
def certificate_setup():
	form = Certificate(request.form)
	if save_formdata(form) != 'success':
		return render_template('certificate.html', form=form)
	else:
		session.clear()
		return render_template('complete.html')

# FIX - Remove reference to _message in base.html and delet the file from includes 
if __name__ == "__main__":
	app.run(debug=True)