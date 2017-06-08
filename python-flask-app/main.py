from flask import Flask, render_template, request
import json 

# Initialize app
app = Flask(__name__)

# Home route 
@app.route('/')
def index():
	return render_template('index.html')

# About route
@app.route('/about')
def about():
	return render_template('about.html')

# Questionnair route
# Accepts GET and POST requests
@app.route('/questionnair', methods=['GET','POST'])
def questionnair():
	return render_template('questionnair.html')

# Run this program if called directly
if __name__ == "__main__":
	app.secret_key = 'secret'
	app.run(debug=True)
	