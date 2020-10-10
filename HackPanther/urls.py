from django.urls import path, include
from . import views
 
urlpatterns = [
    path('',  views.index, name="Index"),
    path('health/',  views.health, name="Health"),
]
