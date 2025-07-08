class ConoPersonalizadoBuilder:
    def __init__(self):
        self.ingredientes = []
        self.precio = 0

    def agregar_base(self, base):
        self.ingredientes.append(base.nombre)
        self.precio += base.precio

    def agregar_toppings(self, toppings):
        precios = {
            "queso_extra": 2,
            "papas_al_hilo": 1.5,
            "salchicha_extra": 3,
            "mayonesa": 0.5
        }
        for t in toppings:
            self.ingredientes.append(t)
            self.precio += precios.get(t, 0)

    def set_tamanio(self, tamanio):
        if tamanio == "mediano":
            self.precio += 2
        elif tamanio == "grande":
            self.precio += 4

    def get_cono(self):
        return {
            "ingredientes_finales": self.ingredientes,
            "precio_final": self.precio
        }

class ConoDirector:
    def __init__(self, builder):
        self.builder = builder

    def construir(self, base, toppings, tamanio):
        self.builder.agregar_base(base)
        self.builder.agregar_toppings(toppings)
        self.builder.set_tamanio(tamanio)
        return self.builder.get_cono()
