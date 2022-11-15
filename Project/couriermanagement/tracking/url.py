from django.conf.urls import url
from tracking import views

urlpatterns=[
    url('pst/',views.search),
    url('vew/',views.view),
    url('post/',views.publicpost)
]