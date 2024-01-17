
from django.shortcuts import render
from api.models import Teacher,Student
from api.serializers import TeacherSerializer,StudentSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


# Create your views here.
class TeacherViewSet(viewsets.ModelViewSet):
    queryset =Teacher.objects.all()
    serializer_class=TeacherSerializer



    #teachers/{teacher_id}/students
    @action(detail=True,methods=['get'])
    def students(self,request,pk=None):
        teacher = Teacher.objects.get(pk=pk)
        stu = Student.objects.filter(class_teacher=teacher)
        stu_serializer=StudentSerializer(stu,many=True,context={'request':request})
        return Response(stu_serializer.data)



class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer    