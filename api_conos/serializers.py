from rest_framework import serializers
from .models import PedidoCono
from .factory import ConoFactory
from .builder import ConoPersonalizadoBuilder, ConoDirector
from api_patrones.logger import Logger

class PedidoConoSerializer(serializers.ModelSerializer):
    precio_final = serializers.SerializerMethodField()
    ingredientes_finales = serializers.SerializerMethodField()

    class Meta:
        model = PedidoCono
        fields = "__all__"

    def get_precio_final(self, obj):
        base = ConoFactory.crear_cono(obj.variante)
        builder = ConoPersonalizadoBuilder()
        director = ConoDirector(builder)
        resultado = director.construir(base, obj.toppings, obj.tamanio_cono)
        Logger().log(f"{obj.cliente} pidió un {obj.variante} por {resultado['precio_final']} Bs.")
        return resultado["precio_final"]

    def get_ingredientes_finales(self, obj):
        base = ConoFactory.crear_cono(obj.variante)
        builder = ConoPersonalizadoBuilder()
        director = ConoDirector(builder)
        resultado = director.construir(base, obj.toppings, obj.tamanio_cono)
        return resultado["ingredientes_finales"]
