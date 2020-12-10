from django.shortcuts import render,redirect,reverse
from . import forms,models
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings
from django.contrib.auth.models import User

def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'vol/index.html')


#for showing signup/login button for VOLUNTEER
def volunteerclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'vol/volunteerclick.html')


#for showing signup/login button for ADMIN
def adminclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return HttpResponseRedirect('adminlogin')


def volunteer_signup_view(request):
    userForm=forms.VolunteerUserForm()
    volunteerForm=forms.VolunteerForm()
    mydict={'userForm':userForm,'volunteerForm':volunteerForm}
    if request.method=='POST':
        userForm=forms.VolunteerUserForm(request.POST)
        volunteerForm=forms.VolunteerForm(request.POST,request.FILES)
        if userForm.is_valid() and volunteerForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            volunteer=volunteerForm.save(commit=False)
            volunteer.user=user
            volunteer.save()
            my_volunteer_group = Group.objects.get_or_create(name='VOLUNTEER')
            my_volunteer_group[0].user_set.add(user)
        return HttpResponseRedirect('volunteerlogin')
    return render(request,'vol/volunteersignup.html',context=mydict)

def is_volunteer(user):
    return user.groups.filter(name='VOLUNTEER').exists()

def afterlogin_view(request):          
    if is_volunteer(request.user):
        accountapproval=models.Volunteer.objects.all().filter(user_id=request.user.id,status=True)
        if accountapproval:
            return redirect('volunteer-dashboard')
        else:
            return render(request,'vol/volunteer_wait_for_approval.html')
    else:
        return redirect('admin-dashboard')


@login_required(login_url='adminlogin')
def admin_dashboard_view(request):
    dict={ 
    'total_volunteer':models.Volunteer.objects.all().filter(status=True).count(),
    'total_pending_volunteer':models.Volunteer.objects.all().filter(status=False).count(),   
    }
    return render(request,'vol/admin_dashboard.html',context=dict)


@login_required(login_url='adminlogin')
def admin_volunteer_view(request):
    return render(request,'vol/admin_volunteer.html')



@login_required(login_url='adminlogin')
def admin_view_volunteer_view(request):
    volunteers= models.Volunteer.objects.all().filter(status=True)
    return render(request,'vol/admin_view_volunteer.html',{'volunteers':volunteers})


@login_required(login_url='adminlogin')
def update_volunteer_view(request,pk):
    volunteer=models.Volunteer.objects.get(id=pk)
    user=models.User.objects.get(id=volunteer.user_id)

    userForm=forms.VolunteerUserForm(instance=user)
    volunteerForm=forms.VolunteerForm(request.FILES,instance=volunteer)
    mydict={'userForm':userForm,'volunteerForm':volunteerForm}
    if request.method=='POST':
        userForm=forms.VolunteerUserForm(request.POST,instance=user)
        volunteerForm=forms.VolunteerForm(request.POST,request.FILES,instance=volunteer)
        if userForm.is_valid() and volunteerForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            volunteerForm.save()
            return redirect('admin-view-volunteer')
    return render(request,'vol/update_volunteer.html',context=mydict)



@login_required(login_url='adminlogin')
def delete_volunteer_view(request,pk):
    volunteer=models.Volunteer.objects.get(id=pk)
    user=User.objects.get(id=volunteer.user_id)
    user.delete()
    volunteer.delete()
    return HttpResponseRedirect('/admin-view-volunteer')


@login_required(login_url='adminlogin')
def admin_view_pending_volunteer_view(request):
    volunteers= models.Volunteer.objects.all().filter(status=False)
    return render(request,'vol/admin_view_pending_volunteer.html',{'volunteers':volunteers})


@login_required(login_url='adminlogin')
def approve_volunteer_view(request,pk):
    volunteer=models.Volunteer.objects.get(id=pk)
    volunteer.status=True
    volunteer.save()
    return HttpResponseRedirect('/admin-view-pending-volunteer')
    

@login_required(login_url='adminlogin')
def reject_volunteer_view(request,pk):
    volunteer=models.Volunteer.objects.get(id=pk)
    user=User.objects.get(id=volunteer.user_id)
    user.delete()
    volunteer.delete()
    return HttpResponseRedirect('/admin-view-pending-volunteer')


@login_required(login_url='adminlogin')
def admin_notification_view(request):
    return render(request,'vol/admin_notification.html')


