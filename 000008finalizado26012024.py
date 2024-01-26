lado=10
radio=5
base=10
altura=10

def areaCuadrado(lado):
    return lado*lado
areaCuadrado(lado)

def areaCirculo(radio):
    return 3.1416*radio*radio
areaCirculo(radio)

def areaTriangulo(base,altura):
    return base*altura/2
areaTriangulo(base,altura)

def areaMedioCuadrado(lado):
    return lado*lado/2
areaMedioCuadrado(lado)

def areaTotal():
    area=areaCuadrado(lado)+areaCirculo(radio)+areaTriangulo(base,altura)+areaMedioCuadrado(lado)
    print("el area total es:", area)
areaTotal()