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

traerUsuarios='Select * from usuario'
insertarUsuario='INSERT INTO USUARIO (Correo, Contrasena) values (%s,%s)'  # CONSULTA INSERTAR
buscarUsuario = 'SELECT * FROM USUARIO WHERE id_Usuario = %s' # CONSULTA SELECT * FROM
eliminarUsuario = 'DELETE FROM USUARIO WHERE id_Usuario = %s' # CONSULTA DELETE
editarUsuario = 'UPDATE USUARIO SET Correo = %s , Contrasena = %s WHERE id_Usuario = %s' # CONSULTA UPDATE

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

                mycursor.execute(insertarUsuario,values) # Iniciarlizar la consulta a realizar
                mydb.commit()  # realizar cambios a base de datos

                print("Usuario Creado")
                time.sleep(3)  # Pausa por 3 segundos
            case 2:
                limpiarPantalla()
                print("Editar Usuario")
                idUsuario = input('Ingrese el Id del usuario a editar :')
                usuario=input('Ingrese el nuevo campo para correo')
                contrasena=input('Ingrese el nuevo campo para la contraseña')
                try:
                    values = (usuario, contrasena, idUsuario)
                    mycursor.execute(editarUsuario, values)
                    mydb.commit()
                    print("Se edito correctamente el usuario")
                    time.sleep(3)
                except:
                    limpiarPantalla()
                    print("No se encontro el usuario ")
                    time.sleep(3)
            case 3:
                limpiarPantalla()
                print("Borrar Usuario")
                try:
                    idUsuario = input('Ingrese el Id del usuario a eliminar :')
                    values = (idUsuario,)

                    mycursor.execute(eliminarUsuario, values)
                    mydb.commit()

                    print(f'Usuario Eliminado')
                    time.sleep(3)
                except:
                    limpiarPantalla()
                    print("No se encontro el usuario ")
                    time.sleep(3)
            case 4:
                limpiarPantalla()
                print("Buscar Usuario")

                try:
                    idUsuario = input('Ingrese el Id del usuario a buscar :')
                    values = (idUsuario,)
                    mycursor.execute(buscarUsuario, values)
                    respuesta = mycursor.fetchone()
                    if (respuesta):
                        print(f"Resultado : {respuesta}")
                    else:
                        print("No se encontro resultados")
                    time.sleep(3)
                except:
                    limpiarPantalla()
                    print("Error en consulta buscar ")
                    time.sleep(3)

            case 5:
                limpiarPantalla()
                print("Mostrar Usuario")
                mycursor.execute(traerUsuarios)
                respuesta = mycursor.fetchall()
                if respuesta:  # Si hay resultados
                    for fila in respuesta:  # Recorre cada fila de la lista
                        print(f"Usuario: {fila}")
                else:
                    print("No se encontraron resultados")
                time.sleep(3)
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


