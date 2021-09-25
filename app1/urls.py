from app1 import views
from django.urls import path

urlpatterns = [
path('super/', views.super,name='super'),
path('joker/', views.joker,name='super'),
path('tommy/', views.tommy,name='good'),
path('world/',views.world,name='worlds'),
path('fly/',views.fly,name='fly'),
path('flower/',views.flower,name='flow'),
path('plant/',views.plant,name='plan'),
path('root/',views.root,name='root'),
path('Postf/',views.Postf,name='Postf')

]
