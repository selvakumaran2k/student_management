from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.base,name='base'),
    path('mark',views.marking,name='mark'),
    path('attendence_submit',views.attendence_submit,name='attendence_submit')
]