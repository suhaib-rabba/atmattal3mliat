from django.forms import ModelForm
from projectOne.models import localRoadsDataBase
from django import forms
from django.forms import MultipleChoiceField, ChoiceField, Form
from django.forms.widgets import ClearableFileInput


class MyClearableFileInput(ClearableFileInput):
    initial_text = 'currently'
    input_text = 'change'
    clear_checkbox_label = 'clear'

class localRoadsForm(ModelForm):
    class Meta:
        model=localRoadsDataBase
        fields='__all__'



        widgets={
        'citizenName':forms.TextInput(attrs={'placeholder':"ادخل اسم المواطن"}),
        'requestNumber':forms.TextInput(attrs={'placeholder':"رقم الطلب"}),
        'requestDate':forms.TextInput(attrs={'placeholder':"تاريخ تقديم الطلب"}),
        'landNumber':forms.TextInput(attrs={'placeholder':"رقم القطعة"}),
        'basinName':forms.TextInput(attrs={'placeholder':"اسم الحوض"}),
        'basinNumber':forms.TextInput(attrs={'placeholder':"رقم الحوض "}),
        'village':forms.Select(attrs={'style': 'font-size: 20px'}),
        'roadLength':forms.TextInput(attrs={'placeholder':"طول الطريق "}),
        'roadWidth':forms.TextInput(attrs={'placeholder':"عرض الطريق"}),
        'report':forms.Select(attrs={'placeholder':"تقرير مساح مرخص" ,'style': 'font-size: 20px' }),
        'landSubgrade':forms.Select(attrs={'placeholder':"الارضية",'style': 'font-size: 20px'}),
        'heavyEquipment':forms.Select(attrs={'placeholder':"الالية",'style': 'font-size: 20px',}),
        "service":forms.Select(attrs={'style': 'font-size: 20px',}),
        "currentLayer":forms.Select(attrs={'style': 'font-size: 20px',}),
        "tendiring"  :forms.Select(attrs={'style': 'font-size: 20px',}),
        "event":forms.TextInput(attrs={'placeholder':"ملاحظات",'style': 'font-size: 20px',}),
        }
        labels = {
            'survy_report': 'Input your X value here',
            'land_chart': 'Select your Y value here',
        }
        # ClearableFileInput
# 'class':'form-control',
#
#
