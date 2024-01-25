#pedir nombre y dar los buenos dias
def tipotexto(nombre):
    saludo=("buenos dias",nombre)
    print(saludo)
tipotexto("jun")

#pedir 2 numeros y sumarlos
def suma():
    num1=int(input("dame el numero 1:"))
    num2=int(input("dame el numero 2:"))
    suma=num1+num2
    print(suma)
suma()