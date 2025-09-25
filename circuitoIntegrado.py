from bateria import bateria

class CircuitoIntegrado:
    def __init__(self, tipo_bateria = "Li-ion", marca_bateria = "Duracell"):
        self.bateria = bateria(tipo_bateria, marca_bateria)
        self.__estado = "apagado"

    def get_estado(self):
        return self.__estado

    def encender(self):
        if self.bateria.get_porcentaje() > 0:
            self.__estado = "encendido"
            return "Circuito encendido con bateria disponible"
        else:
            return "No se puede encender, no hay batería."

    def apagar(self):
        self.__estado = "apagado"
        return "Circuito apagado."

    def consumir_energia(self, cantidad):
        if self.__estado == "encendido":
            if self.bateria.get_porcentaje() >= cantidad
                self.bateria._porcentaje -= cantidad
                return f"Se Consumio{cantidad}%. Batería restante: {self.bateria.get_porcentaje()}%"
            else:
                self.__apagar()
                return "Energia no suficiente, el dispositivo se apagó"
        return "El circuito está apagado."

    def estado_circuito(self):
        return f"Circuito: {self.__estado}, Batería: {self.bateria.get_porcentaje()}%"
