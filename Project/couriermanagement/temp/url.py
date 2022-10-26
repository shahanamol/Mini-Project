from django.conf.urls import url
from temp import views


urlpatterns = [
    url('home/', views.hhmm),
    url('admin/',views.temp),
    url('branch/',views.bbrr),
    url('employee/',views.eemm),
    url('public/',views.ppcc),
    # url(r'^emp_update/(?P<idd>\w+)',views.updtemp,name="emp_update"),

]