from django.shortcuts import render
from projectOne.form import localRoadsForm
from django.http import HttpResponseRedirect
from projectOne.models import localRoadsDataBase
import sys
from projectOne.static.functions import sum
from projectOne.static.columnRemoval import columnRemoval
from projectOne.static.road_width import widthRequest_function
from projectOne.static.Cost_estimations import seal_estimation
from projectOne.static.offensiveFunction import offensiveRemoval
from django.core.files.storage import FileSystemStorage
from projectOne.static.dateFunction import dateDifference
from projectOne.static.dateFunction import dateText


from subprocess import run,PIPE
def index(request):
    context={
    }
    return render(request,"projectOne/index.html",context)
def localRoadsDataBase2(request):

        if request.method == "POST":
            form=localRoadsForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/localRoads/dataBase/')
        else:
            form=localRoadsForm()
            context={'form':form}
            return render(request,"projectOne/localRoadsDataBase2.html",context)
#----------------------------------------------------------------------------------------
def localRoads_view(request):
 if request.method == "POST":
    inp=request.POST.get('citizenName')
    try:
        obj=localRoadsDataBase.objects.get(citizenName=inp)
    except:
        trail="<h1><a href=\"dataBase\"> ادخل معلومات الطريق </a></h1>"
        context={"trail":trail}
        return render(request,"projectOne/localRoads.html",context)

    try:
        survey_report=obj.survy_report.url
        land_chart=obj.land_chart.url
        respond_survey="طريق مساح مرخص "
        respond_land="مخطط اراضي "


    except:
        survey_report="#"
        land_chart="#"
        respond_land="الملف غير موجود  "
        respond_survey="الملف غير موجود  "



    context={
     "objects":obj,
     "survey_report":survey_report,
     "land_chart":land_chart,
     "respond_land":respond_land,
     "respond_survey":respond_survey

    }
    return render(request,"projectOne/localRoads.html",context)
 else:
     return render(request,"projectOne/localRoads.html",{})


#----------------------------------------------------------------------------------------
def widthRequest_view(request):
 if request.method == "POST":
    citizen=request.POST.get('citizenName')
    road_width=request.POST.get('width')
    try:
        obj=localRoadsDataBase.objects.get(citizenName=citizen)
    except:
        trail="<h1><a href=\"dataBase\"> ادخل معلومات الطريق </a></h1>"
        # trail="<h1><a href=\"{% url \'localRoadsDataBase\' %}\"> ادخل معلومات الطريق </a></h1>"

        context={"trail":trail}
        return render(request,"projectOne/widthRequest.html",context)

    citizen_request=obj.requestNumber
    request_date=obj.requestDate
    land_number=obj.landNumber
    basin_name=obj.basinName
    basin_number=obj.basinNumber
    area=obj.village
    road_length=obj.roadLength
    # road_width=obj.roadWidth
    Name=widthRequest_function(citizen,citizen_request,request_date,land_number,basin_name,basin_number
    ,area,road_length,road_width)
    context={"citizenName":Name}
    return render(request,"projectOne/widthRequest.html",context)
 else:
     return render(request,"projectOne/widthRequest.html",{})



#-------------------------------------------------------------------------------------
def column_removal(request):
 if request.method == "POST":
    citizen=request.POST.get('citizenName')
    try:
        obj=localRoadsDataBase.objects.get(citizenName=citizen)
    except:
        trail="<h1><a href=\"dataBase\"> ادخل معلومات الطريق </a></h1>"
        # trail="<h1><a href=\"{% url \'localRoadsDataBase\' %}\"> ادخل معلومات الطريق </a></h1>"

        context={"trail":trail}
        return render(request,"projectOne/columnRemoval.html",context)


    column_type=request.POST.get('column_type')
    column_number=request.POST.get('columnNumber')
    citizen_request=obj.requestNumber
    land_number=obj.landNumber
    basin_name=obj.basinName
    basin_number=obj.basinNumber
    area=obj.village
    road_length=obj.roadLength

    Name=columnRemoval(citizen,column_type,column_number,citizen_request,land_number,basin_name,basin_number
    ,area,road_length)
    context={"citizenName":Name}

    return render(request,"projectOne/columnRemoval.html",context)
 else:
     return render(request,"projectOne/columnRemoval.html",{})

#______________________________________________________________________________________________
def local_Roads_Scope(request):
    context={
    }
    return render(request,"projectOne/basinTamem.html",context)
