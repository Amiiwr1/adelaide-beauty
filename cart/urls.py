from django.urls.conf import path

from .views import CartDetail, CartUpdate

app_name = 'cart'

urlpatterns = [
    path('', CartDetail.as_view(), name='detail'),
    path('<int:pk>/update/', CartUpdate.as_view(), name='update')

]
