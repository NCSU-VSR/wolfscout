Getting Started With Wolfscout
==============================

### Installing Required Packages (Ubuntu Linux)

These packages need to be installed for the rest of the turoial to work.

    sudo apt-get install python-virtualenv python-dev libjpeg-dev git-core libpq-dev

### Installing Required Packages (Mac OSX)

You will need to have Python 2.7 and Git Installed. To install Python 2.7 Install OSX 10.7(Lion) and Install Xcode.
To install git visit: (http://code.google.com/p/git-osx-installer/) and download the version for your computer, then install it.


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

    cd /opt/webapps/ncsu/wolfscout
    source ../bin/activate
    pip install -r requirements.txt

### Configuring Environment Variables:

With your favorite editor open the file "/opt/webapps/ncsu/bin/activate" and append the following lines to the file.

    export PYTHONPATH=.:/opt/webapps/ncsu
    export DJANGO_SETTINGS_MODULE=wolfscout.settings.sample
    
With the name of your new settings file(no .py and keep whatever case you named it).

### Configuring Your Branch (Version Control)

Use only your firstname or combo first and last together(no spaces)

    cd /opt/webapps/ncsu/wolfscout/
    source ../bin/activate
    git branch yourname
    git checkout yourname
    git pull origin development
    git commit -m "I am updating my branch with development"
    git push origin yourname

### Configuring Fabric

Using your favorite text editor called .fabricrc in your home directory (~/.fabricrc). Complete it like so:

    user = ubuntu
    localBranch = yournamme

The user argument is for the remote server(everyone shares this) and the localBrach tells fabric which branch it is currently working with.

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