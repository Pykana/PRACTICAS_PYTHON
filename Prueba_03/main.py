#Ejemplo 1

# convertir a mayusculas y minisculas

texto=input("Ingrese texto a convertir: ")
print(f'Texto en Mayusculas {texto.upper()}')
print(f'Texto en Minusculas {texto.lower()}')

# Ejemplo 2

# validar que se introduscan datos numeros

while True:
    try:
         dato=input('Ingrese su edad: ')
         edad=int(dato)
         if((edad<0) or (edad>120)):
             print('Edad no valida')
         else:
             break
    except:
        print('Ingrese solo numeros')
print(f'Tu edad actual es de {edad}')




