from django.shortcuts import render
from .models import Applications
from .functions.tender_study_phase import Tender
from .functions.diesel_asphalt import Tamem
from .models import Combustibles
from .functions.combustiblesFucntion import tamem_diesel_year
from .functions.dateFunction import dateDifference
from .functions.dateFunction import dateText
from operator import attrgetter
from dateutil.relativedelta import relativedelta
from datetime import date
from datetime import timedelta
import datetime
from . models import Date_app
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import monthlyReportModel

#--------------------------


def date_format(dateObject):
    date_3 = [dateObject.year, dateObject.month, dateObject.day]
    return date_3


#----------------------------
# Create your views here.


def home(request):
    applications = Applications.objects
    context = {'applications': applications}
    return render(request, 'apps/home.html', context)


def about(request):
    context = {}
    return render(request, 'general/about.html', context)


def contact(request):
    return render(request, 'general/contact.html')

    #------------------------------------


def diesel_view(request):
    if request.method == "POST":
        #الاساسي
       year1 = request.POST.get('year1')
       month1 = request.POST.get('month1')
       #التنفيذ
       year2 = request.POST.get('year2')
       month2 = request.POST.get('month2')

       test = request.POST.get('item')

       object1 = Tamem(year1, month1)
       object2 = Tamem(year2, month2)

       if test == "diesel":
           costRequest_basic_diesel = object1.diesel()
           costRequest_final_diesel = object2.diesel()
           diesel_tamem = Combustibles.objects.get(id=1)
           # tamem_base = tamem_diesel_year(year1, diesel_tamem)
           # tamem_final = tamem_diesel_year(year2, diesel_tamem)
          #
           call_base = "tamem_"+str(year1)
           call_final = "tamem_"+str(year2)
           tamem_base = getattr(diesel_tamem, call_base)
           tamem_final = getattr(diesel_tamem, call_final)
        #   tamem_base = diesel_tamem.tamem_2019
          # tamem_final = diesel_tamem.tamem_2020

           context = {"object": object,
                      "costRequest_basic_diesel": costRequest_basic_diesel,
                      "costRequest_final_diesel":  costRequest_final_diesel,
                      "test": test,
                      "tamem_base": tamem_base,
                      "tamem_final": tamem_final
                      }
           return render(request, "apps/diesel_asphalt.html", context)

       else:
           costRequest_basic_bitumen = object1.bitumen()
           costRequest_final_bitumen = object2.bitumen()
           costRequest_basic_fuel = object1.fuel()
           costRequest_final_fuel = object2.fuel
           butimen_oil_tamem = Combustibles.objects.get(title="butiment_fuel")
           call_base = "tamem_"+str(year1)
           call_final = "tamem_"+str(year2)
           tamem_base = getattr(butimen_oil_tamem, call_base)
           tamem_final = getattr(butimen_oil_tamem, call_final)

           context = {"object": object,
                      "costRequest_basic_bitumen": costRequest_basic_bitumen,
                      "costRequest_final_bitumen":  costRequest_final_bitumen,
                      "costRequest_basic_fuel": costRequest_basic_fuel,
                      "costRequest_final_fuel": costRequest_final_fuel,
                      "test": test,
                      "tamem_base": tamem_base,
                      "tamem_final": tamem_final
                      }
           return render(request, "apps/diesel_asphalt.html", context)

    else:
        context = {}
        return render(request, "apps/diesel_asphalt.html", context)

        return render(request, "apps/diesel_asphalt.html", {})

#note


def tender_study_view(request):
    if request.method == "POST":
       cost = request.POST.get('cost')
       period = request.POST.get('period')
       object = Tender(cost, period)

       context = {"object": object}
       return render(request, 'apps/tender_study_phase.html', context)
    else:
       return render(request, 'apps/tender_study_phase.html', {})
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------


