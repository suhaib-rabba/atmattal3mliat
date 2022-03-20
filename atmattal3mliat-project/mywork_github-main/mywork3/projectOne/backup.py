
# 
# def localRoads_view(request):



 # submitbutton= request.POST.get('submit')
 # firstname=''
 # lastname=''
 # emailvalue=''
 #
 # form= localRoadsForm(request.POST or None)
 # if form.is_valid():
 #    firstname= form.cleaned_data.get("first_name")
 #    lastname= form.cleaned_data.get("last_name")
 #    emailvalue= form.cleaned_data.get("email")
 #
 #
 # context= {'form': form, 'firstname': firstname, 'lastname':lastname,
 #          'submitbutton': submitbutton, 'emailvalue':emailvalue}
 #
 # return render(request, "projectOne/localRoads.html", context)









# if request.method == "POST":
#   form=localRoadsForm(request.POST)
#   if form.is_valid():
#     Name=form.citizenName
#     obj=localRoadsDataBase.objects.get(citizenName=Name)
#     context={
#       "objects":obj,}
#     return render(request,"projectOne/localRoads.html",context)
# else:
#     form=localRoadsForm()
# context={'form':form}
# return render(request,"projectOne/localRoads.html",context)

#
#
#
#     obj=localRoadsDataBase.objects.get(id='7')
#     context={
#      "objects":obj,
#     }
#     return render(request,"projectOne/localRoads.html",context)
# -------------------------------------------------------------------------
