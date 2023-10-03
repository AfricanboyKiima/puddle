from django.urls import path
from . import views

#app_name = 'item'#this is a namespace for this app

urlpatterns = [
    path('<int:pk>/',views.detail, name='detail'),
]
#><