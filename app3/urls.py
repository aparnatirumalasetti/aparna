from app3 import views
from django.urls import path
urlpatterns = [
path('fine/', views.fine,name='fine'),
path('nice/', views.nice,name='nice')
]
