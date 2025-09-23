from sensorProximidad import sensorProximidad
from circuitoIntegrado import CircuitoIntegrado 
class robot:
    def __init__(self, nombre, color, fechaFabricacion, modelo, numeroSerie):
        self.__nombre = nombre
        self.__color = color
        self.__fechaFabricacion = fechaFabricacion
        self.__modelo = modelo
        self.__numeroSerie = numeroSerie
        self.__sensor = sensorProximidad("SP-100", "RoboSensors", "SP123456", "2023-01-01", 5.0) 
        self.__circuito = CircuitoIntegrado()

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

    def mostrar_informacion_robot(self):
        return f"Nombre: {self.__nombre}, Color: {self.__color}, Fecha de Fabricacion: {self.__fechaFabricacion}, Modelo: {self.__modelo} con Nº de Serie: {self.__numeroSerie}, Sensor: [{self.__sensor} ], Circuito: [{self.__circuito.estado_circuito()}]"
    

robot1 = robot("Robo1", "Rojo", "2023-01-01", "X100", "12345")
print(robot1.mostrar_informacion_robot())
