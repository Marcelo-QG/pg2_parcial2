class ConoBase:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class ConoFactory:
    @staticmethod
    def crear_cono(variante):
        conos = {
            "carnivoro": ConoBase("Carnívoro", 15),
            "vegetariano": ConoBase("Vegetariano", 12),
            "saludable": ConoBase("Saludable", 10),
        }
        return conos.get(variante, ConoBase("Desconocido", 0))
