from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Appointment
from ..login_and_registration_app.models import User
import datetime

def get_date_now():
    return datetime.date.today()

# Create your views here.
def index(request):
    # User.objects.all().delete()
    # Appointment.objects.all().delete()
    return render(request, 'appointments_app/index.html')

def appointments(request):
    # print "*"*42
    if not request.session.get('id'):
        messages.error(request, 'Access Denied. Log in first.')
        return redirect('/')
    user = User.objects.get(id=request.session.get('id'))
    # trips = user.trips.all().order_by('-created_at')
    todays_date = get_date_now()
    todays_appts = Appointment.objects.filter(userlink=user).exclude(appt_date__gt=todays_date)
    # todays_appts = Appointment.objects.filter(userlink=user, appt_date=todays_date)
    # todays_appts = Appointment.objects.filter(userlink=user, appt_date=todays_date).order_by('-created_at')
    # later_appts = Appointment.objects.filter(userlink=user).exclude(appt_date__gt=todays_date)
    later_appts = Appointment.objects.filter(userlink=user).exclude(appt_date=todays_date)
    print "*"*42
    print todays_date
    print todays_appts
    print later_appts
    print "*"*42
    context = {
        'user': user,
        'todays_appts': todays_appts,
        'later_appts': later_appts,
    }
    # print context
    return render(request, 'appointments_app/appointments.html', context)

def add_appt(request):
    if not request.session.get('id'):
        messages.error(request, 'Access Denied. Log in first.')
        return redirect('/travel_dashboard')
    results = Appointment.objects.addApptVal(request.POST)
    if not results['error_message'] == []:
        for error in results['error_message']:
            messages.error(request, error)
    else:
        messages.success(request, 'Appointment Successfuly Added.')
        # return redirect('books/'+str(results['book'].id))
    return redirect('/appointments')

def delete_appt(request, id):
    appt = Appointment.objects.get(id=id)
    appt.delete()
    return redirect('/appointments')

def edit_appt(request, id):
    appt = Appointment.objects.get(id=id)
    # print "*"*42
    # print appt
    # print "*"*42
    # appt_date_str = str(appt.appt_date)
    # appt_date_massaged = datetime.datetime.strptime(appt_date_str,'%Y-%m-%d')
    appt_date_massaged = datetime.datetime.strftime(appt.appt_date,'%Y-%m-%d')
    appt_time_str = str(appt.appt_time)
    # print appt_time_str
    context = {
        'task' : appt.task,
        'appt_date' : appt_date_massaged,
        # 'appt_time' : appt.appt_time,
        'appt_time' : appt_time_str,
        'appt_status' : appt.status,
        'appt_id' : appt.id
    }
    print context
    return render(request, 'appointments_app/edit_appt.html', context)

def edit_appt_process(request):
    if request.method == 'POST':
        print request.POST
        print request.POST['appt_id']
        appt = Appointment.objects.get(id=request.POST['appt_id'])
        appt.task = request.POST['task']
        appt.status = request.POST['status']
        appt.appt_date = request.POST['date']
        appt.appt_time = request.POST['time']
        appt.save()
    return redirect('/appointments')

def logout(request):
    request.session.clear()
    messages.success(request, 'Logged Out')
    return redirect('/')

def home(request):
    return redirect('/appointments')
