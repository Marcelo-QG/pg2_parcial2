# Segundo Parcial - API REST para pedidos de comida rápida en conos

Materia: Programación II  
Estudiante: Carlos Marcelo Quispe Gonzales  
Curso: 2do Año - Sistemas Informáticos  
Fecha de entrega: 07/07/2025  

---

## Objetivo de la práctica

Desarrollar un proyecto Django que aplique los patrones de diseño Factory, Builder y Singleton en atributos calculados de un serializer en un API REST usando Django REST Framework. El sistema simula un módulo de pedidos de comida rápida basada en conos.

---

## Estructura del proyecto

- api_patrones/ – Proyecto principal de Django.
- api_conos/ – App donde se encuentra el modelo, lógica y patrones aplicados.
- env/ – Entorno virtual de Python.
- db.sqlite3 – Base de datos local.
- requirements.txt – Dependencias.

---

## Pasos realizados

### 1. Entorno virtual y dependencias

```bash
python -m venv env
.\env\Scripts\activate
pip install django djangorestframework django-extensions
```

### 2. Creación del proyecto y app
```bash
django-admin startproject api_patrones .
python manage.py startapp api_conos
```

### 3. Configuración de settings.py
```bash
INSTALLED_APPS = [
    ...
    'django_extensions',
    'rest_framework',
    'api_conos',
]
```
---
### Modelo PedidoCono
Ubicado en api_conos/models.py:
```bash
class PedidoCono(models.Model):
    cliente = models.CharField(max_length=100)
    variante = models.CharField(
        max_length=20,
        choices=[("carnivoro", "Carnívoro"), ("vegetariano", "Vegetariano"), ("saludable", "Saludable")],
    )
    toppings = models.JSONField(default=list)
    tamanio_cono = models.CharField(
        max_length=10,
        choices=[("pequenio", "Pequeño"), ("mediano", "Mediano"), ("grande", "Grande")],
    )
    fecha_pedido = models.DateField(auto_now_add=True)
```
---
### Patrones de diseño aplicados
#### Factory – ConoFactory
Archivo: api_conos/factory.py

- Se encarga de instanciar un objeto base ConoBase según el tipo de variante del pedido.

- Elimina la necesidad de múltiples condicionales en el serializador, encapsulando la lógica en una fábrica.

- Se utiliza en los métodos get_precio_final() y get_ingredientes_finales() del serializador.

#### Builder – ConoPersonalizadoBuilder + ConoDirector
Archivo: api_conos/builder.py

- Construye dinámicamente el pedido personalizado paso a paso.

- Suma los precios y crea una lista detallada de ingredientes finales.

- Se usa en los métodos del serializador para construir la estructura completa del cono.

#### Singleton – Logger
Archivo: api_patrones/logger.py

- Registra logs cada vez que se realiza el cálculo de precio o ingredientes finales.

- Garantiza que solo una instancia controle los registros de operaciones durante la ejecución del proyecto.
---

### Serializador personalizado
Archivo: api_conos/serializers.py:
```bash
class PedidoConoSerializer(serializers.ModelSerializer):
    precio_final = serializers.SerializerMethodField()
    ingredientes_finales = serializers.SerializerMethodField()

    def get_precio_final(self, obj):
        ...
        Logger().log(...)
        return resultado["precio_final"]

    def get_ingredientes_finales(self, obj):
        ...
        return resultado["ingredientes_finales"]
```
### API desarrollada
Endpoint base:
```bash
http://localhost:8000/api/pedidos_conos/
```
### JSON de ejemplo para POST:
```bash
{
  "cliente": "Marcelo",
  "variante": "carnivoro",
  "toppings": ["queso_extra", "papas_al_hilo"],
  "tamanio_cono": "grande"
}
```
### Respuesta esperada:
```bash
{
  "id": 1,
  "cliente": "Marcelo",
  "variante": "carnivoro",
  "toppings": ["queso_extra", "papas_al_hilo"],
  "tamanio_cono": "grande",
  "fecha_pedido": "2025-07-07",
  "precio_final": 22.5,
  "ingredientes_finales": ["Carnívoro", "queso_extra", "papas_al_hilo"]
}
```
### Cómo probar el proyecto
1. Activar el entorno:
```bash
.\env\Scripts\activate
```
2. Correr el servidor:
```bash
python manage.py runserver
```
3. Abrir en el navegador:
```bash
http://127.0.0.1:8000/api/pedidos_conos/
```
---
### Implementación de patrones

#### ¿Qué patrón se utilizó y por qué?

- Factory: para crear la base del cono dependiendo de la variante seleccionada.

- Builder: para ensamblar el pedido sumando toppings, tamaño y tipo de cono, y obtener ingredientes y precio final.

- Singleton: para llevar un registro de los pedidos y precios calculados a lo largo del uso del sistema.
#### ¿Dónde está implementado en el código?
```bash
api_conos/factory.py → clase ConoFactory

api_conos/builder.py → clases ConoPersonalizadoBuilder y ConoDirector

api_patrones/logger.py → clase Logger
```
#### ¿Cómo se prueba o evidencia su uso?

- Al enviar un POST al endpoint /api/pedidos_conos/, se utilizan los tres patrones en el cálculo de precio_final e ingredientes_finales.

- El uso del patrón Singleton se evidencia en el almacenamiento de logs de cada cálculo realizado.
### Capturas de pantalla
### Registro en el administrador de Django
![Admin Registro](Capturas_Pantalla/Registro%20en%20el%20administrador%20de%20Django.png)
### Respuesta de la API con atributos calculados
![API JSON](Capturas_Pantalla/Respuesta%20de%20la%20API%20con%20atributos%20calculados.png)