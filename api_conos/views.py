from rest_framework import viewsets
from .models import PedidoCono
from .serializers import PedidoConoSerializer

class PedidoConoViewSet(viewsets.ModelViewSet):
    queryset = PedidoCono.objects.all().order_by("-fecha_pedido")
    serializer_class = PedidoConoSerializer
