from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^gameplay$', views.gameplay),
    url(r'^reset_game$', views.reset_game),
]
