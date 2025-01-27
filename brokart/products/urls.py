from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index,name='home'),
    path('Product_list',views.list_products,name='list_product')
     path('Product_detail',views.list_products,name='list_product')
]
