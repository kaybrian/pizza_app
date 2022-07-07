from django.urls import path 
from . import views

urlpatterns = [
    path('orders/', views.HelloOrdersView.as_view(),name="auth"),
]
