from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Volunteer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/VolunteerProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    status= models.BooleanField(default=False)
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
    impact=models.CharField(max_length=100)
    date=models.DateField(auto_now=True)
    def __str__(self):
        return self.name


class Work(models.Model):
    pandemic=models.ForeignKey(Pandemic,on_delete=models.CASCADE)
    volunteer=models.ForeignKey(Volunteer,on_delete=models.CASCADE)
    status=models.CharField(max_length=100)
    date=models.DateField(auto_now=True)
