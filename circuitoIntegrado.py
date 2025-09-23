from bateria import bateria

class CircuitoIntegrado:
    def __init__(self, tipo_bateria = "Li-ion", marca_bateria = "Duracell"):
        self.__bateria = bateria(tipo_bateria, marca_bateria)
        self.__estado = "apagado"

    def encender(self):
        if self.__bateria.get_porcentaje() > 0:
            self.__estado = "encendido"
            return "circuito encendido con bateria disponible"
        else:
            return "no se puede encender, no hay batería."

    def apagar(self):
        self.__estado = "apagado"
        return "circuito apagado."

    def consumir_energia(self, cantidad):
        if self.__estado == "encendido":
            if self.__bateria._porcentaje_actual >= cantidad:
                self.__bateria._porcentaje_actual -= cantidad
                return f"Se Consumio{cantidad}%. Batería restante: {self.bateria.porcentaje_actual}%"
            else:
                self.__apagar()
                return "energia no suficiente, el dispositivo se apago"
        return "elcircuito está apagado."

    def estado_circuito(self):
        return f"Circuito: {self.__estado}, Batería: {self.__bateria._porcentaje_actual}%"