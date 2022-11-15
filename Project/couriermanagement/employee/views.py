from django.shortcuts import render
from employee.models import Employee
from login.models import Login
# Create your views here.
def emppost(request):
    if request.method=='POST':
        obj=Employee()
        obj.name=request.POST.get('name')
        obj.branch=request.POST.get('Branch')
        obj.contact_no=request.POST.get('Contact')
        obj.e_mail=request.POST.get('mail')
        obj.username=request.POST.get('uname')
        obj.password=request.POST.get('password')
        obj.save()

        ob=Login()
        ob.username = obj.username
        ob.password = obj.password
        ob.type = "employee"
        ob.u_id = obj.emp_id
        ob.save()

    return render(request,'employee/employee.html')

def  emp_view(request):
    obj=Employee.objects.all()
    context = {
        'ac' : obj
    }
    return render(request,'employee/view_employee.html',context)


def mng(request):
    obj=Employee.objects.all()
    context={
        'ppo':obj
    }
    return render(request,'employee/manage.html',context)



def ape(request,idd):
    obj=Employee.objects.get(emp_id=idd)
    obj.status='approved'
    obj.save()
    return emp_view(request)


def rjt(request,idd):
    obj=Employee.objects.get(emp_id=idd)
    obj.status='rejected'
    obj.save()
    return emp_view(request)