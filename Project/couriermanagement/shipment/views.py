from django.shortcuts import render
from shipment.models import Shipment

# Create your views here.
def shipment(request):
    if request.method == 'POST':
        obj=Shipment()
        obj.courier_description=request.POST.get('dis')
        obj.parcel_weight=request.POST.get('weight')
        obj.parcel_dimension=request.POST.get('dim')
        obj.sender_name=request.POST.get('sname')
        obj.branch_processed=request.POST.get('branch')
        obj.recepient_name=request.POST.get('rname')
        obj.pickup_branch=request.POST.get('pickup')
        obj.parcel_price=request.POST.get('price')
        obj.tracking_no=request.POST.get('track')
        obj.date=request.POST.get('date')
        obj.save()
    return render(request,'shipment/Shipment.html')

def view(request):
    obj = Shipment.objects.all()
    context = {
        'abc': obj
    }
    return render(request,'shipment/view shipment.html',context)
def ad(request):
    obj=Shipment.objects.all()
    context={
        'mmm': obj
    }
    return render(request,'shipment/admin_view.html',context)

def search(request):
    if request.method=="POST":
        vv=request.POST.get('track')
        obj = Shipment.objects.filter(tracking_no__istartswith=vv)
        context = {
            'objval':obj
        }
    else:
        obj = Shipment.objects.all()
        context = {
            'objval': obj
        }
    return render(request,'shipment/pubtrack.html',context)

# def updateprofile(request,idd):
#     obj=Shipment.objects.get()
#     context={
#         'as':obj
#     }
#     if request.method=="POST":
#         obj=Shipment()
#         obj.courier_description = request.POST.get('dis')
#         obj.parcel_weight = request.POST.get('weight')
#         obj.parcel_dimension = request.POST.get('dim')
#         obj.sender_name = request.POST.get('sname')
#         obj.branch_processed = request.POST.get('branch')
#         obj.recepient_name = request.POST.get('rname')
#         obj.pickup_branch = request.POST.get('pickup')
#         obj.parcel_price = request.POST.get('price')
#         obj.tracking_no = request.POST.get('track')
#         obj.date = request.POST.get('date')
#         obj.save()
#     return view(request)
#     return render(request,'shipment/updt profile.html',context)