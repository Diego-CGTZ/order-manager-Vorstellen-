from datetime import datetime

class Pedido:
    def __init__(self, cliente, prendas, fecha_entrega, pago_inicial):
        self.cliente = cliente
        self.prendas = prendas  # lista de Prenda
        self.fecha_entrega = fecha_entrega
        self.pago_inicial = pago_inicial
        self.fecha_creacion = datetime.now()

    def calcular_total(self):
        total = 0
        for prenda in self.prendas:
            subtotal = prenda.precio_unitario * prenda.cantidad
            for p in prenda.personalizaciones:
                subtotal += p.precio * prenda.cantidad
            total += subtotal
        return round(total * 1.16, 2)  # Total con 16% IVA

    def saldo_pendiente(self):
        return round(self.calcular_total() - self.pago_inicial, 2)
