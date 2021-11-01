from django.db import models

# Create your models here.
class Post(models.Model):
     title =models.CharField(max_length=100)
     slug = models.SlugField()
     first_name = models.CharField(max_length=100)
     last_name =models.CharField(max_length=100)
     email =models.CharField(max_length=100)
     phone_number = models.IntegerField()
     hire_date = models.DateField(null=True)
     job_id =models.CharField(max_length=100)
     salary =models.IntegerField()
     comission = models.IntegerField()
     body = models.TextField(max_length=255)
     thumb = models.ImageField(default='default.jpg', blank=True)


     def __str__(self):
          return self.title