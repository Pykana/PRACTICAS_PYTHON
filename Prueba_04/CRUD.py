
#Ejemplo 3
# base_dev_python  --- Nombre base de datos
# cd "C:\Program Files\MariaDB 10.5\bin"  -- navegar hasta la carpeta de mysql
# mysql -u root -h localhost -p # comando conexion mysql terminal

import mysql.connector  # conexion a sql
import os  # maneja instrucciones del sistema
import time  # manejar tiempo ejecucion de un programa

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="SapoRana123",
    database="base_dev_python"
)

insertarTablaUsuario='INSERT INTO usuario (Correo, Contrasena) values (%s,%s)'  # CONSULTA INSERTAR
selectTablaUsuario = 'SELECT * FROM usuario' # CONSULTA SELECT * FROM
eliminarUsuario = 'DELETE FROM USUARIO WHERE id_Usuario = %s' # CONSULTA DELETE
editarUsuario = 'UPDATE USUARIO WHERE id_Usuario = %s' # CONSULTA UPDATE

# Recorrido de tabla
mycursor = mydb.cursor()

plantilla = ('----MENU CRUD----'
             '\n1)Crear Usuario'
             '\n2)Editar Usuario'
             '\n3)Borrar Usuario'
             '\n4)Buscar Usuario'
             '\n5)Mostrar Usuario'
             '\n6)Salir del programa')

ProgramaActivo = True

# detectar el tipo de sistema para la limpieza de pantalla
def limpiarPantalla():
    if os.name == 'nt':  # Para sistemas Windows
        os.system('cls')
    else:  # Para sistemas UNIX, como Linux o Mac
        os.system('clear')

def MostrarOpciones():
    global ProgramaActivo  # Declaramos que vamos a modificar la variable global
    limpiarPantalla()
    print(plantilla)
    opcion = input("\nIngrese su opcion: ")

    try:
        opcion = int(opcion)  # Convertimos a entero
        match opcion:
            case 1:
                limpiarPantalla()
                print("Crear Usuario")
                correo=input('Ingrese el correo :')
                contrasena=input('Ingrese la contraseña :')

                values=(correo,contrasena) # Valores a enviar a la consulta sql

                mycursor.execute(insertarTablaUsuario,values) # Iniciarlizar la consulta a realizar
                mydb.commit()  # realizar cambios a base de datos

                print("Se registro el numero usuario : " , mycursor.rowcount)
                time.sleep(3)  # Pausa por 3 segundos
            case 2:
                limpiarPantalla()
                print("Editar Usuario")
                # Aquí iría el código para editar un usuario
            case 3:
                limpiarPantalla()
                print("Borrar Usuario")
            case 4:
                limpiarPantalla()
                print("Buscar Usuario")
            case 5:
                limpiarPantalla()
                print("Mostrar Usuario")
            case 6:
                limpiarPantalla()
                ProgramaActivo = False
                print("Saliendo del programa...")
                time.sleep(3)  # Pausa por 3 segundos
            case _:
                limpiarPantalla()
                print("Opción no válida, ingrese un número entre 1 y 6.")
                time.sleep(3)  # Pausa por 3 segundos
    except ValueError:  # En caso de ingresar algo que no es numero
        limpiarPantalla()
        print('\nDebe Ingresar Números!!!!!')
        time.sleep(3)  # Pausa por 3 segundos

while ProgramaActivo:
    MostrarOpciones()


