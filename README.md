Getting Started With Wolfscout
==============================

Creating Your Virtual Environment:
----------------------------------
    cd ~/
    sudo mkdir /opt/
    sudo mkdir /opt/webapps
    sudo chown ubuntu /opt/webapps/
    cd /opt/webapps
    virtualenv --no-site-packages ncsu
    cd ncsu
    source bin/activate

###  Getting The Codebase:

    cd /opt/webapps/ncsu/
    git clone git@github.com:NCSU-VSR/wolfscout.git
    

### Install All Required Packages:

    cd /opt/webapps/ncsu/
    source bin/activate
    pip install Django South psycopg2==2.4.1 gunicorn PIL Fabric


### Write Your Local Settings File For Django:

Examine the code found in wolfscout/settings/sample.py . Then create your own file in the same directory that identifies your local environment like "sandysMac.py". After completing the values in the file to match your local environment (db engine, password, usernames, etc). Save the file again. 

Now go back to the root directory and look for ".gitignore", open this file in your favorite editor and look for the section "#Settings Files To Ignore (Your Local Ones)" append your newly created file to that list and save the file.

### Configuring Environment Variables:

With your favorite editor open the file "/opt/webapps/ncsu/bin/activate" and append the following lines to the file.

    export PYTHONPATH=.:/opt/webapps/ncsu
    export DJANGO_SETTINGS_MODULE=wolfscout.settings.MYSETTINGSFILE
    
With the name of your new settings file(no .py and keep whatever case you named it).

Development Utilities:
---------------------

These are the commands and tools you will be using frequently to test and deploy wolfscout.

### Fabric Commands

See fabfile.py inside the repository for a full list of commands and their function.

#### Commiting Locally

    fab updateLocal

#### Updating the Development Branch from Local Branch

    fab updateDev

#### Updating the Master Branch from Local Branch

    fab updateMaster