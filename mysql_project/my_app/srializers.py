from rest_framework import serializers
from .models import Post
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','title', 'slug', 'first_name', 'last_name', 'email', 'hire_date', 'phone_number', 'job_id', 'salary','comission', 'body', 'thumb']