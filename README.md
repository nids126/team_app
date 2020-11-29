# Team Member App

_This implement an HTTP API to support a team-member management
application. The application supports listing team members, adding a new team member, editing a team member,
and deleting a team member._

#### APIs supported:  
- Lists all members.
- Given Id, view an existing member. 
- Add a new member.
- Update an existing member
- Delete an existing member.

_**Added Features**:_  
Restricts duplicate phone number/email entry

#### Prerequisites and Setup steps are mentioned below.

**Prerequisites**

1. Python 3 environment (Install from here if not present: https://www.python.org/downloads/)
To check if present: run command - `python3 --version` on terminal, it should give you the installed version
2. MySQL - (Should be up and running)
2. Install pip3 (https://www.makeuseof.com/tag/install-pip-for-python/)
3. Install virtual environment (pip3 install virtualenv) 


##### Update mysql username & password in `team_app/settings.py` at line 83-84
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'team_app',
        'USER': '<username>',
        'PASSWORD': '<password>',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

**Steps to set up:**

1. `cd path/to/teamapp ` in terminal
2. `virtualenv -p python3 env` to create new virtual environment to install required packages (This is highly recommended)
3. `source env/bin/activate` (Activate the virtual environment)
4. `sh install.sh` (This creates all the necessary schemas and tables required for application)
5. `pip install -r requirements.txt` (Install required libraries)
6.  `python manage.py migrate` (Make database migrations)

**Run Server**

Run command : `python manage.py runserver` 
If the set up is done correctly, it should show like this: 
```
dell@nidhi-pc:~/path/to/team_app$ python manage.py runsver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
November 28, 2020 - 14:02:13
Django version 3.1.3, using settings 'team_app.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

```

**Open Page:** 

Further API details can be viewed from here:
http://127.0.0.1:8000/

**CURL commands for APIs**
- Lists all members.  
`curl -X GET http://127.0.0.1:8000/members/`

- View an existing member.  
`curl -X GET http://127.0.0.1:8000/members/<memberId>/`

- Add a new member.  
`curl http://127.0.0.1:8000/members/create -H "content-type: application/json" -d '{"firstName": "Sample", "lastName": "User2", "phoneNumber": "9008689888", "email": "sampleuser2@gmail.com"}'`

- Update an existing member.  
`curl http://127.0.0.1:8000/members/update/<memberId> -H "content-type: application/json" -d '{"firstName": "Sample", "lastName": "User4", "phoneNumber": "9003689888", "email": "sampleuser4@gmail.com"}'`

- Delete an existing member.
`http://127.0.0.1:8000/members/delete/<memberId>`
