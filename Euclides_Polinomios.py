# numpy.polydiv()  
from fractions import Fraction
import numpy as np

print("\n\n\tCALCULO DEL MAXIMO COMUN DIVISOR DE POLINOMIOS CON EL ALGORITMO DE EUCLIDES ")

def PideInfo1 ():   #Pide informacion sobre el primer polinomio (grado y coeficientes)
    po1 = []
    print ("Grado del primer polinomio: ", end="")
    g = int(input())
    for i in range((g+1)):
        if (i<g):
            print("Valor del ", (i+1), "° coeficiente: ", end="")
            valor = str(input())
            valor = Fraction(valor)
            valor = float(valor)
            po1.append(valor)
        else: 
            print("Valor de la constante: ", end="")
            valor = str(input())
            valor = Fraction(valor)
            valor = float(valor)
            po1.append(valor)

    return po1, g

def PideInfo2 ():   #Pide informacion sobre el segundo polinomio (grado y coeficientes)
    po2 = []

    print ("Grado del segundo polinomio: ", end="")
    g = int(input())
    for i in range((g+1)):
        if (i<g):
            print("Valor del ", (i+1), "° coeficiente: ", end="")
            valor = str(input())
            valor = Fraction(valor)
            valor = float(valor)
            po2.append(valor)
        else: 
            print("Valor de la constante: ", end="")
            valor = str(input())
            valor = Fraction(valor)
            valor = float(valor)
            po2.append(valor)

    return po2, g

#Comprobar que el MCD obtenido al dividirlo por los polinomios originales, da 0 
def Comprobacion(poli1Aux, poli2Aux, auxP):
    h = 0
    print("\n\tComprabacion del resultado: ")
    while (h < 2):
        if(h==0):
            print("\n\tPolinomio ", (h+1), ": \n")
            resultado, residuo = (np.polydiv(poli1Aux, auxP))
            h=h+1
        else:
            print("\n\tPolinomio ", (h+1), ": \n")
            resultado, residuo = (np.polydiv(poli2Aux, auxP))
            h=h+1

        print("\n Resultado: ")
        print(np.poly1d(resultado))
        print("\n Residuo: ")
        print(np.poly1d(residuo))

#Mostar polinomios
print("\n")
p1, g1 = PideInfo1()
print("")
p2, g2 = PideInfo2()
print("\n Polinomio 1: \n", )
print(np.poly1d(p1))
print("\n Polinomio 2: \n")
print(np.poly1d(p2))

#-----------------------------------Algoritmo de Euclides-----------------------------------
j=0
poli1Aux = list(p1)
poli2Aux = list(p2)
poli1 = list(p1)
poli2 = list(p2)
auxP = []

while (True):
    j=j+1
    resultado, residuo = (np.polydiv(p1, p2))       #Division de polinomios 
    print("\n------------------\n")
    print("\n", j, "° Resultado: \n")
    print(np.poly1d(resultado))
    print("\n", j, "° Residuo: \n")
    print(np.poly1d(residuo))
    print("\n", j, "° combinacion lineal: \n")
    print(np.poly1d(p1), " = \n", np.poly1d(resultado), " * \n", np.poly1d(p2), " + \n", np.poly1d(residuo))
    if ((len(residuo)==1) & (residuo[0] == 0) & (j==1)):
        print("\n\nComo el primer residuo resulta en 0, el mayor divisor que puede dividir tanto al polimonio p(x) como al polinomio q(x) sin dejar residuo es: \n")
        print(np.poly1d(p2))

        if ((len(p2)==1) & (p2[0]==1)):
            print("\nLos Polinomios p(x) y q(x) son primos relativos, porque el Maximo Comun Divisor es 1\n")
            exit()
        else:
            Comprobacion(poli1Aux, poli2Aux, p2)
            exit()

    p1 = list(p2)
    p2 = list(residuo)

    if (residuo[0]==0):
        for k in range (j-1):
            resultado, residuo_t = (np.polydiv(poli1, poli2))
            poli1 = list(poli2)
            poli2 = list(residuo_t)

        print("\n----------------------------------------------\n")
        print("\nAsi, el candidato a maximo comun divisor es: \n", np.poly1d(residuo_t))
        
        for l in range(len(residuo_t)):
            aux = residuo_t[l] / residuo_t[0]
            auxP.append((aux))

        print ("\nPero necesitamos que sea monico, entonces, el anterior polinomio es igual a la siguiente expresión: \n")
        print (np.poly1d(auxP), " * (", Fraction(residuo_t[0]), ")")
        
        print("\nPor lo tanto, el mayor divisor que puede dividir tanto al polimonio p(x) como al polinomio q(x) sin dejar residuo es: \n")
        print(np.poly1d(auxP))

        if ((len(auxP)==1) & (auxP[0]==1)):
            print("\nLos Polinomios p(x) y q(x) son primos relativos, porque el Maximo Comun Divisor es 1\n")
            Comprobacion(poli1Aux, poli2Aux, auxP)
            exit()
        else:
            Comprobacion(poli1Aux, poli2Aux, auxP)
            exit()