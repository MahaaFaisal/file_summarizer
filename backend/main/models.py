from django.db import models
from rest_framework_api_key.models import APIKey
# Create your models here.

# ./manage.py migrate --database=requests
# I also need to specify that this model goes to requests db not default
class requests_table(models.Model):
    user = models.ForeignKey(
        APIKey,
        on_delete=models.SET_NULL,
        null=True)
    content = models.TextField()
    summary = models.TextField()
    age = models.IntegerField()
    gender = models.CharField(max_length=6)
    request_date = models.DateTimeField(auto_now=True)

