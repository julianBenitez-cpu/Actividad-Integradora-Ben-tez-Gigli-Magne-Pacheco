class sensor:
    def __init__(self, modelo, marca, n_serie, f_fabricacion):
        self.__modelo = modelo;
        self.__marca = marca;
        self.__n_serie = n_serie;
        self.__f_fabricacion = f_fabricacion;

    def get_modelo(self):
        return self.__modelo;

    def get_marca(self):
        return self.__marca;

    def get_n_serie(self):
        return self.__n_serie;

    def get_f_fabricacion(self):
        return self.__f_fabricacion;

    def set_modelo(self, modelo):
        self.__modelo = modelo;

    def set_marca(self, marca):
        self.__marca = marca;

    def set_n_serie(self, n_serie):
        self.__n_serie = n_serie;

    def set_f_fabricacion(self, f_fabricacion):
        self.__f_fabricacion = f_fabricacion;

    def __str__(self):
        return f'Sensor tipo {self.get_modelo()} de {self.get_marca()}. NºSerie {self.get_n_serie()}, fabricado en {self.get_f_fabricacion()}';
