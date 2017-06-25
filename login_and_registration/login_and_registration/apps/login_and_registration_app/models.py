from __future__ import unicode_literals
# from django.shortcuts import render, redirect
# from django.contrib import messages
from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):

    def register_validate(self, postData):
        email = postData['email']
        try:
            context
        except:
            context = {
                'error_message' : [],
                'success_message' : [],
            }
            input_fail = False
        # print context

        if not EMAIL_REGEX.match(email):
            context['error_message'].append('ERROR: Invalid Email Address!')
            # print context
            input_fail = True

        first_name = postData['first_name']
        if len(first_name) < 2:
            context['error_message'].append('ERROR: First name must be at least 2 characters!')
            # print context
            input_fail = True


        last_name = postData['last_name']
        if len(last_name) < 2:
            # messages.add_message(request, messages.ERROR,
                # 'Last name must be at least 3 characters!')
            # context = {
            #     'error_message' : 'Last name must be at least 2 characters!'
            # }
            # return redirect('/', context)
            context['error_message'].append('ERROR: Last name must be at least 2 characters!')
            # print context
            input_fail = True

        password_in = postData['password']
        if len(password_in) < 8:
            context['error_message'].append('ERROR: Password must be at least 8 characters!')
            # print context
            input_fail = True

        password_confirm = postData['password_confirm']
        if password_in != password_confirm:
            context['error_message'].append('ERROR: Password confirmation failed!')
            # print context
            input_fail = True

        #now test to see if user exists for email
        user = User.objects.filter(email=email)
        # users = User.objects(all)
        print user
        if user.exists():
            context['error_message'].append('ERROR: User already exists!')
            # print context
            input_fail = True

        if input_fail:
            return context
        else:
            user = User.objects.create(
                first_name=postData['first_name'],
                last_name=postData['last_name'],
                email=postData['email'],
                password=postData['password'],
            )
            user.save()
            context['success_message'].append('SUCCESS: User Registered!')
            context['user'] = user
            # print context
            return context

    def login_validate(self, postData):

        email = postData['email']
        try:
            context
        except:
            context = {
                'error_message' : [],
                'success_message' : [],
            }
            input_fail = False

        if not EMAIL_REGEX.match(email):
            context['error_message'].append('ERROR: Invalid Email Address!')
            input_fail = True

        password_in = postData['password']
        if len(password_in) < 8:
            context['error_message'].append('ERROR: Password must be at least 8 characters!')
            input_fail = True

        #now test to see if user exists for email
        # users = User.objects(all)
        # print users
        user = User.objects.filter(email=email)
        if not user.exists():
            context['error_message'].append('ERROR: User does not exist!')
            # print context
            input_fail = True

        if input_fail:
            return context
        else:
            context['success_message'].append('SUCCESS: User Logged In!')
            context['user'] = user
            # print context
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
