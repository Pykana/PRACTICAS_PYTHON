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

if diaTrabajo.upper() == 'LUNES' or diaTrabajo == "1":
    print("Escogio el dia lunes")
elif diaTrabajo.upper() == 'MARTES' or diaTrabajo == "2":
    print("Escogio el dia martes")
elif diaTrabajo.upper() == 'MIERCOLES' or diaTrabajo == "3":
    print("Escogio el dia miercoles")
elif diaTrabajo.upper() == 'JUEVES' or diaTrabajo == "4":
    print("Escogio el dia jueves")
elif diaTrabajo.upper() == 'VIERNES' or diaTrabajo == "5":
    print("Escogio el dia viernes")
else:
    print("Día no válido")
