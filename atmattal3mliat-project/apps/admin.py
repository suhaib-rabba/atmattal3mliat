from django.contrib import admin
from .models import Applications
from .models import Combustibles
from .models import Date_app
from .models import monthlyReportModel
from .models import  QuestionnaireModel
# Register your models here.
admin.site.register(Applications)
admin.site.register(Combustibles)
admin.site.register(Date_app)
admin.site.register(monthlyReportModel)
admin.site.register(QuestionnaireModel)
