# BRAIN DUMP NOTES APPLICATION

## Project Description

#### BrainDump is a Django web app that allows users to store their ideas and thoughts in a structured manner. 

`Feel free to make changes based on your requirements. and if you like this project, ADD a STAR ⭐️`

## Getting Started:
To get started with BrainDump, you'll need to follow these steps:

#### Prerequisites
```
- Python 3.9
- pip package installer
- Git
- PostgreSQL
```

## Installing:
Clone the repository to your local machine:
```
git clone https://github.com/DavidDanso/brain-dump.git
```

#### Navigate to the project directory:
```
cd brain-dump/
```

#### Create a virtual environment:
```
python3 -m venv venv
```

#### Activate the virtual environment:
```
source venv/bin/activate
```

#### Install the required dependencies:
```
pip install -r requirements.txt
```

## Configuring PostgreSQL:
How to connect Project to PostgreSQL:

#### steps
```
1. Download PostgreSQL [ https://www.postgresql.org ]

2. Download pgAdmin [ https://www.pgadmin.org ]

3. Enter master password in pgAdmin [ one you created when download postgre ]

4. Create a new server and connect to your Project

5. Enter server name, hostname, port and password [ same password ]

6. Create a new DB

7. Use the name, username, password, host and port details to connect project to Postgre in the settings.py file

8. Open terminal and install psycopg2
```

## Connecting Django to PostgreSQL:
In your project's settings.py file, modify the DATABASES setting to use PostgreSQL:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ENTER_YOUR_DATABASE_NAME',
        'USER': 'ENTER_YOUR_DATABASE_USERNAME',
        'PASSWORD': 'ENTER_YOUR_DATABASE_PASSWORD',
        'HOST': 'localhost',
        'PORT': 'ENTER_YOUR_DATABASE_PORT_NUMBER',
    }
}
```

## Running the Server:
Migrate the database:
```
python manage.py migrate
```

Create a superuser account::
```
python manage.py createsuperuser
```

Start the development server:
```
python manage.py migrate
```

## Running the Server:
Migrate the database:
```
python manage.py runserver
```

`Visit http://localhost:8000 in your web browser to access the site.`


## App Preview:

<table width="100%"> 
<tr>
<td width="50%">      
&nbsp; 
<br>
<p align="center">
  Home Page
</p>
<img src="https://github.com/DavidDanso/brain-dump/blob/main/static/app-UI/home.png" />
</td> 
<td width="50%">
<br>
<p align="center">
  Sign Up Page
</p>
<img src="https://github.com/DavidDanso/brain-dump/blob/main/static/app-UI/sign_up.png" />
</td>
</table>

<table width="100%"> 
<tr>
<td width="50%">      
&nbsp; 
<br>
<p align="center">
  Login Page
</p>
<img src="https://github.com/DavidDanso/brain-dump/blob/main/static/app-UI/login.png" />
</td> 
<td width="50%">
<br>
<p align="center">
  Get Started
</p>
<img src="https://github.com/DavidDanso/brain-dump/blob/main/static/app-UI/get_started.png" />
</td>
</table>

<table width="100%"> 
<tr>
<td width="50%">      
&nbsp; 
<br>
<p align="center">
  Empty Page
</p>
<img src="https://github.com/DavidDanso/brain-dump/blob/main/static/app-UI/empty_allNote.png" />
</td> 
<td width="50%">
<br>
<p align="center">
  All Notes
</p>
<img src="https://github.com/DavidDanso/brain-dump/blob/main/static/app-UI/allNotes.png" />
</td>
</table>

<table width="100%"> 
<tr>
<td width="50%">      
&nbsp; 
<br>
<p align="center">
  Empty Page
</p>
<img src="https://github.com/DavidDanso/brain-dump/blob/main/static/app-UI/empty_quickNote.png" />
</td> 
<td width="50%">
<br>
<p align="center">
  Create Note
</p>
<img src="https://github.com/DavidDanso/brain-dump/blob/main/static/app-UI/createNote.png" />
</td>
</table>

<table width="100%"> 
<tr>
<td width="50%">      
&nbsp; 
<br>
<p align="center">
  Update Note
</p>
<img src="https://github.com/DavidDanso/brain-dump/blob/main/static/app-UI/updateNote.png" />
</td> 
<td width="50%">
<br>
<p align="center">
  Delete Note
</p>
<img src="https://github.com/DavidDanso/brain-dump/blob/main/static/app-UI/deleteNote.png" />
</td>
</table>

<table width="100%"> 
<tr>
<td width="50%">      
&nbsp; 
<br>
<p align="center">
  View Note
</p>
<img src="https://github.com/DavidDanso/brain-dump/blob/main/static/app-UI/viewNote.png" />
</td> 
<td width="50%">
<br>
<p align="center">
  Create New Folder
</p>
<img src="https://github.com/DavidDanso/brain-dump/blob/main/static/app-UI/createFolder.png" />
</td>
</table>

<table width="100%"> 
<tr>
<td width="50%">      
&nbsp; 
<br>
<p align="center">
  New Folder Page
</p>
<img src="https://github.com/DavidDanso/brain-dump/blob/main/static/app-UI/newFolderPage.png" />
</td> 
<td width="50%">
<br>
<p align="center">
  Delete Folder Page
</p>
<img src="https://github.com/DavidDanso/brain-dump/blob/main/static/app-UI/deleteFolder.png" />
</td>
</table>

<table width="100%"> 
<tr>
<td width="50%">      
&nbsp; 
<br>
<p align="center">
  User Profile
</p>
<img src="https://github.com/DavidDanso/brain-dump/blob/main/static/app-UI/userProfile.png" />
</td> 
<td width="50%">
<br>
<p align="center">
  Delete Profile Account
</p>
<img src="https://github.com/DavidDanso/brain-dump/blob/main/static/app-UI/deleteAccount.png" />
</td>
</table>

## Authors
David Danso - Initial work - [GitHub Profile](https://github.com/DavidDanso)

##### Email: davidkellybrownson@gmail.com

### Happy Coding!
