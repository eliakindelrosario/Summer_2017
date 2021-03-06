
## About Project 
This project is a simple Python-flask web app that captures form data and saves it in into a json file.

## Getting Started 
Before using this application, you will need to install a few dependencies.
It is advised that python, python-pip, and python-virtualenv already exist in your machine. 
###### Note: virtualenv is not required and if you install Python version 2.7> and 3.> will install pip automatically. Earlier versions may not.

#### Setting up the Virtual Environment
For best practice, create a python virtual environment to hold the application. Here I am assuming virtualenv is already on your machine. 

Enter a directory where you want your virtual environment to be and create it.
```
$ cd ~/where/virtualenv/will/be/located
$ virtualenv projectenv
```
Then activate the environment by executing this command:

`source ~/where/virtualenv/will/be/located/projectenv/bin/activate`

You should now be inside the virtual environment. Inside the virtual environment, clone the application and install the dependencies. 
```
$ git clone https://github.com/eliakindelrosario/Summer_2017.git
$ cd Summer_2017
$ sudo pip install -r requirements.txt
```
Finally, run the application

`$ python app.py`

In a Browser visit localhost:5000. After filling in the forms, a json file should be available in the current directory of the application.

## Usage
The application uses wtform to create class objects that underline the foundation of the form. Using this method, many forms can be created and rendered easily on templates. For that purpose, this application can be used to create any number of forms to gather information for many purposes. 

## Application Structure
The application follows a simple convention. Once the first view is rendered, the user must fill in the form and submit it for validation. Upon validation, a request will be made to the server to return the next view. Same principles apply here. Once that form is filled in, submitted, and validated another request will be made to render the next view. Once all the needed information is submitted, the server will then save the form data it received into a .json file.

The forms will be rendered in a hierarchal order.  
1. Mirror Selection
2. Node Configuration 
3. Tomcat Setup
4. Database Setup
5. Globus Setup
6. Subsystem Selection 
7. Certification 

## Deployment 
To test deploy this application, follow this tutorial here;

**Deployment Guide:** https://hostpresto.com/community/tutorials/deploy-flask-applications-with-gunicorn-and-nginx-on-ubuntu-14-04/

###### Note: _In the requirements.txt files, gunicorn and virtualenv are being installed. It is advised that virtualenv is installed before running the requirements.txt file._ However, as previously indicated, virtualenv is not a requirement. 

## Improvements
### **TBA**

## Future Work
- Complete network.py to pre-populate some form fields.
- Integrated application with the ESGF installer.



