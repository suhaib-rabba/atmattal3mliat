
from django.contrib import admin
from django.urls import path
from apps import views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include


urlpatterns = [
    path('diesel/', views.diesel_view, name='diesel_asphalt'),
    path('tender_study_phase/', views.tender_study_view, name='tender_study_phase')
]
