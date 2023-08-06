from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
    path('',views.home2,name='home2'),
    path('tweet/',views.home,name='home'),
    path('quiz/',views.quiz,name='quiz'),
    path('quiz2/',views.quiz,name='quiz2'),
    path('task/',views.task,name='task'),
    path('wheel/',views.wheel,name='wheel')
]