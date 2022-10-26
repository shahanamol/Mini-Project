from django.db import models

# Create your models here.

class Login(models.Model):
    login_id = models.AutoField(db_column='login id', primary_key=True)  # Field renamed to remove unsuitable characters.
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    type = models.CharField(max_length=15)
    u_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'login'
