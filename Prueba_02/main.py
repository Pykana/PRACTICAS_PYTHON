# USO DEL IF - DESCUENTO 

# Ejemplo 1 

nombre=input("Escriba su nombre : ")
TotalCompras= float(input("Escriba el total de comrpas realizadas : "))
if(TotalCompras >500):
    descuento=TotalCompras*.10  #10%
    print("Felicidades ",nombre," tiene un total de ",descuento," por compras mayores a 500")
else:
    print("No cuenta con el monto requerido (500) para obtener el descuento")

# Ejemplo 2

nombre=input("Escriba su nombre : ")
edad=int(input("Escriba su edad : "))

if(edad<18):
    print("Usted no cumple con la edad minima requeridad")
else:
    dni=input("Cuenta con DNI? (S/N) :")
    if(dni.upper()=='S'):
        print("Cuenta con los requisitos para votar")
        #print("Nombre : ", nombre,"\nEdad : ",edad)
        print(f'Nombre : {nombre} \nEdad : {edad}') #OTRA FORMA
    else:
        print("No cuenta con los requisitos para votar")
        print("DNI Necesario")
    


# Ejemplo 3

estatura=float(input("Escriba su estatura : "))

if(estatura>1.60):
    if(estatura>2.10):
        print(f'Si pasa \nSu estatura es de {estatura}')
    else:
        print("Escriba una estatura real")
else:
    print("La estatura requerida es de 1.60 a mas")
    

# Ejemplo 4

diaTrabajo = input("Escriba el dia que quiere trabajar : (Escriba el dia o del 1 al 5)")

#TIPO SWITCH 
if diaTrabajo.upper() == 'LUNES' or diaTrabajo == "1":  #CASO
    print("Escogio el dia lunes")
elif diaTrabajo.upper() == 'MARTES' or diaTrabajo == "2":#CASO
    print("Escogio el dia martes")
elif diaTrabajo.upper() == 'MIERCOLES' or diaTrabajo == "3":#CASO
    print("Escogio el dia miercoles")
elif diaTrabajo.upper() == 'JUEVES' or diaTrabajo == "4":#CASO
    print("Escogio el dia jueves")
elif diaTrabajo.upper() == 'VIERNES' or diaTrabajo == "5":#CASO
    print("Escogio el dia viernes")
else:      #DEFAULT
    print("Día no válido")


# Ejemplo 5


moneda=float(input("Escriba la cantidad de soles : "))
opcion=int(input("\nA que moneda desea convertir:"
                   "\n1: Dolares S/3.75 "
                   "\n2: Pesos mexicanos S/0.19"
                   "\nOpcion : "))

if(opcion == 1):
    print(f'Saldo ingresado de : {moneda} \nSaldo convertido : {round((moneda/3.75),2)}')
    # print(f'Saldo ingresado de : {moneda} \nSaldo convertido : {moneda/3.75}')
elif opcion == 2:#CASO
    print(f'Saldo ingresado de : {moneda} \nSaldo convertido : {round((moneda/0.19),2)}')
    # print(f'Saldo ingresado de : {moneda} \nSaldo convertido : {moneda/0.19}')
else:      
    print("Opcion inexistente")


# USO DEL WHILE

# Ejemplo 6

import time #Sirve para manjear el tiempo en un programa

contador=10

print('Iniciando cuenta regresiva...')

while(contador>0):
    print(contador)
    time.sleep(1)
    contador-=1 #Reducir el valor en 1
print('¡El cohete ha despegado con existe!')


# Ejemplo 7

# USO DE MATCH

def evaluar_dia(diaTrabajo):   #DEF = FUNCIONES 
    match diaTrabajo:           # funcion similar al switch
        case "1" | "LUNES":     # caso
            return "Escogió el día lunes"
        case "2" | "MARTES":# caso
            return "Escogió el día martes"
        case "3" | "MIÉRCOLES":# caso
            return "Escogió el día miércoles"
        case "4" | "JUEVES":# caso
            return "Escogió el día jueves"
        case "5" | "VIERNES":# caso
            return "Escogió el día viernes"
        case _:# default
            return "Día no válido"

dia = input("Escriba el dia que quiere trabajar : (Escriba el dia o del 1 al 5)")
resultado = evaluar_dia(dia.upper())
print(resultado)
# print(evaluar_dia(dia.upper())) # Otra forma


# Ejemplo 8

# USO DE MATCH

x=int(input('Ingrese variable X:'))
y=int(input('Ingrese variable Y:'))

point=(x,y) # tupla - secuencia de elementos inmutables (no se pueden modificar después de su creación)

match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        # raise ValueError("Not a point")
         print('Error')

# Ejemplo 9

x = int(input('Ingrese variable X:'))
y = int(input('Ingrese variable Y:'))

point = [x, y]  # Lista (array)

# Se utiliza el comodín _ para ignorar un valor específico en la comparación osea el elemento puede ser cualquier valor

match point:
    case [0, 0]:
        print("Origin")
    case [0, _]:
        print(f"Y={point[1]}")
    case [_, 0]:
        print(f"X={point[0]}")
    case [_, _]:
        print(f"X={point[0]}, Y={point[1]}")
    case _:
        print('Error')




