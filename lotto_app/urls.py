from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('buy/', views.buy),
    path('mypage/', views.mypage),
    path('result/<int:round_number>/', views.check_result),

    # 관리자 기능
    path('admin/draw/', views.admin_draw),
    path('admin/sales/', views.admin_sales),
]
