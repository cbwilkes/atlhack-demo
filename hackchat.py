#!/usr/bin/env python

# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START imports]
import os
import urllib

from google.appengine.ext import ndb

import jinja2
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
# [END imports]

class Message(ndb.Model):
    author = ndb.StringProperty()
    content = ndb.StringProperty()
    timestamp = ndb.DateTimeProperty(auto_now_add=True)

class MainPage(webapp2.RequestHandler):
    def get(self):

        messages_query = Message.query().order(-Message.timestamp)
        messages = messages_query.fetch(10)
        template_values = {
            'messages': messages,
        }
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))

class HomePage(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        template = JINJA_ENVIRONMENT.get_template('home.html')
        self.response.write(template.render(template_values))

class Upload(webapp2.RequestHandler):
    def post(self):
        message = Message()
        message.author = self.request.get('author')
        message.content = self.request.get('content')
        message.put()
        self.redirect('/')

class ExamplePage(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        template = JINJA_ENVIRONMENT.get_template('example.html')
        self.response.write(template.render(template_values))

app = webapp2.WSGIApplication([
    webapp2.Route('/home', HomePage, name='home'),
    webapp2.Route('/', MainPage, name='chat'),
    webapp2.Route('/new', Upload, name='chat_upload'),
    webapp2.Route('/example', ExamplePage, name='example'),
    ], debug=True)
