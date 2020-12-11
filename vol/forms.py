from django import forms
from django.contrib.auth.models import User
from . import models

class VolunteerUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }

class VolunteerForm(forms.ModelForm):
    class Meta:
        model=models.Volunteer
        fields=['address','mobile','profile_pic','age','certificate']

class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))


class PandemicForm(forms.ModelForm):
    class Meta:
        model=models.Pandemic
        fields='__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3, 'cols': 100}),
            'risk_level': forms.Textarea(attrs={'rows': 2, 'cols': 100}),
            'impact': forms.Textarea(attrs={'rows': 2, 'cols': 100})
        }

class WorkForm(forms.ModelForm):
    pandemicId=forms.ModelChoiceField(queryset=models.Pandemic.objects.all(),empty_label="Pandemic Name", to_field_name="id")
    volunteerId=forms.ModelChoiceField(queryset=models.Volunteer.objects.all().filter(status=True),empty_label="Volunteer Name", to_field_name="user_id")
    class Meta:
        model=models.Work
        fields=['status']

class TeamForm(forms.ModelForm):
    pandemicId=forms.ModelChoiceField(queryset=models.Pandemic.objects.all(),empty_label="Pandemic Name", to_field_name="id")
    member1=forms.ModelChoiceField(queryset=models.Volunteer.objects.all().filter(status=True),empty_label="Member 1 Name", to_field_name="user_id")
    member2=forms.ModelChoiceField(queryset=models.Volunteer.objects.all().filter(status=True),empty_label="Member 2 Name", to_field_name="user_id")
    member3=forms.ModelChoiceField(queryset=models.Volunteer.objects.all().filter(status=True),empty_label="Member 3 Name", to_field_name="user_id")
    member4=forms.ModelChoiceField(queryset=models.Volunteer.objects.all().filter(status=True),empty_label="Member 4 Name", to_field_name="user_id")
    member5=forms.ModelChoiceField(queryset=models.Volunteer.objects.all().filter(status=True),empty_label="Member 5 Name", to_field_name="user_id")
    class Meta:
        model=models.Team
        fields=['description']
