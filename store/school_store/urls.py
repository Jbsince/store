from django.urls import path
from . import views


urlpatterns=[
    path('',views.index,name='index'),

    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('purchase', views.purchase, name='purchase'),
    path('booking', views.booking, name='booking'),
    path('get_courses/', views.get_courses, name='get_courses')

]

