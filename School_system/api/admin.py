from django.contrib import admin
from api.models import Teacher,Student

# Register your models here.
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display=('teacher_id','name','subject')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=('s_name','f_name')    
