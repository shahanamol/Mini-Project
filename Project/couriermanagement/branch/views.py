from django.shortcuts import render
from branch.models import Branch
from login.models import Login
# Create your views here.
def post(request):
    if request.method=='POST':
        obj=Branch()
        obj.name=request.POST.get('name')
        obj.address=request.POST.get('address')
        obj.e_mail=request.POST.get('mail')
        obj.city=request.POST.get('city')
        obj.state=request.POST.get('State')
        obj.country=request.POST.get('Country')
        obj.pincode=request.POST.get('Pincode')
        obj.contact_no=request.POST.get('Contact')
        obj.username=request.POST.get('uname')
        obj.password=request.POST.get('password')
        obj.status='pending'
        obj.save()

        ob=Login()
        ob.username=obj.username
        ob.password=obj.password
        ob.type="branch"
        ob.u_id=obj.br_id
        ob.save()
    return render(request,'branch/branch.html')

def bd_view(request):
    obj=Branch.objects.all()
    context = {
        'ab': obj
    }
    return render(request,'branch/view_branch.html',context)


def mg_view(request):
    obj=Branch.objects.all()
    context= {
        'ppo':obj
    }
    return render(request,'branch/manage.html',context)



def app(request,idd):
    obj=Branch.objects.get(br_id=idd)
    obj.status='approved'
    obj.save()
    return bd_view(request)


def rjj(request,idd):
    obj=Branch.objects.get(br_id=idd)
    obj.status='rejected'
    obj.save()
    return bd_view(request)