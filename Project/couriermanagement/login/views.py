from django.shortcuts import render
from django.http import HttpResponseRedirect
from login.models import Login

# Create your views here.
def post(request):
    if request.method=='POST':
        uname=request.POST.get('user')
        passw=request.POST.get('password')
        obj=Login.objects.filter(username=uname,password=passw)
        tp=''
        for ob in obj:
            tp=ob.type
            uid=ob.u_id
            if tp=='admin':
                request.session["uid"]=uid
                return HttpResponseRedirect('/temp/admin/')
            if tp=='branch':
                request.session["uid"]=uid
                return HttpResponseRedirect('/temp/branch/')
            if tp=='employee':
                request.session["uid"]=uid
                return HttpResponseRedirect('/temp/employee/')
            if tp=='public':
                request.session["uid"]=uid
                return HttpResponseRedirect('/temp/public/')
            objlist="Username or Password incorrect"
            context={
                'msg':objlist
            }
            return render(request,'login/login.html',context)

    return render(request,'login/login.html')

