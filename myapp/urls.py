"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from myapp.views import *

urlpatterns = [
    path('test', test.as_view()),

    path('bed/', bed_view.as_view()),
    path('bed/<int:id>/', bed_view.as_view()),

    path('ipd/', ipd_view.as_view()),
    path('ipd/<int:id>/', ipd_view.as_view()),
    path('ipd/bed_id/<int:bed_id>/', ipd_view.as_view()),

    path('scalp/', scalp_view.as_view()),
    path('scalp/<int:id>/', scalp_view.as_view()),

    path('complaint/', complaint_view.as_view()),
    path('complaint/<int:id>/', complaint_view.as_view()),
    
    path('past_history/', past_history_view.as_view()),
    path('past_history/<int:id>/', past_history_view.as_view()),
    
    path('personal_ho/', personal_H_O_view.as_view()),
    path('personal_ho/<int:id>/', personal_H_O_view.as_view()),

    path('fc/', fc_view.as_view()),
    path('fc/<int:id>/', fc_view.as_view()),

    path('admin_login/', admin_login_view.as_view()),
    path('admin_login/<int:id>/', admin_login_view.as_view()),
    path('admin_login/<str:email>/', admin_login_view.as_view()),

    path('service/', Service_view.as_view()),
    path('service/<int:id>/', Service_view.as_view()),
    
    path('specialization/', Specialization_view.as_view()),
    path('specialization/<int:id>/', Specialization_view.as_view()),
    
    path('doctor/', Doctor_view.as_view()),
    path('doctor/<int:id>/', Doctor_view.as_view()),

    path('opd/', OPD_view.as_view()),
    path('opd/<int:id>/', OPD_view.as_view()),
    path('opd/doctor/<int:doctor_id>/', OPD_view.as_view()),

    

]
