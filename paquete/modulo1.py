"""

"""
from paquete.modulo3 import obtener_reporte

def obtener_estudiantes(numero=1):
    # Inicialización de variables
    contador = 0  # Contador para numeración de estudiantes
    bandera = True  # Variable de control para el ciclo while
    
    contador = 1  # Se inicializa el contador en 1

    # Uso de lista para almacenar la información de los estudiantes
    lista_estudiantes = []  # Lista donde cada estudiante se almacenará como una sublista
    
    # Bucle para ingreso de datos de los estudiantes
    while contador <= numero:  # Se ejecuta hasta que se ingresen la cantidad de estudiantes solicitados
        print("\nIngrese la información del estudiante:")
        nombre = input("Nombre del estudiante: ")  # Se solicita el nombre del estudiante
        apellido = input("Apellidos del estudiante: ")  # Se solicita el apellido del estudiante
        correo = input("Correo del estudiante: ")  # Se solicita el correo electrónico del estudiante
        edad = input("Edad del estudiante: ")  # Se solicita la edad del estudiante
        edad = int(edad)  # Conversión de la edad a entero

        # Se almacena la información en una lista temporal
        lista = [nombre, apellido, correo, edad]  
        lista_estudiantes.append(lista)  # Se agrega la lista del estudiante a la lista principal
    
        contador = contador + 1  # Se incrementa el contador para controlar el número de registros
    
    reporte = obtener_reporte(1, lista_estudiantes)
    
    # Impresión del reporte final de estudiantes
    print(reporte)  # Se muestra el listado de estudiantes
