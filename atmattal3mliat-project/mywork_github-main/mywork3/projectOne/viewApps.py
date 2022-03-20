from django.shortcuts import render
from projectOne.form import localRoadsForm
from django.http import HttpResponseRedirect
from projectOne.models import localRoadsDataBase
from projectOne.static.functions_class import tender
from projectOne.static.functions_class import tamem



def tenderApp_view(request):

    if request.method == "POST":
       cost=request.POST.get('cost')
       period=request.POST.get('period')
       object=tender(cost,period)

       context={"object":object}
       return render(request,"projectOne/TenderApp.html",context)
    else:
       return render(request,"projectOne/TenderApp.html",{})



def dieselApp_view(request):
    if request.method == "POST":
       year=request.POST.get('year')
       month=request.POST.get('month')
       test=request.POST.get('test')
       object=tamem(year,month)

       costRequest = getattr(object, test)

       context={"object":object,
        "costRequest":costRequest}
       return render(request,"projectOne/dieselApp.html",context)
    else:
       return render(request,"projectOne/dieselApp.html",{})
