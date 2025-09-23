from bateria import bateria

class CircuitoIntegrado:
    def __init__(self, tipo_bateria, marca_bateria):
        # crea y controla la batería
        self.bateria = bateria(tipo_bateria, marca_bateria)
        self.estado = "apagado"

    def encender(self):
        if self.bateria.get_porcentaje() > 0:
            self.estado = "encendido"
            return "circuito encendido con bateria disponible"
        else:
            return "no se puede encender, no hay batería."

    def apagar(self):
        self.estado = "apagado"
        return "circuito apagado."

    def consumir_energia(self, cantidad):
        if self.estado == "encendido":
            if self.bateria.porcentaje_actual >= cantidad:
                self.bateria.porcentaje_actual -= cantidad
                return f"Se Consumio{cantidad}%. Batería restante: {self.bateria.porcentaje_actual}%"
            else:
                self.apagar()
                return "energia no suficiente, el dispositivo se apago"
        return "elcircuito está apagado."

    def estado_circuito(self):
        return f"Circuito: {self.estado}, Batería: {self.bateria.porcentaje_actual}%"
