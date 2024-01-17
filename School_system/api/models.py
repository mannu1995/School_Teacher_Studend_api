from django.db import models

# Create your models here.
class Teacher(models.Model):
    teacher_id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.IntegerField()
    subject=models.CharField(max_length=100,default=" ")
    address=models.TextField(max_length=2000)
    joining_date=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name 


class Student(models.Model):
    s_name = models.CharField(max_length=100)
    f_name = models.CharField(max_length=100)
    m_name = models.CharField(max_length=100)
    add = models.TextField(max_length=100)
    class_teacher=models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.s_name

