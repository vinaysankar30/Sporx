from django.db import models


class organization(models.Model):
    org_name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images')
    room_id = models.IntegerField(primary_key=True)
