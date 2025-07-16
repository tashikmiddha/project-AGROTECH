from django.contrib import admin
from django.urls import path,include
from project import views
urlpatterns = [
    path('',views.home,name='home'),
    path('home/',views.home,name='home'),
    path('team/',views.team,name='team'),
    path('term/',views.term,name='term'),
    path('datasets/',views.datasets,name='datasets'),
    path('code/',views.code,name='code'),
    path('crop_prediction/', views.crop_predict_view, name='crop_predict_view'),
    path('watering/', views.watering, name='watering'),
    path('contact/',views.contact,name='contact'),
    path('fertilizer_prediction/',views.fertilizer_prediction,name='fertilizer_prediction'),
]