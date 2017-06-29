from django.conf.urls import url
from . import views
app_name = 'appts'
urlpatterns = [
    url(r'^$', views.index),
    url(r'^appointments$', views.appointments),
    url(r'^add_appt$', views.add_appt, name='add_appt'),
    url(r'^delete_appt/(?P<id>\d+)$', views.delete_appt, name='delete_appt'),
    url(r'^appointments/(?P<id>\d+)$', views.edit_appt, name='edit_appt'),
    url(r'^edit_appt_process$', views.edit_appt_process, name='edit_appt_process'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^home$', views.home, name='home'),

]
