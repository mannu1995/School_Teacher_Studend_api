from rest_framework import serializers
from api.models import Teacher,Student

class TeacherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Teacher
        fields="__all__"
        
class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields ='__all__'        