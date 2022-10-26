from django.shortcuts import render

# Create your views here.
def temp(request):
    return render(request,'temp/admin.html')

def hhmm(request):
    return render(request,'temp/home.html')

def bbrr(request):
    return render(request,'temp/branch.html')

def eemm(requset):
    return render(requset,'temp/employee.html')

def ppcc(request):
    return render(request,'temp/public.html')