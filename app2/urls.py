from app2 import views
from django.urls import path
urlpatterns = [
path('need/', views.need,name='need'),
path('wow/', views.wow,name='wow')
]
