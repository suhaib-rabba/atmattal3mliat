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
from .models import QuestionnaireModel
import operator

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
       # test = request.POST.get('item')
       object1 = Tamem(year1, month1)

       costRequest_basic_diesel = object1.diesel()
       diesel_tamem = Combustibles.objects.get(id=1)

       call_base = "tamem_"+str(year1)
       tamem_base = getattr(diesel_tamem, call_base)

       costRequest_basic_bitumen = object1.bitumen()
       costRequest_basic_fuel = object1.fuel()
       butimen_oil_tamem = Combustibles.objects.get(title="butiment_fuel")
       call_base = "tamem_"+str(year1)
       tamem_base_asphaltFuel = getattr(butimen_oil_tamem, call_base)

       context = {
                  "costRequest_basic_diesel": costRequest_basic_diesel,
                  "tamem_base": tamem_base,
                  "costRequest_basic_bitumen": costRequest_basic_bitumen,
                  "costRequest_basic_fuel": costRequest_basic_fuel,
                  "tamem_base_asphaltFuel": tamem_base_asphaltFuel,
                  "month": month1, }
       return render(request, "apps/diesel_asphalt.html", context)

    else:
        context = {}
        return render(request, "apps/diesel_asphalt.html", context)


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
        doc = request.FILES
        model.photo = doc['docfile']
        model.area = request.POST.get('area')
        model.work = request.POST.get('workDescription')
        model.month = month1
        model.year = year1
        model.code = len(request.POST.get('department'))
        model.save()
        responed = "تم الادخال بنجاح"
        context = {'success': responed}
        return render(request, 'monthlyReport/monthlyReportInput.html', context)

    else:
        context = {}
        return render(request, 'monthlyReport/monthlyReportInput.html', context)


def monthly_reportRender(request):
    objects = monthlyReportModel.objects.all()
    objects = list(objects)

    def length(x):
        return len(x.department)
    objects = sorted(objects, key=lambda x: x.code)
    objects = list(filter(lambda x: x.month == 7, objects))

    trail = []
    for object in objects:
        trail.append(object.photo.url)

    context = {"objects": objects, 'trail': trail}
    return render(request, 'monthlyReport/monthlyReportRender.html', context)


def monthly_reportAutomation(request):
    objects = monthlyReportModel.objects.all()
    objects = list(objects)

    def length(x):
        return len(x.department)
    objects = sorted(objects, key=lambda x: x.code)
    objects = list(filter(lambda x: x.month == 7, objects))
    src = []
    department_list = []
    sector_list = []
    work_list = []
    for object in objects:
        src.append(object.photo.url)
    for object in objects:
        department_list.append(object.department)
    for object in objects:
        sector_list.append(object.sector)
    for object in objects:
        work_list.append(object.work)
    context = {"src": src, 'department_list': department_list,
               "sector_list": sector_list, 'work_list': work_list}

    return render(request, 'monthlyReport/monthlyReportAutomation.html', context)


def questionnaire_view(request):
        if request.method == "POST":
            #--------------------------------
            #---------------------------------
            model =QuestionnaireModel()

            model.sector =request.POST.get('sector')
            model.institution=request.POST.get('institution')
            model.user = request.POST.get('user')
            model.application= request.POST.get('application')
            model.date_sumbmittion =datetime.datetime.now()
            model.speed=request.POST.get('speed')
            model.difficulty=request.POST.get('difficulty')
            model.usage = request.POST.get('usage')
            model.improvment=request.POST.get('improvment')

            model.save()
            responed = "تم الادخال بنجاح"
            context = {'success': responed}
            return render(request, 'general/questionnaire.html', context)

        else:
            context = {}
            return render(request, 'general/questionnaire.html', context)
