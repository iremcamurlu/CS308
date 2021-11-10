from django.db import models

# Create your models here.
""" class Users(models.Model):
    id=models.BigAutoField(primary_key=True)
    name=models.CharField('name',max_length=120)
    password=models.CharField('password',max_length=120)


    def __str__(self):
        return self.name """

class Users(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    id = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'Users'
