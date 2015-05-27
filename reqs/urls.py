from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^hello/', views.funhello),
    url(r'^names/', views.names),
    url(r'^details/(?P<id>\d+)/', views.details),
    url(r'^insert/(?P<name>\w+)/(?P<reqs>\w+)/', views.add),
]
