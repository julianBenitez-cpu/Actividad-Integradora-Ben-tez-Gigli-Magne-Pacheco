class bateria:
    def __init__(self, tipo, marca, porcentaje_actual = 100):
        self.__tipo = tipo
        self.__marca = marca
        self._porcentaje_actual = porcentaje_actual

    def get_porcentaje(self):
        return self._porcentaje_actual

    def mostrar_porcentaje(self):
        if self.get_porcentaje() == 0:
            print(f"La batería está completamente descargada..")
        else:
            print(f"El porcentaje de batería actual es {self._porcentaje_actual}%.")
    def mostrar_atributos(self):
        return f"El tipo de la bateria es: {self.__tipo}, de la marca: {self.__marca}"
