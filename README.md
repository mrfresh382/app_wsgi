# Linux Server Turn-up/Config Project
Submitted by Doug McDonald for Udacity Full Stack Nanodegree.
This is a website for a fictional general store at the Big Bend National Park hosted on AWS Lightsail. 

## VM Specs
- Lightsail - Ubuntu 18.04
- DNS - using GoDaddy.com
- OAuth provided by Google API Console
- HTTPS provided by 'Let's Encrypt'

## VM Setup
1. Select an Ubuntu 18.04 instance and open in Lightsail. 
2. Enable Ports HTTP, HTTPS, TCP 123 , TCP 2200 in Networking and Firewall. 
3. I temporarily allowed SSH on default port 22 in case of disaster. This step can be un-done at the end. 
4. SSH into VM ( See 'User Guide for Udacity Grader' for help). Use the AWS provided SSH key to SSH into the VM for the first time. 
5. Once SSHed, I ran these commands to setup the VM as user `ubuntu`
```
sudo apt-get update -y && sudo apt-get upgrade -y

sudo ufw default deny incoming && sudo ufw default allow outgoing
sudo ufw allow www && sudo ufw allow 123/tcp
sudo ufw allow 2200/tcp
sudo ufw allow 443/tcp
sudo ufw enable -y
sudo ufw status

sudo apt-get install apache2 -y
sudo apt-get install finger -y
sudo apt-get install postgresql -y
sudo apt-get install libapache2-mod-wsgi -y
sudo apt-get install python-pip
sudo apt-get install finger
sudo pip install flask
sudo pip install httplib2
sudo pip install dos2unix
sudo pip install oauth2client
sudo pip install SQLalchemy
sudo apt-get install python-psycopg2
sudo apt-get install libpq-dev
sudo apt-get install putty-tools
```
6. It would be advisable to setup a grader and student user as soon as possible incase you get locked out of the ubuntu account. 
7. Disable remote root login and password login by adding directives to /etc/ssh/sshd_config:
```
PasswordAuthentication yes
PermitRootLogin no
```
Setup the grader account
## Getting Started
### Prerequisites 
A Google account is required for the user to have full permissions on the webpage. The grader must login to the server from SSH or PuTTY.


### User Guide for Udacity Grader
There is the option to use the shell or PuTTY to SSH to the AWS VM. The public key and .ppk file are provided in the 'Additional Notes' section with the project submission. The provided key has a passphrase and the grader account also a password which is provided. 

*Shell Option*
1. Convert provided public key to private key in appropriate folder
2. OR, use a virtual environment and install PuTTY keygen command line tool
```
sudo apt-get install putty-tools
puttygen <provided key file> -O private-openssh -o <converted private key>
sudo chmod 400 <converted private key>
```
3. Ensure key file has proper permissions and stored in appropriate directory such as /home/<user>/.ssh/...
4. SSH into AWS instance: `ssh -i <converted private key path> -p 2200 grader@18.204.23.73`

*PuTTY Option*
1. Use provided keyfile and save as file with .ppk extension. 
2. Use `grader@18.204.23.73` as host name and Port `2200`. Provide path to .ppk file in /Connection/SSH/Auth field.

### User Guide for General User
1. Visit [http://thedoug.online](http://thedoug.online) and enjoy!!!

## Notes/Issues/Bugs
- Links to HTTP for fonts had to be changed to HTTPS within the HTML templates
- Full path for client_secrets.json had to be added to the python file. This hard-coded change is not preferable, but works in this case. 
- catalog_app.py showCatagorys() function had to be updated to properly display preview items while browsing mainpage. Upon conversion to PostGreSQL, the lists had to be converted to dictionaries to properly display items and prevent fatal errors. 
- I accidently configured UFW with command "sudo ufw default deny outgoing" instead of "sudo ufw default allow outgoing" , this still permitted SSH into the VM, but I could not update packages or install new packages. 

## Design Notes
### Hello World and First Steps
I started this project by baseline configuring the server and creating a "Hello World" WSGI app. 

`if __name__ == '__main__':` section had to be updated to convert to WSGI to run with Apache Web Server. I did not setup a WSGI-APP daemon or create an '_init_.py' file as other students alluded to using. I was able to avoid these 2 steps and the app works just fine. This VM is serving a single function, so this step could be bypassed for the project, but would be important in other applications. 

### Pulled WebServer App files from GitHub
I had to create a new GitHub repo due to the previous project getting corrupt. The web server files are in /var/www/app_wsgi. The shebang line, absolute paths, and other bugs were debugged here.

### Setup DNS
I have domain thedoug.online from GoDaddy.com, and I configured Apache and Google API to recognize this domain name. HTTP redirects to HTTPS via the Apache config.

### Setup SSH
I used PuTTY to primarily SSH into the VM, but tested SSH using GitBash in a Windows 7 environment and Vagrant Ubuntu environment. I had to use `puttygen` command to convert .ppk file to a key file recognizable by shell 'ssh' command. 

### Catalog DB
Creating a catalog database in PostGreSQL did not require much code conversion besides making sure the correct packages were installed on the VM. Unlike SQLite3, PostGreSQL will create new primary key for new categories, rather than overwriting previous primary key integers, so this required a minor code change to accomodate all functionality. Instead of using a numbered list, I opted to use dictionaries to store the db so that I could preview using JQuery. 

### JQuery and Drop Down lists
I added JQuery to the Main page so that the user can preview category items before clicking on each category individually. See line 249 in catalog_app.py file for detailed explanation. 

### HTTPS
I re-configured Apache with the help of this [Digital Ocean tutorial](https://www.digitalocean.com/community/tutorials/how-to-secure-apache-with-let-s-encrypt-on-ubuntu-18-04). I had to ensure HTTPS port 443 was enabled in UFW and AWS Security Group. 

## Built With
- Sublime Text
- Nano text editor for last minute tweaks. 

## Author
[mrfresh382](https://github.com/mrfresh382)

## Acknowledgments
-[PostGreSQL](https://www.postgresql.org/docs/)
-[StackOverFlow](https://stackoverflow.com)
-[juvers Aka jayismonkey Linux Project Repo](https://github.com/juvers/Linux-Configuration)
-[Apache 2.4 Documentation](https://httpd.apache.org/docs/2.4/)
-Udacity
-[Digital Ocean-HTTPS](https://www.digitalocean.com/community/tutorials/how-to-secure-apache-with-let-s-encrypt-on-ubuntu-18-04)
-[Digital Ocean Tutorials and Forums](https://www.digitalocean.com/)
