"""First_form URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from mywork3 import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from django.conf.urls import url
from projectOne import views
from projectOne.views import localRoads_view
from projectOne.views import widthRequest_view
from projectOne.views import column_removal
from projectOne.views import local_Roads_Scope
from projectOne.views import costEstimations_view
from projectOne.views import offensive_removal
from projectOne.views import webApp
from projectOne.views import  dateApp
from projectOne.viewApps import tenderApp_view
from projectOne.viewApps import dieselApp_view



urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^localRoads/dataBase',views.localRoadsDataBase2,name='localRoadsDataBase'),
    url(r'^localRoads/View',localRoads_view,name='localRoadsRender'),
    url(r'^localRoads/widthRequest',widthRequest_view,name='widthRequest'),
    url(r'^localRoads/columnRemoval',column_removal,name='columnRemoval'),
    url(r'^localRoads/localRoadsScope',local_Roads_Scope,name='localRoadsScope'),
    url(r'^localRoads/costEstimations',costEstimations_view,name='cost_estimations'),
    url(r'^localRoads/offensiveRemoval',offensive_removal,name='offensive'),
    url(r'^webApplications',webApp,name='webApp'),
    url(r'^dateApp',dateApp,name='dateApp2'),
    url(r'^tenderApp',tenderApp_view,name='tenderAppUrl'),
    url(r'^dieselApp',dieselApp_view,name='dieselApp_url'),

]
