"""atmattal3mliat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from apps import views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('accounts/', include('accounts.urls')),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('application/', include('apps.urls')),
    path('monthly_report/', views.monthly_report, name='reportInput'),
    path('monthly_reportRender/', views.monthly_reportRender, name='reportRender'),
    path('monthly_reportAutomation/', views.monthly_reportAutomation, name='reportAutomation'),
    path('questionnaire/',views.questionnaire_view, name='questionnaireUrl')


         ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#little change
# trail
