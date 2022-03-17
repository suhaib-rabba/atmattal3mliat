from django.shortcuts import render
from .models import Applications
from .functions.tender_study_phase import Tender
from .functions.diesel_asphalt import Tamem

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
       year=request.POST.get('year')
       month=request.POST.get('month')
       test=request.POST.get('test')
       object=tamem(year,month)

       costRequest = getattr(object, test)

       context={"object":object,
        "costRequest":costRequest}
       return render(request,"apps/diesel_asphalt.html",context)
    else:
       return render(request,"apps/diesel_asphalt.html",{})


def tender_study_view(request):
    if request.method == "POST":
       cost = request.POST.get('cost')
       period = request.POST.get('period')
       object = Tender(cost, period)

       context = {"object": object}
       return render(request, 'apps/tender_study_phase.html', context)
    else:
       return render(request, 'apps/tender_study_phase.html', {})
