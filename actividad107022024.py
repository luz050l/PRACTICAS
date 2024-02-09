#actividad 1  def e init

class Celular:
    def __init__ (self,marca, modelo, color):
        self.marca=marca
        self.modelo=modelo
        self.color=color
        self.prendido=True
    def prendido(self):
        if self.prendido==False:
            print("El telefono esta apagado")
        else:
            self.prendido=False
    def apagar(self):
        if self.prendido:
            self.prendido=True
        else:
            print("Esta encendiodo")
    def datos (self):
        print(f"El celular {self.modelo} es de la marca {self.marca} de color {self.color} y esta {self.prendido}")
c1=Celular("samsung","S24 ultra","Rojo")
c1.datos()
