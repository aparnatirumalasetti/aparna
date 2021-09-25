from app6 import views
from django.urls import path

urlpatterns = [
path('eform/', views.eform,name='eform'),
path('eall/', views.eall,name='eall'),
path('hello/', views.hello,name='hello'),
path('eformget,<a>/', views.eformget,name='eformget'),
path('eformupdate,<a>/', views.eformupdate,name='eformupdate'),
path('eformdelete,<t>/', views.eformdelete,name='eformdelete'),


]
