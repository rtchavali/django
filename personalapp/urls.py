from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.personal_index, name='index')
]