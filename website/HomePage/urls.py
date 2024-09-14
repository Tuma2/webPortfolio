from django.urls import path
from  . import views

urlpatterns = [
    #Empty path directs us to the homepage
    path('', views.home, name='homepage'),
]
