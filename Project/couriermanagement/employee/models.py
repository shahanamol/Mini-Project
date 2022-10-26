from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    name = models.CharField(max_length=15)
    branch = models.CharField(max_length=15)
    contact_no = models.CharField(max_length=15)
    e_mail = models.CharField(db_column='e-mail', max_length=20)  # Field renamed to remove unsuitable characters.
    status = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'employee'
