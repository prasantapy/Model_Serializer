from rest_framework import serializers
from .models import Student_model


 #validators

''' 
def start_with_s(value):
    if value[0]!='s':
        raise serializers.ValidationError('Name should be start only s')
    return value'''

class student_serializer(serializers.ModelSerializer):
    class Meta:
        model = Student_model
        fields=['name','roll','city']



   