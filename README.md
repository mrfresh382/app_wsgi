# Linux Server Turn-up/Config Project
Submitted by Doug McDonald for Udacity Full Stack Nanodegree.
This is a website for a fictional general store at the Big Bend National Park hosted on AWS Lightsail. 

## VM Specs
- Lightsail - Ubuntu 18.08
- DNS - using GoDaddy.com
- OAuth provided by Google API Console
- HTTPS provided by 'Let's Encrypt'

## Getting Started
### Prerequisites 
A Google account and GitHub account are required for the user to have full permissionson the webpage. The grader must login to the server from SSH or PuTTY.

### 
 for further troubleshooting. 
 
### User Guide for Udacity Grader and General Public

1. Use shell and cd to the vagrant directory 
2. Open VM- `vagrant up`
3. SSH into VM- `vagrant ssh`
4. Once SSHed into VM type `cd /vagrant`
5. From this folder you can run the project files, Static, and Template folder. Check to ensure they are accessible by executing `ls` command. If they are not viewable, check that you are in the '/vagrant' folder, then proceed with troubleshooting. 
6. Execute python file within VM `python catalogDB_setup.py`. This will establish a blank SQLite database using SQLAlchemy for the web app. 
7. Execute `python catalogDBpreLOAD.py` . This will add some info in the database for testing and viewing in the webpage. 
8. Execute `python catalog-app.py` This will start the web app on port 8000 on your local machine. Visit http://localhost:8000 on either Firefox or Chrome to view the home page. Some output messages are visible on the shell. To close App, enter 'CTRL-C' on the keyboard to terminate.

## Notes/Issues/Bugs
- Links to HTTP had to be changed to HTTPS within the HTML templates
- Full path for client_secrets.json had to be added to the python file
- catalog_app.py showCatagorys() function had to be updated to properly display preview items while browsing mainpage. Upon conversion to PostGreSQL, the lists had to be converted to dictionaries to properly display items and prevent fatal errors. 
- I accidently configured UFW with command "sudo ufw default deny outgoing" instead of "sudo ufw default allow outgoing" , this still permitted SSH into the VM, but I could not update packages or install new packages. 

## Design Notes
### Hello World and First Steps
I started this project by baseline configuring the server and creating a "Hello World" WSGI app. 

`if __name__ == '__main__':` section had to be updated to convert to WSGI to run with Apache Web Server. I did not setup a WSGI-APP daemon or create an '_init_.py' file as other students alluded to using. I was able to avoid these 2 steps and the app works just fine.

### Pulled WebServer App files from GitHub
I had to create a new GitHub repo due to the previous project getting corrupt. The web server files are in /var/www/app_wsgi. The shebang line, absolute paths, and other bugs were debugged here.

### Setup DNS
I have domain thedoug.online from GoDaddy.com, and I configured Apache and Google API to recognize this domain name. 

### Setup SSH
I used ............

### Catalog DB
I refactored the database_setup.py file from the lesson to create catalogDB_setup.py. Each category is a section of the store. Each item, is an item sold at the store. I then created catalogDBpreLOAD.py to load dummy data into the database for additional testing. I tested by using 2 different Google accounts to ensure CRUD functions worked as desired. 

### JQuery and Drop Down lists
I added JQuery to the Main page so that the user can preview category items before clicking on each category individually. 

## Built With
- Sublime Text

## Author
[mrfresh382](https://github.com/mrfresh382)

## Acknowledgments
Much of the OAuth functionality was provided by Lorenzo Brown and the Udacity staff. Udacity's code can be found in the lessons and on [GitHub](https://github.com/udacity/OAuth2.0)# app_wsgi
