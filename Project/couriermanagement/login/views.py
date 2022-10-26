from django.shortcuts import render
from login.models import Login

# Create your views here.
def post(request):
    if request.method=='POST':
        obj=Login()
        obj.username=request.POST.get('uname')
        obj.password=request.POST.get('password')
        obj.save()


    return render(request,'login/login.html')

