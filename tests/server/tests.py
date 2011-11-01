from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
__author__ = 'bo'

class ServerTestCases(TestCase):
    #fixtures = ['serverTestFixtures.json']
    loginURL = '/login/'
    client = Client()
    STATUS_OK = 200
    existingUser = {'id':'id', 'password':'password'}
    user = User.objects.create_user(existingUser['id'], 'email@email.com', existingUser['password'])
    
    def setUp(self):
        self.client = Client()
        self.assertTrue(self.login())

    def test_loginPage(self):
        response = self.client.get('/login/')
        self.assertEquals(response.status_code, self.STATUS_OK)

    def test_redirect_loggedIn(self):
        response = self.client.get('', follow=True)
        self.assertTrue(len(response.redirect_chain) == 0)

    def test_redirect_loggedOut(self):
        self.client.logout()
        response = self.client.get('', follow=True)
        self.assertTrue(len(response.redirect_chain) == 1)
        redirect = response.redirect_chain[0]
        self.assertIn('/login/?next=/', redirect[0])
        self.assertEquals(302, redirect[1])

    def login(self):
        return self.client.login(username=self.existingUser['id'], password=self.existingUser['password'])