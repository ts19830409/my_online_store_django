from tkinter.font import names

from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import catalog, contacts, products_list, products_detail, product_add

app_name = CatalogConfig.name
urlpatterns = [
	path('catalog/', catalog, name='catalog'),
	path('contacts/', contacts, name='contacts'),
	path('', products_list, name='products_list'),
    path('products/<int:pk>/', products_detail, name='products_detail'),
	path('product_add/', product_add, name='product_add'),
]
