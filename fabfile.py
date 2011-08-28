from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm

__author__ = 'chris'
"""
Fabric is a utility that automates many things, here are some functions for prepping
the code for release onto a production server
"""

env.hosts = ['wolfscout.ncsu.edu']

def testData():
    print str(env.localBranch)

#usage: fab commit:'my commit message here'
def commit(commitMessage):
    #add all new local files
    local('git add .')
    local('git commit -m '+ '"' + str(commitMessage) + '"')

def pushLocal():
    #just push it out
    local('git push origin %s' % env.localBranch)
    local('git pull origin development')
    local('git push origin %s' % env.localBranch)

def updateDev():
    local('git checkout development')
    local('git pull origin development')
    local('git pull origin %s'% env.localBranch)
    local('git push origin development')
    local('git checkout %s' % env.localBranch)

def update(commitMessage):
    commit(commitMessage)
    pushLocal()
    updateDev()

def updateRemote():
    with cd('/opt/webapps/django/pdfsupply'):
        run('git pull origin development')
        run('sudo service gunicorn restart')