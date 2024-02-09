#actividad 2 con def e init

class Asistencia:
    def __init__ (self,nombre,materia,hora):
        self.nombre=nombre
        self.hora=hora
        self.materia=materia
        self.asistio=False
    def asistio(self):
        if self.asistio==True:
            print("El asistio al lugar")
        else:
            self.asistio=True
    def falta(self):
        if self.asistio:
            self.asistio=False
            print("No asistio, Faltó")
    def datos(self):
        print(f"El {self.nombre} en la materia de {self.materia} a la hora {self.hora} tuvo que {self.asistio}")
a1=Asistencia("Manolo","Calculo",10.20)
a1.datos()
a1.asistio()
a1.datos()
