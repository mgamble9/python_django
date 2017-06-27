from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^validate_registration$', views.validate_registration),
    url(r'^validate_login$', views.validate_login),
    url(r'^success$', views.success),
]
