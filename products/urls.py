from django.urls.conf import path

from .views import ProductList, ProductDetail

app_name = 'products'

urlpatterns = [
    path('', ProductList.as_view(), name='list'),
    path('<slug>', ProductDetail.as_view(), name='detail'),

]
