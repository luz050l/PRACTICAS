A=int(input("Cual es su altura?"))
P=float(input("Cual es su peso?"))

class Persona:
    def __init__ (self,nombre,edad,DNI,peso,altura):
        self.nombre=nombre
        self.edad=edad
        self.sexo=True
        self.peso=peso
        self.altura=altura
    def mujer(self):
        if self.sexo==False:
            print("La persona es hombre")
        else:
            self.mujer=True
    def hombre(self):
        if self.sexo:
            self.sexo=False
        else:
            print("Es mujer")
    def edad (self):
        if self.edad<=18:
            print("LEGAL")
        else:
            print("ILEGAL")
    def IMC(self):
        imc=P/A*A
        print("El IMC es:",imc)
    def Persona(self):
        print(f"la persona{self.nombre} tiene{self.edad} y su IMC es{self.IMC}")
p1=Persona("Ana",18)
p1.datos()