@login_required(login_url='adminlogin')
def admin_add_pandemic_view(request):
    pandemicForm=forms.PandemicForm()
    mydict={'pandemicForm':pandemicForm}
    if request.method=='POST':
        pandemicForm=forms.PandemicForm(request.POST)
        
        if pandemicForm.is_valid():
            pandemicForm.save()
        return HttpResponseRedirect('admin-view-pandemic')
    return render(request,'vol/admin_add_pandemic.html',context=mydict)


@login_required(login_url='adminlogin')
def admin_view_pandemic_view(request):
    pandemics=models.Pandemic.objects.all()
    return render(request,'vol/admin_view_pandemic.html',{'pandemics':pandemics})

@login_required(login_url='adminlogin')
def delete_pandemic_view(request,pk):
    pandemic=models.Pandemic.objects.get(id=pk)
    
    pandemic.delete()
    return HttpResponseRedirect('/admin-view-pandemic')





@login_required(login_url='adminlogin')
def admin_work_view(request):
    return render(request,'vol/admin_work.html')


@login_required(login_url='adminlogin')
def admin_add_work_view(request):
    workForm=forms.WorkForm()
    mydict={'workForm':workForm}
    if request.method=='POST':
        workForm=forms.WorkForm(request.POST)
        
        if workForm.is_valid():

            work=workForm.save(commit=False)
            pandemic=models.Pandemic.objects.get(id=request.POST.get('pandemicId'))
            volunteer=models.Volunteer.objects.get(user_id=request.POST.get('volunteerId'))
            work.pandemic=pandemic
            work.volunteer=volunteer
            work.save()

        return HttpResponseRedirect('admin-view-work')
    return render(request,'vol/admin_add_work.html',context=mydict)


@login_required(login_url='adminlogin')
def admin_view_work_view(request):
    works=models.Work.objects.all()
    return render(request,'vol/admin_view_work.html',{'works':works})


@login_required(login_url='adminlogin')
def delete_work_view(request,pk):
    work=models.Work.objects.get(id=pk)
    
    work.delete()
    return HttpResponseRedirect('/admin-view-work')



@login_required(login_url='volunteerlogin')
@user_passes_test(is_volunteer)
def volunteer_dashboard_view(request):
    volunteer = models.Volunteer.objects.get(user_id=request.user.id)
    dict={ 
    'total_pandemic':models.Pandemic.objects.all().count(),
    'total_work':models.Work.objects.all().filter(volunteer=volunteer).count(),   
    }
    return render(request,'vol/volunteer_dashboard.html',context=dict)


@login_required(login_url='volunteerlogin')
@user_passes_test(is_volunteer)
def volunteer_work_view(request):
    return render(request,'vol/volunteer_work.html')


@login_required(login_url='volunteerlogin')
@user_passes_test(is_volunteer)
def volunteer_pandemic_view(request):
    pandemics=models.Pandemic.objects.all()
    return render(request,'vol/volunteer_view_pandemic.html',{'pandemics':pandemics})



@login_required(login_url='volunteerlogin')
@user_passes_test(is_volunteer)
def volunteer_view_work_view(request):
    volunteer = models.Volunteer.objects.get(user_id=request.user.id)
    works=models.Work.objects.all().filter(volunteer=volunteer)
    return render(request,'vol/volunteer_view_work.html',{'works':works})



@login_required(login_url='volunteerlogin')
@user_passes_test(is_volunteer)
def volunteer_apply_work_view(request):
    pandemics=models.Pandemic.objects.all()
    return render(request,'vol/volunteer_apply_work.html',{'pandemics':pandemics})


@login_required(login_url='volunteerlogin')
@user_passes_test(is_volunteer)
def apply_work_view(request,pk):
    pandemic=models.Pandemic.objects.get(id=pk)
    volunteer = models.Volunteer.objects.get(user_id=request.user.id)
    work=models.Work()
    work.pandemic=pandemic
    work.volunteer=volunteer
    work.save()
    return HttpResponseRedirect('/volunteer-view-work')






def aboutus_view(request):
    return render(request,'vol/aboutus.html')
from django.core.mail import send_mail
def contactus_view(request):
    sub = forms.ContactusForm()
    if request.method == 'POST':
        sub = forms.ContactusForm(request.POST)
        if sub.is_valid():
            email = sub.cleaned_data['Email']
            name=sub.cleaned_data['Name']
            message = sub.cleaned_data['Message']
            send_mail(str(name)+' || '+str(email),message,settings.EMAIL_HOST_USER, settings.EMAIL_RECEIVING_USER, fail_silently = False)
            return render(request, 'vol/contactussuccess.html')
    return render(request, 'vol/contactus.html', {'form':sub})