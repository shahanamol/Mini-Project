from django.db import models

# Create your models here.

class Branch(models.Model):
    br_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    e_mail = models.CharField(db_column='e-mail', max_length=20)  # Field renamed to remove unsuitable characters.
    address = models.CharField(max_length=25)
    city = models.CharField(max_length=15)
    contact_no = models.CharField(db_column='contact _no', max_length=12)  # Field renamed to remove unsuitable characters.
    state = models.CharField(max_length=15)
    pincode = models.CharField(max_length=10)
    country = models.CharField(max_length=20)
    name = models.CharField(max_length=15)
    status = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'branch'
