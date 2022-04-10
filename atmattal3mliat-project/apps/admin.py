from django.contrib import admin
from .models import Applications
from .models import Combustibles
from .models import date_app
# Register your models here.
admin.site.register(Applications)
admin.site.register(Combustibles)
admin.site.register(date_app)
