from django.shortcuts import render
from tracking.models import Tracking
from shipment.models import Shipment
from login.models import Login
# Create your views here.
# def post(request):
#     if request.method=='POST':
#         ob=Tracking()
#         obj=Shipment()
#         obj.tracking_no=request.POST.get('track')
#         ob.entertrackingnumber=request.POST.get('number')
#         obj.courier_description=request.POST.get('description')
#         obj.branch_processed=request.POST.get('branch processed')
#         obj.pickup_branch=request.POST.get('branch pickup')
#         obj.date=request.POST.get('delivery date')
#         obj.save()
#
#     return render(request,'tracking/track.html')

def search(request):
    if request.method=="POST":
        vv=request.POST.get('track')
        obj = Shipment.objects.filter(tracking_number__istartswith=vv)
        context = {
            'objval':obj
        }
    else:
        obj = Tracking.objects.all()
        context = {
            'objval': obj
        }
    return render(request,'tracking/track.html',context)

def view(request):
    # obj=Tracking.objects.all()
    ob=Shipment.objects.all()
    context = {
        # 'bc': obj,
        'abc': ob
    }
    return render(request,'tracking/track.html',context)

def publicpost(request):
    if request.method == 'POST':
        obj = Tracking()
        obj.name = request.POST.get('name')
        obj.address= request.POST.get('address')
        obj.email = request.POST.get('email')
        obj.contactno= request.POST.get('contact no')
        obj.password = request.POST.get('password')
        obj.save()

        ob = Login()
        ob.username = obj.name
        ob.password = obj.password
        ob.type = "public"
        ob.u_id = obj.tracking_id
        ob.save()
    return render(request,'tracking/public.html')