from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('submit_form/', views.submit_form, name='submit_form'),
    path('submit_modal/', views.submit_modal, name='submit_modal'),
]
