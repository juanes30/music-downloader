__author__ = 'Juan.Londono'
import sys
from PyQt5 import QtGui, QtCore

class PrimeraAplicacion(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init(self, parent)
        self.setGeometry(300,300,200,200)
        self.setWindowTitle('Venta de Ejemplo')
        quit = QtGui.QPushButton('Close', self)
        quit.setGeometry(10, 10, 70, 40)
        self.connect(quit, QtCore.SIGNAL('clicked()'), QtGui.qApp, QtCore.SLOT('quit()'))


app = QtGui.QApplication(sys.argv)
dw = PrimeraAplicacion()
dw.show()
sys.exit(app.exec_())

print ("Aprendiendo python variables") #forma de mostrar un mensaje en el shell

edad = 27 # declaracion de variable tipo int

altura=1.75 # declaracion de variable tipo float

nombre = "Juan" # declaracion de variable tipo string

sexo = True # declaracion de variable tipo boolean

print ("OPERADORES MATEMATICOS") #operadores matematicos

x = 2
y=3

# con // se redondea hacia bajo
#resultado = x // y

# con % es el residuo
# resultado = x % y

#para sacar la potencia, quiere decir x elevado a la y
resultado = (x**y)

print (resultado)

print ("CONDICIONALES")# condicionales en python
edad = 17
pago = True

if edad > 18:
    if pago == True:
        print ('Si Pago y eres mayor de edad')
    else:
        print ('Eres mayor pero No Pago')
elif edad < 18:
    print ('eres meno de edad')
else:
    print ('No es mayor de edad')

print ("COMPARADORES")# operadores relacionales en python o comparadores en python

print ('>=, <=, !=, == ')

print ("OPERADORES LOGICOS")# operadores logicos

print ('and, or, not')

print ("CICLO WHILE")#while en python con "," se hace un concatenado en print
numero = 1

while numero < 5:
    print ("el valor de numero es: ", numero)
    numero += 1

print ("FUNCIONES")#funciones

def Saludo():
    print ('Hola')

def Comer():
    print ('Comer')


Saludo()

print ("FUNCIONES CON PARAMETROS")# funciones con parametros
def Nombre(nombre):
    print ("hola",nombre)

Nombre("Juan")

print ("FUNCIONES QUE RETORNAN")# funciones que retorna algo

def Sumar(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

sumar = Sumar(5,7)
print (sumar)

print ("FUNCIONES CON PARAMETROS DEFAULD")# funciones con parametros por defecto
def Sumar2(numero1, numero2=0):
    resultado = numero1 + numero2
    return resultado

sumar2 = Sumar2(5)
print (sumar2)

print ("Tuplas en python") # no se pueden modificar

tupla = (27,1.25,"Juan")

print (tupla[2])

indece = 0

while indece < len(tupla):
    print(tupla[indece])
    indece += 1

print ("tuplas con for")

tupla = (12,25,98,45,24)

for numeros in tupla:
    print(numeros)

print ("tuplas por porciones")

tupla = (12,454,42,4823,5)

tupla2 = tupla[:2]

print (tupla2)

print ("Manejo de cadenas en python")

nombre = "Juan Esteban Londoño Tabares"
print(nombre[:4]) #saco una porcion de la cadena

print ("listas en python") #listas en python

lista = ['Juan','Juliana',98,76]
lista2 = ['Samuel','Games',1]
print (len(lista))

for elemento in lista:
    print(elemento) #recorro elemento por elemento

listaf=lista+lista2 # unificando las listas o concatenacion
print (listaf)

if 98 in lista: #buscando un elemento de la lista desde un if
    print("si")
else:
    print("no")

print(listaf[:5])#mostrando una porcion de la lista

print("indices negativos en tuplas y diccionarios")

print(listaf[-1]) #con esto accedo al ultimo dato.

print ("dicionario en python") #diccionario en python
diccionario = {'Juan':23,'Juliana':15, 'Samuel':11}

print(diccionario[1])

print(len(diccionario))

print ("funciones proporcionadas por python")

tupla =(2,4,5)

help(tupla)

print ("funcion Type en Python")

x = True

print(type(x))

print("str en python")

numero = 7
numero2 = 2

print(str(numero) + str(numero2))
print(numero)

print ("funcion dir en python")

tupla = (1,2,3,4)
print(dir(tupla))

print ("Clases y Atributos")
class Persona:
    #pass # ya que las clases siempre tiene que tener informacion.
    nBrazos = 0
    nPiernas =0
    cabello = True
    cCabello = "Defecto"
    hambre = 0
    
    print ("Inicializar o constructor") #se inicilizan los objectos de forma predeterminada

    def __init__(self):
        self.nBrazos = 2
        self.nPiernas = 2
        
    def Dormir():
        pass

    def Comer(self):#self busca el atributo y lo modifica dentro de la misma clase
        self.hambre=0

    print ("Herencia")
    
        
class Hombre(Persona):
    #pass
    nombre="Defecto"
    sexo = "M"

    def CambiarNombre(self, nombre):
        self.nombre = nombre


samuel = Hombre()
samuel.Comer()
print(samuel.hambre)


print ("archivos")

def CrearArchivo():
    archivo =open('datos.txt','w') #w significa que vamos a escribir si no existe lo crea
    archivo.close()

def EscribirArchivo():
    archivo = open('datos.txt','a') # se agregan nuevas cosas
    archivo.write('Juan Esteban\n')
    archivo.write('Developer')
    archivo.close()

def LeerArchivo ():
    archivo = open('datos.txt','r')
    linea = archivo.readline()
    while linea != "":
        print (linea)
        linea=archivo.readline()
    archivo.close()
LeerArchivo()
