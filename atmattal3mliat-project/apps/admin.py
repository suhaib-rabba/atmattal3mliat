from django.contrib import admin
from .models import Applications
from .models import Combustibles
from .models import Date_app
# Register your models here.
admin.site.register(Applications)
admin.site.register(Combustibles)
admin.site.register(Date_app)
