from __future__ import unicode_literals
from django.db import models
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):

    def register_validate(self, postData):
        email = postData['email']
        context = {
            'error_message' : [],
            'success_message' : []
        }

        if not EMAIL_REGEX.match(email):
            context['error_message'].append('ERROR: Invalid Email Address!')

        first_name = postData['first_name']
        if len(first_name) < 2:
            context['error_message'].append('ERROR: First name must be at least 2 characters!')

        last_name = postData['last_name']
        if len(last_name) < 2:
            context['error_message'].append('ERROR: Last name must be at least 2 characters!')

        password_in = postData['password']
        if len(password_in) < 8:
            context['error_message'].append('ERROR: Password must be at least 8 characters!')

        password_confirm = postData['password_confirm']
        if password_in != password_confirm:
            context['error_message'].append('ERROR: Password confirmation failed!')

        #now test to see if user exists for email
        check = User.objects.filter(email=email)
        if check:
            context['error_message'].append('ERROR: User already exists!')

        if not context['error_message'] == []:
            return context
        else:
            user = User.objects.create(
                first_name=postData['first_name'],
                last_name=postData['last_name'],
                email=postData['email'],
                password=bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt()),
            )
            user.save()
            context['success_message'].append('SUCCESS: User Registered!')
            context['user'] = user
            return context

    def login_validate(self, postData):

        context = {
            'error_message' : [],
            'success_message' : []
        }

        email = postData['email']

        if not EMAIL_REGEX.match(email):
            context['error_message'].append('ERROR: Invalid Email Address!')

        password_in = postData['password']
        if len(password_in) < 8:
            context['error_message'].append('ERROR: Password must be at least 8 characters!')

        #now test to see if user exists for email
        try:
            user = User.objects.get(email=email)
        except:
            context['error_message'].append('ERROR: User does not exist!')

        if user.password != bcrypt.hashpw(postData['password'].encode(), user.password.encode()):
            context['error_message'].append('ERROR: Password does not match!')

        if not context['error_message'] == []:
            return context
        else:
            context['success_message'].append('SUCCESS: User Logged In!')
            context['user'] = user
            return context

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.first_name
    objects = UserManager()
