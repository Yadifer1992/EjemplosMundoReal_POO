# archivo: EjemplosMundoReal_POO/sistema_reservas.py

class Habitacion:
    """Representa una habitación de hotel."""

    def __init__(self, numero, tipo, precio):
        """
        Inicializa una habitación.
        :param numero: Número de la habitación.
        :param tipo: Tipo de habitación (Individual, Doble, etc.).
        :param precio: Precio por noche.
        """
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.ocupada = False  # Por defecto, la habitación está disponible

    def reservar(self):
        """Marca la habitación como ocupada."""
        self.ocupada = True

    def liberar(self):
        """Libera la habitación (la deja disponible)."""
        self.ocupada = False

    def __str__(self):
        estado = "Ocupada" if self.ocupada else "Disponible"
        return f"Habitación {self.numero} - {self.tipo} - ${self.precio} - {estado}"


class Cliente:
    """Representa un cliente del hotel."""

    def __init__(self, nombre, cedula):
        """
        Inicializa un cliente.
        :param nombre: Nombre completo.
        :param cedula: Cédula de identidad.
        """
        self.nombre = nombre
        self.cedula = cedula

    def __str__(self):
        return f"{self.nombre} (Cédula: {self.cedula})"


class Reserva:
    """Representa una reserva realizada por un cliente."""

    def __init__(self, cliente, habitacion):
        """
        Crea una nueva reserva.
        :param cliente: Objeto Cliente.
        :param habitacion: Objeto Habitacion.
        """
        self.cliente = cliente
        self.habitacion = habitacion

    def confirmar(self):
        """Confirma la reserva si la habitación está disponible."""
        if not self.habitacion.ocupada:
            self.habitacion.reservar()
            print(f"✅ Reserva confirmada para {self.cliente} en {self.habitacion}")
        else:
            print(f"❌ Error: La {self.habitacion} ya está ocupada.")

    def cancelar(self):
        """Cancela la reserva y libera la habitación."""
        if self.habitacion.ocupada:
            self.habitacion.liberar()
            print(f"❌ Reserva cancelada para {self.cliente} en {self.habitacion}")
        else:
            print(f"La habitación {self.habitacion.numero} ya estaba libre.")


def mostrar_habitaciones(lista):
    """Muestra todas las habitaciones y su estado actual."""
    print("\n📋 Estado actual de las habitaciones:")
    for h in lista:
        print(" -", h)


# ---------------------- PRUEBA DEL SISTEMA ----------------------

# Lista de habitaciones
habitaciones = [
    Habitacion(101, "Individual", 40),
    Habitacion(102, "Doble", 60),
    Habitacion(103, "Suite", 120)
]

# Cliente
cliente1 = Cliente("Yadira Ureña", "2200024194")

# Reservar habitación 101
reserva1 = Reserva(cliente1, habitaciones[0])
reserva1.confirmar()

# Intentar reservar la misma habitación de nuevo
reserva2 = Reserva(cliente1, habitaciones[0])
reserva2.confirmar()

# Cancelar la reserva
reserva1.cancelar()

# Mostrar estado actualizado
mostrar_habitaciones(habitaciones)