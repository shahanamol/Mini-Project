from django.shortcuts import render
from tracking.models import Tracking
from shipment.models import Shipment
# Create your views here.
def post(request):
    if request.method=='POST':
        ob=Tracking()
        obj=Shipment()
        ob.entertrackingnumber=request.POST.get('number')
        obj.courier_description=request.POST.get('description')
        obj.branch_processed=request.POST.get('branch processed')
        obj.pickup_branch=request.POST.get('branch pickup')
        obj.date=request.POST.get('delivery date')
        obj.save()

    return render(request,'tracking/track.html')

def view(request):
    obj=Tracking.objects.all()
    ob=Shipment.objects.all()
    context = {
        'bc': obj,
        'ad': ob
    }
    return render(request,'tracking/track.html',context)