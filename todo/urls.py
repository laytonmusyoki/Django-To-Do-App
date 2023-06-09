from django.urls import path
from .views import*

urlpatterns=[
    path('show/',show,name='show'),
    path('createusers',Createuser,name='createuser'),
    path('update/<str:pk>/',update,name='update'),
    path('delete/<str:pk>/',delete,name='delete'),
    path('register/',register,name='register'),
    path('loginpage/',loginpage,name='loginpage'),
    path('logouturl/',logouturl,name='logouturl'),
    
]