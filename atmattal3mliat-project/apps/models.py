from django.db import models
from django.contrib.auth.models import User

from datetime import timedelta
# Create your models here.
from datetime import datetime
from django.utils import timezone


class Applications(models.Model):
    title = models.CharField(max_length=255)
    # pub_date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    url = models.TextField()
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    # votes_total = models.IntegerField(default=1)
    app_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def url_modified(self):
        a = "<h1> it is working {link}</h>".format(link=self.url)
        #{% autoescape off %}{{ app.url_modified }}{% endautoescape %}
        return a

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')


class Combustibles(models.Model):
    title = models.CharField(max_length=255)
    tamem_2019 = models.FileField(upload_to='combustibles/diesel/')
    tamem_2020 = models.FileField(upload_to='combustibles/diesel/')
    tamem_2021 = models.FileField(upload_to='combustibles/diesel/')
    tamem_2022 = models.FileField(upload_to='combustibles/diesel/')

    def __str__(self):
        return self.title


class Date_app(models.Model):
    tender_name = models.TextField()
    tender_number = models.TextField()
    concractor_name = models.TextField()

    maintenance_interval = models.IntegerField()
    date_work = models.DateField(
         default=datetime(2022, 11, 4, 0, 5, 23))
    date_maintenance = models.DateField(
         default=datetime(2022, 11, 4, 0, 5, 23))

    def date_start(self):
        a = [self.date_work.year, "/",
             self.date_work.month, "/", self.date_work.day]
        a = str(self.date_work.year)+"/" + \
            str(self.date_work.month) + \
            "/" + str(self.date_work.day)

        return a

    def date_end(self):
        a = ["/", self.date_maintenance.year,
             self.date_maintenance.month, self.date_maintenance.day]
        a = str(self.date_maintenance.year)+"/" + \
            str(self.date_maintenance.month) + \
            "/" + str(self.date_maintenance.day)
        return a

    def days_remain(self):
        intrval = self.date_maintenance-datetime.now().date()
        month = int((intrval.days)/30)
        days = intrval.days % 30

        interval = month*30+days
        month = str(month)
        days = str(days)
        return [month, days, interval]

    def days_remain2(self):
        intrval = self.date_maintenance-datetime.now().date()
        month = int((intrval.days)/30)
        days = intrval.days % 30
        return month*30 + days

    def __str__(self):
       return self.tender_name


class monthlyReportModel(models.Model):
    sector = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    date_work = models.DateField(
             default=datetime(2022, 11, 4, 0, 5, 23))
    month = models.IntegerField()
    year = models.IntegerField()
    code = models.IntegerField(default=1)

    year = models.IntegerField()
    area = models.CharField(max_length=255)
    work = models.TextField()
    photo = models.FileField(upload_to='monthlyReport/', blank=True)

    def __str__(self):
        return self.department+' ('+str(self.month)+")"



class QuestionnaireModel(models.Model):
    sector = models.CharField(max_length=255)
    institution=models.CharField(max_length=255)
    user = models.CharField(max_length=255)
    application= models.CharField(max_length=255)
    date_sumbmittion = models.DateField(
             default=datetime(2022, 11, 4, 0, 5, 23))
    speed=models.CharField(max_length=255)
    difficulty=models.CharField(max_length=255)
    usage = models.CharField(max_length=255)
    improvment=models.CharField(max_length=500)


    def __str__(self):
        return self.user+' ('+str(self.sector )+")"
