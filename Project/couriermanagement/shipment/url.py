from django.conf.urls import url
from shipment import views

urlpatterns=[
    url('post/',views.shipment),
    url('vew/',views.view),
    url('asdmin/',views.ad)
]