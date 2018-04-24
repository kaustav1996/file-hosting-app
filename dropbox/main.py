import os
import urllib
import datetime
from google.appengine.api import users
from google.appengine.ext import ndb

import jinja2
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
#Models
# file and directory
# Classes and Functions

class MainPage(webapp2.RequestHandler):

    def get(self):
        user = users.get_current_user()
        if user:
            nickname = user.nickname()
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'
        if url_linktext == "Login" :
            template_values = {
            'user': user,
            'url': url,
            'url_linktext': url_linktext,
        }
            template = JINJA_ENVIRONMENT.get_template('login.html')
            self.response.write(template.render(template_values))
        else:
            template_values = {
            'path': path,
            'user': user,
            'url': url,
            'url_linktext': url_linktext,
        }
            template = JINJA_ENVIRONMENT.get_template('main.html')
            self.response.write(template.render(template_values))

app = webapp2.WSGIApplication([
	('/', MainPage),
	], debug=True)