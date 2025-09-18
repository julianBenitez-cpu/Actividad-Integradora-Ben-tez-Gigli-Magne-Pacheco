class robot:
    def __init__(self, nombre, color, fechaFabricacion, modelo, numeroSerie):
        self.nombre = nombre
        self.color = color
        self.fechaFabricacion = fechaFabricacion
        self.modelo = modelo
        self.numeroSerie = numeroSerie

    def get_numeroSerie_robot(self):
        return self.numeroSerie
    
    def get_nombre_robot(self):
        return self.nombre
    
    def get_color_robot(self):
        return self.color
    
    def get_fechaFabricacion_robot(self):
        return self.fechaFabricacion
    
    def get_modelo_robot(self):
        return self.modelo
    
    def set_nombre_robot(self, nombre):
        self.nombre = nombre

    def set_color_robot(self, color):
        self.color = color

    def set_fechaFabricacion_robot(self, fechaFabricacion):
        self.fechaFabricacion = fechaFabricacion

    def set_modelo_robot(self, modelo):
        self.modelo = modelo

    def set_numeroSerie_robot(self, numeroSerie):
        self.numeroSerie = numeroSerie

    def mostrar_informacion_robot(self):
        return f"Nombre: {self.nombre}, Color: {self.color}, Fecha de Fabricacion: {self.fechaFabricacion}, Modelo: {self.modelo}"
    

robot1 = robot("Robo1", "Rojo", "2023-01-01", "X100", "12345")
robot2 = robot("Robo2", "Azul", "2023-02-01", "Y200", "67890")
print(robot1.mostrar_informacion_robot())
print(robot2.mostrar_informacion_robot())