from django.urls import path
from . import views
urlpatterns = [
    path('products/',views.ProductsListAPIView.as_view(),name='products'),
    path('products/info/',views.ProductInfoAPIView.as_view(),name='products_info'),
    path('products/<int:product_id>',views.ProductDetailAPIView.as_view(),name='product'),
    path('orders/',views.OrdersListAPIView.as_view(),name='orders'),
    path('user-orders/',views.UserOrdersListAPIView.as_view(),name='userorders'),
]

