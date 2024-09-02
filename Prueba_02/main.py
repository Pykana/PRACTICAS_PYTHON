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
    


