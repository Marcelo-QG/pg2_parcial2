from django.urls import path, include
from rest_framework import routers
from .views import PedidoConoViewSet

router = routers.DefaultRouter()
router.register(r"pedidos_conos", PedidoConoViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]
