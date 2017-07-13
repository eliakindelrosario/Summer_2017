import json

# ESGF INSTALLER QUESTIONS
QUESTIONS = [
    "Please select the ESGF distribution mirror for this installation",

    "Are you ready to begin the installation?",

    "Please select the IP address to use for this installation",

    "What is the fully qualified domain name of this node?",

    "What is the admin password to use for this installation?",

    "Please re-enter password:",

    "What is the name of your organization?",

    "Please give this node a \"short\" name",

    "Please give this node a more descriptive \"long\" name",

    "What is the namespace to use for this node?",

    "What peer group(s) will this node participate in?",

    "What is the default peer to this node?",

    "What is the hostname of the node do you plan to publish to?",

    "What email address should notifications be sent as?",

    "Is the database external to this node?",

    "What is the database connection string?",

    "Is the database external to this node?",

    "What is the (low priv) db account for publisher?",

    "What is the db password for publisher user",

    "Enter password for postgres user dbsuper:",

    "Re-enter password for postgres user dbsuper:",

    "Please Enter PostgreSQL port number",

    "Would you like a \"system\" or \"user\" publisher configuration",

    "Is this correct?",

    "What is your organization's id?",

    "Do you want to continue with Tomcat installation and setup?",

    "Do you want to continue with esgcet installation and setup?",

    "Do you want to continue with thredds installation and setup?",

    "Do you want to continue with ESGF Dashboard IP installation and setup?",

    "Would you like to use the DN: (OU=ESGF.ORG, O=ESGF)",

    "Please enter the password for this keystore",

    "Please re-enter the password for this keystore",

    "Enter a single ip address which would be cleared to access admin restricted pages.",

    "Do you wish to allow further ips?",

    "Please enter username for tomcat",

    "Please enter password for user, ",

    "Would you like to add another user?",

    "Do you wish to setup the redirect to the esgf-node-manager's page?",

    "(RETURN if same as keystore password)",

    "Do you wish to generate a Certificate Signing Request at this time?",

    "Please Enter the IP address of this host",

    "Please Enter the public (i.e. routable) IP address of this host",

    "Do you wish to use an external IDP peer?",

    "Please specify your IDP peer node's FQDN:",

    "Enter certificate to add to trusted keystore",

    "Do you want to continue with the Globus installation and setup?",

    "Do you want to make a back up of the existing Globus distribution (datanode)?",

    "Do you want to register the GridFTP server with Globus?",

    "Do you want to register the MyProxy server with Globus?",

    "Please provide a Globus username",

    "Globus password",

    "Globus Username:",

    "Globus Password:",

    "Enter password for new role:",

    "Enter it again:",

    "Do you want to continue with openid relying party installation and setup?",

    "Do you want to make a back up of the existing distribution?",

    "Do you want to continue with security services installation and setup?",

    "Do you want to continue with idp services installation and setup?",

    "Do you want to continue with search services installation and setup?",

    "Do you want to continue with security schema setup?",

    "Do you want to make a back up of the existing database schema",

    "Do you still wish to (re)GENERATE self signed certs (and usurp what is present)?"]
# count = 0
# for item in QUESTIONS:
# 	count = count + 1
# 	print str(count) + ':' + item
# 	print "\n"




with open("init.json", "r") as file:
    data = json.load(file)

for x in data["Set"]["node"]:
    print(x["title"])

