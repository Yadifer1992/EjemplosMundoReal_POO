# archivo: EjemplosMundoReal_POO/sistema_reservas.py

# Clase que representa una habitación en un hotel
class Habitacion:
    def __init__(self, numero, tipo, precio):
        # Número de habitación (ej: 101)
        self.numero = numero
        # Tipo de habitación (Individual, Doble, etc.)
        self.tipo = tipo
        # Precio por noche
        self.precio = precio
        # Estado de ocupación (False por defecto = disponible)
        self.ocupada = False

    # Método para marcar la habitación como reservada
    def reservar(self):
        self.ocupada = True

    # Método para liberar la habitación (quitar reserva)
    def liberar(self):
        self.ocupada = False

    # Representación en cadena del objeto
    def __str__(self):
        estado = "Ocupada" if self.ocupada else "Disponible"
        return f"Habitación {self.numero} - {self.tipo} - ${self.precio} - {estado}"

# Clase que representa un cliente del hotel
class Cliente:
    def __init__(self, nombre, cedula):
        self.nombre = nombre  # Nombre del cliente
        self.cedula = cedula  # Cédula del cliente

    def __str__(self):
        return f"{self.nombre} (Cédula: {self.cedula})"

# Clase que representa una reserva hecha por un cliente
class Reserva:
    def __init__(self, cliente, habitacion):
        self.cliente = cliente      # Objeto Cliente
        self.habitacion = habitacion  # Objeto Habitacion

    # Método para confirmar la reserva si la habitación está disponible
    def confirmar(self):
        if not self.habitacion.ocupada:
            self.habitacion.reservar()
            print(f"Reserva confirmada para {self.cliente} en {self.habitacion}")
        else:
            print(f"Error: La {self.habitacion} ya está ocupada.")

# ---------------------- PRUEBA DEL SISTEMA ----------------------

# Creamos una lista de habitaciones disponibles
habitaciones = [
    Habitacion(101, "Individual", 40),
    Habitacion(102, "Doble", 60),
    Habitacion(103, "Suite", 120)
]

# Creamos un cliente
cliente1 = Cliente("Yadira Ureña", "2200024194")

# El cliente hace una reserva de la habitación 101
reserva1 = Reserva(cliente1, habitaciones[0])
reserva1.confirmar()

# El cliente intenta reservar la misma habitación otra vez
reserva2 = Reserva(cliente1, habitaciones[0])
reserva2.confirmar()