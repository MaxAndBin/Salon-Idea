"""Salon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from Salon import views


urlpatterns = [
    path('admin/', admin.site.urls),   
    url(r'^LifeEvents/$',views.lifeEvent_list),
    url(r'^SensorEvents/$',views.SensorEvent_list),
    url(r'^UserProfiles/$',views.Userprofile_list),
    url(r'^Devices/$',views.Device_list),
    url(r'^UserDevices/$',views.UserDevice_list),
    url(r'^Education/$',views.Education_list),
    url(r'^UserEducation/$',views.UserEducation_list),
    url(r'^Language/$',views.Language_list),
    url(r'^UserLanguage/$',views.UserLanguage_list),
    url(r'^Hobby/$',views.Hobby_list),
    url(r'^UserHobby/$',views.UserHobby_list),
    url(r'^Images/$',views.Image_list),
    url(r'^UserImages/$',views.UserImage_list),
    url(r'^Address/$',views.Address_list),
    url(r'^UserAddress/$',views.UserAddress_list)

    
]
