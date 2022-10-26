from django.conf.urls import url
from tracking import views

urlpatterns=[
    url('pst/',views.post),
    url('vew/',views.view)
]