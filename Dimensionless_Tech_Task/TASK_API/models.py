from django.db import models

class awsimage(models.Model):
    image_name = models.CharField(max_length=200)
    object_name = models.CharField(max_length=200)
    timestamp =  models.TimeField()
    Image = models.ImageField("images/")
    xml_file = models.FileField(blank=False, null=False)
