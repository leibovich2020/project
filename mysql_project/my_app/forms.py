from django import forms
from . import models

class CreateArticle(forms.ModelForm):
    class Meta:
        model = models.Post
        fields =['title','slug','first_name','last_name','email','hire_date','phone_number','job_id','salary','comission','body','thumb']