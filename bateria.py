class bateria:
    def __init__(self, tipo, marca, porcentaje_actual= 100):
        self.tipo = tipo
        self.marca = marca
        self.porcentaje_actual = porcentaje_actual

        def mostrar_porcentaje_actual(self):
            if porcentaje_actual == 0:
                print(f"La batería está completamente descargada.")
            
            else:
                print(f"El porcentaje de batería actual es {self.porcentaje_actual}%.")
