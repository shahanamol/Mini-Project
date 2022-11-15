from django.conf.urls import url
from employee import views

urlpatterns=[
    url('pst/',views.emppost),
    url('vew/',views.emp_view),
    url('manage/',views.mng),
    url('apve/(?P<idd>\w+)',views.ape),
    url('rejt/(?P<idd>\w+)',views.rjt,name="rt")
]