
## About Project 
This project is a simple Python-flask web app that captures form data and saves it in into a json file.

## Getting Started 
Before using this application, you will need to install a few dependencies.
It is advised that python, python-pip, and python-virtualenv already exist in your machine. Note that virtualenv is not required.  

Ubuntu Installation: 
$ apt-get install python 

CentOs Installation: 
$ yum install python 

Note: python version 2.7> and 3 will install pip automatically. Earlier versions may not.  

Setting up the application:
For best practice, create a python virtual environment to host the application. This is assuming virtualenv is already in your machine as advised. 

$ cd ~/where/virtualenv/will/be/located
$ virtualenv projectenv

Activate the environment:
Source ~/where/virtualenv/will/be/located/projectenv/bin/activate

Now clone the application inside this virtual environment after installing the dependencies. 
Install Dependencies: $ sudo pip install -r requirements.txt

Now you can run the application:
$ python app.py

In a Browser visit localhost:5000. 

After filling in the forms, a json file should be available in the current directory of the application. 

## Usage
The application uses wtform to create class objects that underline the foundation of the form. Using this method, many forms can be created and rendered easily on templates. For that purpose, this application can be used to create any number of forms to gather information for many purposes. 

## Application Structure
The application follows a simple convention. Once the first view is rendered, the user must fill in the form and submit it for validation. Upon validation, a request will be made to the server to return the next form. Same principles apply here. Once that form is filled in, submitted, and validated another request will be made to render the next view. Once all the needed information is submitted, the server will then save the form data it received into a .json file.

The forms will be rendered in a hierarchal order.  
Mirror Selection 
	-Node Configuration 
		-Tomcat Setup
			-Database Setup
				-Globus Setup
					-Subsystem Selection 
						-Certification 

## Deployment 
To test deploy this application, follow this tutorial here;
Deployment Guide: https://hostpresto.com/community/tutorials/deploy-flask-applications-with-gunicorn-and-nginx-on-ubuntu-14-04/

Note: In the requirements.txt files, gunicorn and virtualenv are being installed. It is advised that virtualenv is installed before running the requirements.txt file. 

## Future Work and Improvements
There are many improvements to be made. Just to name a few:
-	Populating fields automatically,
-	Better Designs of the forms,
-	Session handling for each view,
-	Etc.

For Future works, this application will be integrated into an installer.


