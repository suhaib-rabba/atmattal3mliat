
from django.contrib import admin
from django.urls import path
from apps import views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include


urlpatterns = [
    path('diesel/', views.diesel_view, name='diesel_asphalt'),
    path('tender_study_phase/', views.tender_study_view, name='tender_study_phase'),
    path('tender_date/', views.tender_date, name='tender_date'),
    path('tender_maintenance/', views.tender_maintenance,
         name='tender_maintenance_url'),
    path('tender_maintenanceRender/', views. tender_maintenanceTables,
         name='tender_maintenanceRender')

         ]
