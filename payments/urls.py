from django.urls import path

from . import views

urlpatterns = [
      path('', views.payments, name='payments'),
      path('create_payment/', views.create_payment, name='create-payment'),
]