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
        #الاساسي
       year1 = request.POST.get('year1')
       month1 = request.POST.get('month1')
       #التنفيذ
      year2 = request.POST.get('year2')
      month2 = request.POST.get('month2')


       test = request.POST.get('item')

       object1 = Tamem(year1, month1)
       object2 = Tamem(year2, month2)
       if test=='diesel':
           costRequest_basic_diesel=object1.diesel()
           costRequest_final_diesel=object2.diesel()
       else:





       costRequest1 = getattr(object1, test)
       costRequest2_ = getattr(object2, test)



       context = {"object": object,
                  "costRequest": costRequest}
       return render(request, "apps/diesel_asphalt.html", context)
    else:
       return render(request, "apps/diesel_asphalt.html", {})


def tender_study_view(request):
    if request.method == "POST":
       cost = request.POST.get('cost')
       period = request.POST.get('period')
       object = Tender(cost, period)

       context = {"object": object}
       return render(request, 'apps/tender_study_phase.html', context)
    else:
       return render(request, 'apps/tender_study_phase.html', {})