def tender_date(request):
    if request.method == "POST":
        #------     امر المباشرة ------
        year1 = int(request.POST.get('year1'))
        month1 = int(request.POST.get('month1'))
        day1 = int(request.POST.get('day1'))
       #------     تاريخ انهاء الاعمال ------
        year2 = int(request.POST.get('year2'))
        month2 = int(request.POST.get('month2'))
        day2 = int(request.POST.get('day2'))
        #--------------------------------
        tenderPeriod = request.POST.get('tenderPeriod')
        periodOther = request.POST.get('periodOther')
        periodSemster = request.POST.get('periodSemster')

        from datetime import date
        #year=dateStart.split()[0]
        #month=dateStart.split()[1]
        #day=dateStart.split()[2]
        d0 = date(year1, month1, day1)
        d1 = date(year2, month2, day2)
        delta = d1 - d0
        actualPeriod = delta.days+1

        try:
            periodOther = int(periodOther)
        except:
            periodOther = 0

        try:
            periodSemster = int(periodSemster)
        except:
            periodSemster = 0

        extendsSummation = int(periodOther) + int(periodSemster)
        delays = actualPeriod-int(tenderPeriod)-extendsSummation
        if delays <= 0:
            delays = "لا يوجد ايام تاخير"
        context = {"delays": delays,
                   "actualPeriod": actualPeriod,
                   "extendsSummation": extendsSummation,
                   "tenderPeriod": tenderPeriod}
        return render(request, 'apps/tender_date_measure.html', context)
    else:
        return render(request, 'apps/tender_date_measure.html', {})

#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------


@login_required()
def tender_maintenance(request):

    if request.method == "POST":
        #---------------------- تاريخ انهاء الاعمال
        year1 = int(request.POST.get('year1'))
        month1 = int(request.POST.get('month1'))
        day1 = int(request.POST.get('day1'))
        date_finish = datetime.datetime(year1, month1, day1)
        maintenance_interval = int(request.POST.get('interval'))
        interval_year = int(maintenance_interval/12)
        interval_month = int(maintenance_interval % 12)
        date_maintenance = date_finish + \
            relativedelta(years=interval_year, months=interval_month)

        b = Date_app()
        #-------------------------------------------------
        b.tender_name = request.POST.get('tender_name')
        b.tender_number = request.POST.get('tender_number')
        b.concractor_name = request.POST.get('concractor')
        b.maintenance_interval = int(request.POST.get('interval'))
        b.date_work = date_finish
        b.date_maintenance = date_maintenance
        #-------------------------------------------------
        b.save()
        objects = Date_app.objects
        context = {"objects": objects}

        #date_finish = date(year1, month1, day1)

        return render(request, 'apps/tender_maintenanceRender.html', context)
    else:
        return render(request, 'apps/tender_maintenanceInput.html', {})


def tender_maintenanceTables(request):
    a = request.user
    objects = Date_app.objects.all()
    objects_list = []

    objects_list = list(objects)
    objects_list = sorted(objects_list, key=lambda x: x.days_remain2())
    #sort(key=lambda x: x.days_remain2())

    context = {"objects": objects,
               "objects_list": objects_list}
    return render(request, 'apps/tender_maintenanceRender.html', context)

    #---------------------------------------------------------------------------


def monthly_report(request):
    if request.method == "POST":
        #--------------------------------
        year1 = int(request.POST.get('year1'))
        month1 = int(request.POST.get('month1'))
        day1 = int(request.POST.get('day1'))
        date_work = datetime.datetime(year1, month1, day1)
        #---------------------------------
        model = monthlyReportModel()
        model.sector = request.POST.get('office')
        model.department = request.POST.get('department')
        model.date_work = date_work
        model.image = request.POST.get('workImage')
        model.area = request.POST.get('area')
        model.work = request.POST.get('workDescription')
        model.save()
        context = {}
        return render(request, 'monthlyReport/monthlyReportInput.html', context)

    else:
        context = {}
        return render(request, 'monthlyReport/monthlyReportInput.html', context)
