
from django import forms

from rest_framework import serializers

from .models import Course

from django.contrib.auth.models import User

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('name', 'introduction', 'teacher', 'price')

class UserSerializer ( serializers.ModelSerializer ):
    class Meta:
        model = User
        fields = '__all__'

# class CourseSerializer(serializers.ModelSerializer):
#     teacher = serializers.CharField(source='teacher.username')  #外键字段 只读
#     class Meta:
#         model = Course
#         # exclude = ('id','name','introduction','teacher','price','create_at','update_at')
#         fields = '__all__'
#
class CourseSerializer(serializers.HyperlinkedModelSerializer):
    teacher = serializers.ReadOnlyField(source='teacher.username')
    class Meta:
        model = Course
        #url是默认值  可在setting是.py设置URL_FIELD_NAME是全局生效
        fields = ('name', 'introduction', 'teacher', 'price', 'create_at', 'update_at')
