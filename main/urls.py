from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),               # головна сторінка
    path('submit_form/', views.submit_form, name='submit_form'),   # форма консультації
    path('submit_modal/', views.submit_modal, name='submit_modal'), # модальне вікно
]
