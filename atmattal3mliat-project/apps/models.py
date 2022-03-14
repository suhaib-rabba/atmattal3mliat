from django.db import models
from django.contrib.auth.models import User

# Create your models here.


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
