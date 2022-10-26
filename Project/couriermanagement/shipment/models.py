from django.db import models

# Create your models here.

class Shipment(models.Model):
    c_id = models.AutoField(primary_key=True)
    courier_description = models.CharField(max_length=20)
    sender_name = models.CharField(max_length=15)
    recepient_name = models.CharField(max_length=15)
    parcel_weight = models.CharField(max_length=10)
    parcel_dimension = models.CharField(max_length=15)
    branch_processed = models.CharField(max_length=20)
    pickup_branch = models.CharField(max_length=20)
    parcel_price = models.CharField(max_length=10)
    date = models.DateField()
    tracking_no = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'shipment'
