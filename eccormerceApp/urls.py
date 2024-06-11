
from django.urls import path
from . import views
urlpatterns = [
    path('', views.endpoints, name='enpoint'),
    path('products/', views.ProductGetAndCreate.as_view(), name='products'),
    path('products/update/<str:pk>/', views.ProductGetANDUpdate.as_view(), name='products'),
    path('categories/', views.CategoryGetAndCreate.as_view(), name='category'),
    path('orderItems/', views.OderItemGetAndCreate.as_view(), name='orderItems'),
    path('orders/', views.OderGetAndCreate.as_view(), name='orderItems'),
]