from django.db import models
from django.contrib.auth.models import User
from datetime import date

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


class date_app(models.Model):
    tender_name = models.TextField()
    tender_number = models.TextField()
    maintenance_interval = models.PositiveIntegerField()
    date_finish = models.DateField(
         default=datetime(2022, 11, 4, 0, 5, 23))
    days_remaning = models.PositiveIntegerField()
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
#auto_now_add=True,, null=True, blank=True

    def __str__(self):
        return self.tender_name
