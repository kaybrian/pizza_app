from django.urls import path 
from . import views

urlpatterns = [
    path('',views.OrderCreateListView.as_view(),name="orders"),
    path('order/<str:order_id>/',views.OrderDetailView.as_view(),name="order_detail"),
    path('update-status/<str:order_id>/',views.updateOrderStatus.as_view(),name="update_order_status"),
    path('user/<str:user_id>/orders/',views.UserOrdersListView.as_view(),name="user_orders"),
    path('user/<str:user_id>/order/<str:order_id>/',views.UserOrderDetails.as_view(),name="user_order_detail")
]
