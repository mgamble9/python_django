from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_course$', views.add_course),
    url(r'^course/destroy/(?P<id>\d+)$', views.delete_page),
    url(r'^delete_course$', views.delete_course),
]
