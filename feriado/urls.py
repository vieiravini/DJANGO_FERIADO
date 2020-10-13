from django.urls import path
from . import views

urlpatterns = [    
    path('natal', views.natal),
    path('carnaval', views.carnaval),
    path('tiradentes', views.tiradentes),
]