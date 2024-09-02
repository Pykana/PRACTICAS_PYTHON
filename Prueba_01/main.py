#################################################
# PARA CORRER UNA PARTE DEL CODIGO BORRAR LOS  #
# PARA COMENTAR UNA PARTE DEL CODIGO COLOCAR   #
#################################################

#############################
#   CUIDADO CON LOS ESPACIOS
############################


# IMPRIMIR DATA

print("hola gente")

# SETEAR VARIABLES

var1="hola"
var2=" gente"
var3=var1 + var2
var4="Otra"
var4+=" Forma"

print(var1+var2)
print(var3)
print(var4)

# BUSCAR SUB CADENA DENTRO DE TEXTO

mensaje="Cadena de mensaje en Python ,hola mundo"
subCadena=mensaje.find("Python")

print("Mensaje :\n" ,mensaje ,"\ncon subcadena: (posicion) " ,subCadena)

# EXTRAER MENSAJE DE LA POSICION DE LA SUBCADENA

subCadenaTexto=mensaje[20:27] # se añade un digito mas al deseado  ejm : dato 21  == dato 22    python = de 21 a 26

print("texto extraido: ", subCadenaTexto)


# COMPRAR CADENA DE TEXTO

mensaje1="texto 1"
mesanje2="texto1"

print("Primer mensaje : ",mensaje1,"\nSegundo mensaje: ",mesanje2,"\nSon iguales? Resultado: ",mensaje1==mesanje2)

# SUMA DE VARIABLES Y SUBA DE VARIABLES INTRODUCIDAS

dato1=5
dato2=6.5

print("Resultado de la suma : ", dato1+dato2) #se puede guardar en otra variable antes o despues de guardar


#ERROR , AQUI CONCATENO CARACTERES INGRESADOS

dato1=input("Ingrese el dato 1 : ")
dato2=input("ingrese el dato 2 : ")

print("La suma es : " , dato1+dato2)


# FORMA CORRECTA 

#dato1=int(input("Ingrese el dato 1 : "))  # A ENTEROS
#dato2=int(input("ingrese el dato 2 : "))  # A ENTEROS

dato1=float(input("Ingrese el dato 1 : "))  # A DECIMALES
dato2=float(input("ingrese el dato 2 : "))  # A DECIMALES


print("La suma es : " , dato1+dato2)
