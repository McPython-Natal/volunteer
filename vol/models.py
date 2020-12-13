from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Volunteer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/VolunteerProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    status= models.BooleanField(default=False)
    age = models.CharField(null=True,max_length=20)
    certificate= models.ImageField(upload_to='certificates/',null=True,blank=True)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_instance(self):
        return self
    def __str__(self):
        return self.user.first_name

class Pandemic(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=500)
    risk_level=models.CharField(max_length=100)
    location=models.CharField(max_length=50,null=True)
    impact=models.CharField(max_length=100)
    date=models.DateField(auto_now=True)
    def __str__(self):
        return self.name


class Work(models.Model):
    pandemic=models.ForeignKey(Pandemic,on_delete=models.CASCADE)
    volunteer=models.ForeignKey(Volunteer,on_delete=models.CASCADE)
    status=models.CharField(max_length=100,default='Started Working')
    date=models.DateField(auto_now=True)

class WorkRequest(models.Model):
    choice=(('pending','pending'),('confirm','confirm'))
    pandemic=models.ForeignKey(Pandemic,on_delete=models.CASCADE)
    volunteer=models.ForeignKey(Volunteer,on_delete=models.CASCADE)
    status=models.CharField(max_length=20,choices=choice,default='pending')
    date=models.DateField(auto_now=True)



class Team(models.Model):
    pandemic=models.ForeignKey(Pandemic,on_delete=models.CASCADE)
    member1=models.ForeignKey(Volunteer,on_delete=models.CASCADE,related_name='member1')
    member2=models.ForeignKey(Volunteer,on_delete=models.CASCADE,related_name='member2')
    member3=models.ForeignKey(Volunteer,on_delete=models.CASCADE,related_name='member3')
    member4=models.ForeignKey(Volunteer,on_delete=models.CASCADE,related_name='member4')
    member5=models.ForeignKey(Volunteer,on_delete=models.CASCADE,related_name='member5')
    description=models.CharField(max_length=500)
    date=models.DateField(auto_now=True)
