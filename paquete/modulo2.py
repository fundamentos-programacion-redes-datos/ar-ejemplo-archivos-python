"""

"""

from paquete.modulo3 import obtener_reporte

def obtener_docentes(numero=1):
    # Inicialización de variables
    contador = 0  # Contador para numeración de docentes
    bandera = True  # Variable de control para el ciclo while
    
    contador = 1  # Se inicializa el contador en 1

    # Uso de lista para almacenar la información de los docentes
    lista_docentes = []  # Lista donde cada docente se almacenará como una sublista
    
    # Bucle para ingreso de datos de los docentes
    while contador <= numero:  # Se ejecuta hasta que se ingresen la cantidad de docentes solicitados
        print("\nIngrese la información del docente:")
        nombre = input("Nombre del docente: ")  # Se solicita el nombre del docente
        apellido = input("Apellidos del docente: ")  # Se solicita el apellido del docente
        ciudad = input("Ciudad de residencia: ")  # Se solicita la ciudad de residencia del docente

        # Se almacena la información en una lista temporal
        lista = [nombre, apellido, ciudad]  
        lista_docentes.append(lista)  # Se agrega la lista del docente a la lista principal
    
        contador = contador + 1  # Se incrementa el contador para controlar el número de registros
    
    reporte = obtener_reporte(2, lista_docentes)
    
    # Impresión del reporte final de docentes
    print(reporte)  # Se muestra el listado de docentes
