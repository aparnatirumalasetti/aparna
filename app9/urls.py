from app9 import views
from django.urls import path

urlpatterns = [
path('market/', views.market,name='market'),
path('reg/', views.registration,name='reg'),
#path('regs/', views.regs,name='regs'),
path('login/', views.login,name='login'),
path('welcome/', views.welcome,name='welcome'),
path('logout/', views.logout,name='logout'),

]
