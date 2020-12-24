from django.db import models


# Create your models here.
class IPUser(models.Model):
    user = models.CharField(max_length=10)
    ip_addr = models.CharField(max_length=17)
    mac_addr = models.CharField(max_length=17)

    class Meta:
        db_table = 'ipusers'
        ordering = ['user']