
from django.urls import path
from . import views
urlpatterns = [
    path('', views.endpoints, name='enpoint'),
    path('products/', views.ProductGetAndCreate.as_view(), name='products'),
    path('categories/', views.CategoryGetAndCreate.as_view(), name='category'),
]