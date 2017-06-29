from __future__ import unicode_literals

from django.db import models
from ..login_and_registration_app.models import User
import datetime
from django.utils import timezone

def get_time_now():
    # return datetime.datetime.today()
    dt = datetime.datetime.now()
    return datetime.datetime(dt.year, dt.month, dt.day)

class ApptManager(models.Manager):
    def addApptVal(self, postData):
        context = {
            'error_message' : [],
            # 'success_message' : []
        }

        # print postData['travel_start']
        # print postData['travel_end']
        if not postData['date'] or len(postData['date']) < 1:
            context['error_message'].append(
                'ERROR: Please enter a date!')
        else:
            first_date= datetime.datetime.strptime(str(postData['date']),'%Y-%m-%d')
            date_now = get_time_now()
            if date_now > first_date:
                context['error_message'].append(
                    'ERROR: Date must be later than today\'s date!')

        # second_date= datetime.datetime.strptime(str(postData['travel_end']),'%Y-%m-%d')
        # print first_date
        # print second_date


        # if date_now > second_date:
        #     context['error_message'].append(
        #         'ERROR: Trip ending date of trip can\'t be less than today\'s date!')
        #
        # if first_date == second_date:
        #     context['error_message'].append(
        #         'ERROR: Start and end dates of the trip can\'t be the same!')
        #
        # if first_date > second_date:
        #     context['error_message'].append(
        #         'ERROR: Start date can\'t later then end date!')

        # results = {'status': True, 'errors': []}
        if not postData['time'] or len(postData['time']) < 1:
            context['error_message'].append(
                'ERROR: Please enter valid time!)')
        if not postData['task'] or len(postData['task']) < 1:
            context['error_message'].append(
                'ERROR: Please enter a task for your appointment!')



        # try:
        if context['error_message'] == []:
            user = User.objects.get(id=postData['creator'])

            appt_scheduled = Appointment.objects.create(
                task=postData['task'],
                appt_date=postData['date'],
                appt_time=postData['time'],
                userlink=user,
            )

            appt_scheduled.save()
            # appt_scheduled.user.add(user)

            # review.books.add(book)
            # review.users.add(user)

        # except IntegrityError as e:
        # except:
        #     results['status'] = False
        #     results['errors'].append('fail')

        return context

# Create your models here.
class Appointment(models.Model):
    task = models.TextField(blank=False, null=False)
    status = models.TextField(default='Pending')
    appt_date = models.DateTimeField()
    appt_time = models.TimeField(default=timezone.now())
    userlink = models.ForeignKey(User, related_name="users")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ApptManager()
    def __str__(self):
        return str(self.task)
