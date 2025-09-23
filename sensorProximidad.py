from sensor import sensor

class sensorProximidad(sensor):

    objetoAdelante = False;
    
    def __init__(self, modelo,  marca, n_serie, f_fabricacion, alcance):
        super().__init__(modelo, marca, n_serie, f_fabricacion);
        self.__alcance = alcance;

    def get_alcance(self):
        return self.__alcance;

    def set_alcance(self, alcance):
        self.__alcance = alcance;

    def detectar(self, distancia_objeto):
        if distancia_objeto <= self.__alcance and distancia_objeto >= 0:
            self.objetoAdelante = True
            return True
        else:
            self.objetoAdelante = False
            return False

    def alertar(self, distancia_objeto):
        if self.detectar(distancia_objeto):
            print(f"¡Objeto detectado! Distancia: {distancia_objeto}m")
        else:
            print(f"No hay objetos detectados. Distancia: {distancia_objeto}m")
