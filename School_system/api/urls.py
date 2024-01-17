from django.urls import path,include
from api.views import TeacherViewSet,StudentViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'teachers',TeacherViewSet)
router.register(r'students',StudentViewSet)



urlpatterns = [
    path('',include(router.urls) ) 

] 
  
