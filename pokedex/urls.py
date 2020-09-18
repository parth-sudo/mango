from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('guess/', views.Guesser, name = 'guess'),
    path('result/', views.result, name = 'result'),
    path('regions/', views.regions, name='regions'),
    path('studs/', views.studs, name = 'studs'),
    path('search/', views.search, name='search'),

]