#______________________________________________________________________________________________
def costEstimations_view(request):
 if request.method == "POST":
    citizen=request.POST.get('citizenName')
    ground_type=request.POST.get('layer_number')
    culvert_number=request.POST.get('culvert_number')
    culvert_diameter=request.POST.get('culvert_diameter')
    culvert_price=request.POST.get('culver_price')

    try:
        obj=localRoadsDataBase.objects.get(citizenName=citizen)
    except:
        trail="<h1><a href=\"dataBase\"> ادخل معلومات الطريق </a></h1>"
        # trail="<h1><a href=\"{% url \'localRoadsDataBase\' %}\"> ادخل معلومات الطريق </a></h1>"

        context={"trail":trail}
        return render(request,"projectOne/cost_estimations.html",context)

    citizen_request=obj.requestNumber
    request_date=obj.requestDate
    land_number=obj.landNumber
    basin_name=obj.basinName
    basin_number=obj.basinNumber
    area=obj.village
    road_length=obj.roadLength
#------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------


    Name=seal_estimation(road_length,ground_type,culvert_number,culvert_diameter,culvert_price,citizen,citizen_request,land_number,basin_name,basin_number,area)

    context={"citizenName":Name}
    return render(request,"projectOne/cost_estimations.html",context)
 else:
     return render(request,"projectOne/cost_estimations.html",{})

#----------------------------------------------------------------------------------------------------------------------------------------------
def offensive_removal(request):
 if request.method == "POST":
    citizen=request.POST.get('citizenName')
    offensive=request.POST.get('offensive')
    try:
        obj=localRoadsDataBase.objects.get(citizenName=citizen)
    except:
        trail="<h1><a href=\"dataBase\"> ادخل معلومات الطريق </a></h1>"
        # trail="<h1><a href=\"{% url \'localRoadsDataBase\' %}\"> ادخل معلومات الطريق </a></h1>"

        context={"trail":trail}
        return render(request,"projectOne/offensiveRemoval.html",context)


    citizen_request=obj.requestNumber
    land_number=obj.landNumber
    basin_name=obj.basinName
    basin_number=obj.basinNumber
    area=obj.village
    road_length=obj.roadLength

    Name=offensiveRemoval(road_length,citizen,citizen_request,land_number,basin_name,basin_number,area,offensive)
    context={"citizenName":Name}

    return render(request,"projectOne/offensiveRemoval.html",context)
 else:
     return render(request,"projectOne/offensiveRemoval.html",{})


#----------------------------------------------------------------------------------------------------------------------------------------------

def webApp(request):
    context={}
    return render(request,"projectOne/webApplications.html",context)
#-------------------------------------------------------------------------------------------------------------------------------------------------
def dateApp(request):
     if request.method == "POST":
        dateStart=request.POST.get('dateStart')
        dateEnd=request.POST.get('dateEnd')
        year1=int(request.POST.get('year1'))
        month1=int(request.POST.get('month1'))
        day1=int(request.POST.get('day1'))
        year2=int(request.POST.get('year2'))
        month2=int(request.POST.get('month2'))
        day2=int(request.POST.get('day2'))


        tenderPeriod=request.POST.get('tenderPeriod')
        periodOther=request.POST.get('periodOther')
        periodSemster=request.POST.get('periodSemster')


        from datetime import date
        #year=dateStart.split()[0]
        #month=dateStart.split()[1]
        #day=dateStart.split()[2]
        d0 = date(year1,month1,day1)
        d1 = date(year2,month2,day2)
        delta = d1 - d0
        function_date=dateText(delta,periodSemster,periodOther,tenderPeriod)
        delta=function_date[2]
        explanation=function_date[1]
        equation="المعادلة"
        if function_date[1]=='لا يوجد ايام تاخير':
            delays_title=""
            equal=""
        else:
            delays_title="عدد ايام التاخير"
            equal="="
        context={"delta":delta,
        "explanation":explanation,
        "equation":equation,
        "delays_title":delays_title,
        "equal":equal}
        return render(request,"projectOne/dateApp.html",context)
     else:
         return render(request,"projectOne/dateApp.html",{})

#----------------------------------------------------------------------------------------------------------------------------------------------










 # views.py
    # def file_view(request):
    #
    #     filename = '<path to your file>'
    #     data = open(filename, "rb").read()
    #     response = HttpResponse(data, content_type='application/vnd')
    #     response['Content-Length'] = os.path.getsize(filename)
    #
    #     return response
#----------------------------------------------------------------------------------------
    # inp=request.POST.get('param')
    # out=run([sys.executable,'C:\\Users\\suhaib rabba\\Desktop\\mywork_github\\mywork3\\projectOne\\test.py',inp],shell=False,stout=PIPE)
    # print(out)
