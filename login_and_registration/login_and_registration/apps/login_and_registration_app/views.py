from django.shortcuts import render, redirect
from . models import User
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, "login_and_registration_app/index.html")

def validate_registration(request):
    if request.method == 'POST':
        postData = request.POST
        email = request.POST['email']
        context = User.objects.register_validate(postData)
        if context['error_message']:
            for err_msg in context['error_message']:
                messages.add_message(request, messages.ERROR, err_msg)
            return render(request, "login_and_registration_app/index.html")
        if context['success_message']:
            for success_msg in context['success_message']:
                messages.add_message(request, messages.SUCCESS, success_msg)
            user = User.objects.filter(email=email)
            context = {'user' : user}
            return render(request, "login_and_registration_app/success.html", context)
        else:
            return redirect('/')

def validate_login(request):
    if request.method == 'POST':
        postData = request.POST
        # print postData
        email = request.POST['email']
        # print email
        user = User.objects.filter(email=email)
        # firstname = user.first_name
        # try:
        #     not user
        # except:
        #     print user
        print "*"*42
        print user
        context = User.objects.login_validate(postData)
        if context['error_message']:
            for err_msg in context['error_message']:
                messages.add_message(request, messages.ERROR, err_msg)
            return render(request, "login_and_registration_app/index.html")
        if context['success_message']:
            for success_msg in context['success_message']:
                messages.add_message(request, messages.SUCCESS, success_msg)
            # firstname = user.first_name
            context = {'user' : user}
            print context
            return render(request, "login_and_registration_app/success.html", context)
        else:
            return redirect('/')
