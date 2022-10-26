from django.conf.urls import url
from branch import views

urlpatterns=[
    url('pst/',views.post),
    url('vew/',views.bd_view),
    url('aprv/(?P<idd>\w+)',views.app),
    url('rjct/(?P<idd>\w+)',views.rjj,name="rj")
]