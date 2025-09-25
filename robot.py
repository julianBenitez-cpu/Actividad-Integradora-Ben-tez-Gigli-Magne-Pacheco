from sensorProximidad import sensorProximidad
from circuitoIntegrado import CircuitoIntegrado 
class robot:
    def __init__(self, nombre, color, fechaFabricacion, modelo, numeroSerie):
        self.__nombre = nombre
        self.__color = color
        self.__fechaFabricacion = fechaFabricacion
        self.__modelo = modelo
        self.__numeroSerie = numeroSerie
        self.sensor = sensorProximidad("SP-100", "RoboSensors", "SP123456", "2023-01-01", 5.0) 
        self.circuito = CircuitoIntegrado()

    def get_numeroSerie_robot(self):
        return self.__numeroSerie
    
    def get_nombre_robot(self):
        return self.__nombre
    
    def get_color_robot(self):
        return self.__color
    
    def get_fechaFabricacion_robot(self):
        return self.__fechaFabricacion
    
    def get_modelo_robot(self):
        return self.__modelo
    
    def set_nombre_robot(self, nombre):
        self.__nombre = nombre

    def set_color_robot(self, color):
        self.__color = color

    def set_fechaFabricacion_robot(self, fechaFabricacion):
        self.__fechaFabricacion = fechaFabricacion

    def set_modelo_robot(self, modelo):
        self.__modelo = modelo

    def set_numeroSerie_robot(self, numeroSerie):
        self.__numeroSerie = numeroSerie

    def __str__(self):
        return f"Nombre: {self.get_nombre_robot()}, Color: {self.get_color_robot()}, Fecha de Fabricacion: {self.get_fechaFabricacion_robot()}, Modelo: {self.get_modelo_robot()} con Nº de Serie: {self.get_numeroSerie_robot}, Sensor: [{self.sensor}], Circuito: [{self.circuito.estado_circuito()}]"
    