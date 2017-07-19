from flask import Flask, render_template, request, redirect, url_for
import json

# Initialize app
app = Flask(__name__)

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
		with open("init.json", "r") as init_data:
			data = json.load(init_data)
			
		return render_template('questionnaire.html', data=data, text="Hello World")

@app.route('/complete')
def complete():
	""" Render template with complete message."""
	return render_template('complete.html')

@app.route('/test')
def test():
	return render_template('test.html')

# Run this program if called directly
if __name__ == "__main__":
	app.secret_key = 'secret'
	app.run(debug=True)
