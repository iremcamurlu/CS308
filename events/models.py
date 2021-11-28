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


class Usersv2(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Usersv2'


class Student(models.Model):
   
    sname = models.CharField(max_length=40, blank=True, null=True)
    semail = models.CharField(max_length=40, blank=True, null=True)
    spass = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'



class Alluniv(models.Model):
    univname = models.CharField(max_length=100, blank=True, null=True)
    unicity = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alluniv'



class GradStudent(models.Model):
    gname = models.CharField(max_length=100, blank=True, null=True)
    gpass = models.CharField(max_length=100, blank=True, null=True)
    gemail = models.CharField(max_length=100, blank=True, null=True)
    gmajor = models.CharField(max_length=100, blank=True, null=True)
    guniv = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'grad_student'



class Question(models.Model):
    univid = models.CharField(max_length=100)
    sid = models.CharField(max_length=100)
    question = models.CharField(max_length=256)
    answer = models.CharField(max_length=100, blank=True, null=True)
    gid = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'question'