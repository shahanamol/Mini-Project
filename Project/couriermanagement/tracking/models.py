from django.db import models

# Create your models here.
class Tracking(models.Model):
    tracking_id = models.AutoField(primary_key=True)
    tracking_number = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'tracking'
