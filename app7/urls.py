from app7 import views
from django.urls import path

urlpatterns = [
path('eformget/', views.eformget,name='eformget')
]
