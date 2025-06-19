# archivo: EjemplosMundoReal_POO/tienda_productos.py

# Clase que representa un producto disponible en la tienda
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre  # Nombre del producto (ej: Laptop)
        self.precio = precio  # Precio del producto en dólares

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"

# Clase que representa el carrito de compras del cliente
class CarritoCompra:
    def __init__(self):
        # Lista donde se guardan los productos agregados al carrito
        self.productos = []

    # Método para agregar un producto al carrito
    def agregar_producto(self, producto):
        self.productos.append(producto)
        print(f"Agregado: {producto}")

    # Método para calcular el total de la compra
    def total(self):
        return sum(p.precio for p in self.productos)

    # Método para mostrar todos los productos del carrito
    def mostrar_carrito(self):
        print("\nCarrito de Compras:")
        for p in self.productos:
            print(f"- {p}")
        print(f"Total: ${self.total()}")

# ---------------------- PRUEBA DEL SISTEMA ----------------------

# Creamos algunos productos
p1 = Producto("Laptop", 1200)
p2 = Producto("Mouse", 25)
p3 = Producto("Teclado", 45)

# Creamos un carrito de compras
carrito = CarritoCompra()

# Agregamos productos al carrito
carrito.agregar_producto(p1)
carrito.agregar_producto(p2)
carrito.agregar_producto(p3)

# Mostramos el contenido del carrito y el total
carrito.mostrar_carrito()