from django.urls import path

from todo import views

urlpatterns = [
    path('',views.home,name='home'),

    path('addTask',views.addTask,name='addTask')

]
