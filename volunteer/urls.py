"""volunteer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from vol import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view,name=''),

    path('adminclick', views.adminclick_view),
    path('volunteerclick', views.volunteerclick_view),
    path('volunteersignup', views.volunteer_signup_view,name='volunteersignup'),
   

    path('volunteerlogin', LoginView.as_view(template_name='vol/volunteerlogin.html'),name='volunteerlogin'),
    
    path('adminlogin', LoginView.as_view(template_name='vol/adminlogin.html'),name='adminlogin'),

    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),
    path('admin-volunteer', views.admin_volunteer_view,name='admin-volunteer'),

    path('admin-view-volunteer', views.admin_view_volunteer_view,name='admin-view-volunteer'),
    path('update-volunteer/<int:pk>', views.update_volunteer_view,name='update-volunteer'),
    path('delete-volunteer/<int:pk>', views.delete_volunteer_view,name='delete-volunteer'),

    path('admin-view-pending-volunteer', views.admin_view_pending_volunteer_view,name='admin-view-pending-volunteer'),
    path('approve-volunteer/<int:pk>', views.approve_volunteer_view,name='approve-volunteer'),
    path('reject-volunteer/<int:pk>', views.reject_volunteer_view,name='reject-volunteer'),

    path('admin-notification', views.admin_notification_view,name='admin-notification'),
    path('admin-add-pandemic', views.admin_add_pandemic_view,name='admin-add-pandemic'),
    path('admin-view-pandemic', views.admin_view_pandemic_view,name='admin-view-pandemic'),
    path('delete-pandemic/<int:pk>', views.delete_pandemic_view,name='delete-pandemic'),
    


    path('admin-work', views.admin_work_view,name='admin-work'),
    path('admin-add-work', views.admin_add_work_view,name='admin-add-work'),
    path('admin-view-work', views.admin_view_work_view,name='admin-view-work'),
    path('delete-work/<int:pk>', views.delete_work_view,name='delete-work'),
  




    path('volunteer-dashboard', views.volunteer_dashboard_view,name='volunteer-dashboard'),
    path('volunteer-work', views.volunteer_work_view,name='volunteer-work'),
    path('volunteer-apply-work', views.volunteer_apply_work_view,name='volunteer-apply-work'),
    path('apply-work/<int:pk>', views.apply_work_view,name='apply-work'),
    path('volunteer-view-work', views.volunteer_view_work_view,name='volunteer-view-work'),
    path('volunteer-pandemic', views.volunteer_pandemic_view,name='volunteer-pandemic'),



    path('logout', LogoutView.as_view(template_name='vol/logout.html'),name='logout'),
    path('aboutus', views.aboutus_view),
    path('contactus', views.contactus_view),
    path('afterlogin', views.afterlogin_view,name='afterlogin'),

]
