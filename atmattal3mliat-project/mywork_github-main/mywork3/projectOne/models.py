from django.db import models
from django.forms.widgets import ClearableFileInput


class MyClearableFileInput(ClearableFileInput):
    initial_text = 'currently'
    input_text = 'change'
    clear_checkbox_label = 'clear'

class localRoadsDataBase(models.Model):
    citizenName=models.CharField(max_length=200)
    requestNumber=models.CharField(max_length=200)
    requestDate=models.CharField(max_length=200,blank=True, null=True)
    landNumber=	models.PositiveIntegerField()
    basinName=models.CharField(max_length=200)
    basinNumber=models.PositiveIntegerField()
    village_Choices=(
    ("مادبا","مادبا"),
    ("ماعين","ماعين"),
    ("الفحياء","الفيحاء"),
    ("الفيصلية","الفيصلية"),
    ("جرينة","جرينة"),
    ("الخطابية","الخطابية"),
    ("خربة الهلالية","خربة الهلالية"),
    ("الواحة","الواحة"),
    ("جبيل","جبيل"),
    ("خربة سطيحة","خربة سطيحة"),
    ("خربة حنينا","خربة حنينا"),
    ("كفير ابو خنينان الشريق","كفير ابو خنينان الشرقي"),
    )

    village=models.CharField( max_length=200,choices=village_Choices)

    roadLength=models.PositiveIntegerField(blank=True, null=True)
    roadWidth=models.PositiveIntegerField(blank=True, null=True)
    report_Choices=(
    (" يوجد تقرير مساح مرخص  "," يوجد تقرير مساح مرخص "),
    (" لا يوجد تقرير مساح مرخص    ",  " لا يوجد تقرير مساح مرخص "),
    )
    report=models.CharField(max_length=200,blank=True, null=True,choices=report_Choices)
    landSubgrade_Choices=(
    ("تربة حمراء","تربة حمراء"),
    ("صخرية","صخرية"),
    )
    landSubgrade=models.CharField(max_length=200,blank=True, null=True,choices=landSubgrade_Choices)
    heavyEquipment_Choices=(
    ("لودر","لودر"),
    ("جك همر","جك همر"),
    ("قلاب","قلاب"),
    ("جريدير","جريدر"),
    ("مدحلة + تنك مياه","مدحلة + تنك مياه"),)

    heavyEquipment=models.CharField(max_length=200,blank=True, null=True,choices=heavyEquipment_Choices)
    service_Choices=(
    ("بيوت","بيوت"),
    ("اراضي","اراضي"),
    ("مزارع","مزارع"),
    )
    service=models.CharField(max_length=100,blank=True,null=True,choices=service_Choices)
    tendiring_Choices=(
    ("الفرشيات","الفرشيات"),
    ("سيل كوت","سيل كوت"),
    ("تعبيد","تعبيد"),)


    tendiring=models.CharField(max_length=100,blank=True,null=True,choices=tendiring_Choices)
    currentLayer_Choices=(
    ("غير مفتوحة","غير مفتوحة"),
    ("طمم","طمم"),
    ("فرشيات","فرشيات"),
    ("سيل كوت متاكل_اعادة انشاء","سيل كوت متاكل_اعادة انشاء"),
    ("خلطة متاكلة_اعادة انشاء","خلطة متاكلة_اعادة انشاء"),
    )
    currentLayer=models.CharField(max_length=100,blank=True,null=True,choices=currentLayer_Choices)
    event=models.CharField(max_length=1000,blank=True,null=True)
    survy_report=models.FileField(upload_to="pdfFile/",blank=True,null=True)
    land_chart=models.FileField(upload_to="pdfFile/",blank=True,null=True )

    def __str__(self):
        return self.citizenName
