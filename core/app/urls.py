from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'customer',views.CustomerViewSet,basename = 'customer')
router.register(r'order-model',views.OrderModelViewSet,basename = 'order-model')
router.register(r'product',views.ProductViewSet,basename = 'product')
router.register(r'product-model',views.ProductModelViewSet,basename = 'product-model')

urlpatterns = [
   path('',include(router.urls))
]