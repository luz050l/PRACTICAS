def infoCuadrado():
    print("el area se calcula con: lado*lado")
infoCuadrado()

def infoTriangulo():
    print("el area se calcula con: base*altura/2")
infoTriangulo()

def infoRectangulo():
    print("el area se calcula con: base*altura")
infoRectangulo()

def infoPentagono():
    print("el area se calcula con: lado1*altura1/2*lado2")
infoPentagono()

def menuFiguras(opcion):
    if (opcion==1):
        infoCuadrado()
    elif (opcion==2):
        infoTriangulo()
    elif (opcion==3):
        infoRectangulo()
    elif (opcion==4):
        infoPentagono()

print("BIENVENIDO")
print("MENU")
print("Escoja una opcion:")
print("1. cuadrado")
print("2. triangulo")
print("3. rectangulo")
print("4. pentagono")
opcion=int(input("Escoge una opcion: "))
menuFiguras(opcion)