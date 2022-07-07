from django.urls import path 
from . import views

urlpatterns = [
    path('auth/', views.HelloAuthView.as_view(),name="auth"),
]
