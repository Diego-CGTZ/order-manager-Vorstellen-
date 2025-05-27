class Prenda:
    def __init__(self, tipo, cantidad, precio_unitario, personalizaciones=[]):
        self.tipo = tipo
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.personalizaciones = personalizaciones  # lista de Personalizacion
