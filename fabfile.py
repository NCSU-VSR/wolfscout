from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm
#Lauren's first edit
__author__ = 'chris'
"""
Fabric is a utility that automates many things, here are some functions for prepping
the code for release onto a production server

In order for many fab commands to work, env.localbranch will need to be defined. In order to do this,
create a file in your home dir called .fabricrc. Add the following two lines where <user> is your git user
and <localBranch> is the name of your local branch.
user = <user>
localBranch = <localBranch>
"""

env.hosts = ['wolfscout.ncsu.edu']

def commands():
    """
    prints out all the fab commands
    """
    print 'test migrate runServer commit pushLocal syncLocalWithDev syncLocalWithMaster updateLocal updateDev updateMaster deployToProduction'

def test():
    """
    Runs all tests in the django project
    """
    local('django-admin.py test')

def migrate():
    """
    Runs migrations on the database. If there are no migrations to be done, will do nothing.
    """
    local('django-admin.py migrate apps.crawler.cronos')
    local('django-admin.py migrate apps.crawler.gpscollar')
    local('django-admin.py migrate apps.study')
    local('django-admin.py migrate apps.wildlife')

def runServer():
    """
    Runs the server
    """
    local('django-admin.py runserver')

def commit():
    """
    Starts by running tests on the project.
    If tests fail the script ends.
    Adds all files that are new in project
    Then it starts the commit by asking for your commit message in the shell.
    After you press enter it will commit to your local repo.
    """
    test()
    local('git add -p && git commit')

def pushLocal():
    """
    To be done after a commit, it will push the changes to your local repo.
    After that it will execute all tests in the django project.
    If the tests complete it will 
    """
    test()
    local('git push origin %s' % env.localBranch)

def syncLocalWithDev():
    """
    After pushing local you may wish to update your branch with the content from the development
    branch. Todo this we first test your code again, then pull in the code from development, and test it.
    If both sets of tests pass, your code is allowed to be pushed into the dev branch.
    """
    test()
    local('git pull origin development')
    test()
    local('git push origin %s' % env.localBranch)

def syncLocalWithMaster():
    """
    After pushing local you may wish to update your branch with the content from the master
    branch. Todo this we first test your code again, then pull in the code from master, and test it.
    If both sets of tests pass, your code is allowed to be pushed into the master branch.
    """
    test()
    local('git pull origin master')
    test()
    local('git push origin %s' % env.localBranch)

def updateLocal():
    """
    update relies on the functionality of the aforementioned methods to do the following tasks:
        1. Test your current code and allow a commit to your local repo
        2. Push your local changes up to the global repo under your branch.
    """
    commit()
    pushLocal()

def updateLocalNoTest():
    local('git add -p && git commit')
    local('git push origin %s' % env.localBranch)

def updateDev():
    """
    The goal here is to update the development repository to your latest changes.
    At first we sync your local repo with all the changes in the dev repo and validate these changes.
    Followed by checking out the development branch.
    Then we pull in any new changes that we may not have.(extra caution)
    After that we get the content of your local branch.
    Again tests must be run to ensure the build is sanitary.
    Once test validation is complete it will push the code to the central development repository.
    Finally it ends by switching your branch back to your local dev branch.
    """
    syncLocalWithDev()
    local('git checkout development')
    local('git pull origin development')
    local('git pull origin %s'% env.localBranch)
    test()
    local('git push origin development')
    local('git checkout %s' % env.localBranch)

def updateMaster():
    """
    Same workflow as updateDev but with the master branch
    """
    syncLocalWithDev()
    local('git checkout master')
    local('git pull origin master')
    local('git pull origin %s'% env.localBranch)
    test()
    local('git push origin master')
    local('git checkout %s' % env.localBranch)

def deployToProduction():
    """
    !!!! CAUTION: THIS CODE IS NOT COMPLETE AT THE MOMENT DO NOT RELY ON IT !!!!

    deployToProduction does exactly what it specifies that it will do.
    1. Logon to production server
    2. CD to project location
    3. Activate Shell Content
    4. Pull in the latest production changes
    5. Test them
    6. If tests pass it reboots the web server
    """
    with cd('/opt/webapps/ncsu/wolfscout'):
        run('source ../bin/activate')
        run('git pull origin master')
        run('django-admin.py test')
        run('sudo service gunicorn restart')