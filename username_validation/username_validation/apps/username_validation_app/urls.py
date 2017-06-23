from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^validate', views.validate),
    url(r'^invalid', views.invalid),
    url(r'^success', views.success),
    url(r'^add', views.add),
    url(r'^remove/(?P<id>\d+)', views.remove),
]
