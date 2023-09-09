from django.urls import path

from . import views

app_name = 'hw_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('customer/<int:pk>/', views.CustomerView.as_view(), name='customer_page'),
    path('product/<int:pk>/', views.ProductView.as_view(), name='product_page'),
    path('update_product/<int:pk>/', views.UpdateProductView.as_view(), name='update_product'),
    path('orders/year/<int:year>/<int:pk>/', views.AllYearProducts.as_view(), name='yearly_orders'),
    path('orders/monthly/<int:year>/<int:month>/<int:pk>/', views.AllMonthProducts.as_view(), name='monthly_orders'),
    path('orders/week/<int:year>/<int:week>/<int:pk>/', views.AllWeekProducts.as_view(), name='weekly_orders'),
]
