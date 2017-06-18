from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    # url('testimonials', views.testimonials), # this works
    url(r'^', views.testimonials),
    url(r'^$', views.index), # THIS DOES NOT WORK
]
