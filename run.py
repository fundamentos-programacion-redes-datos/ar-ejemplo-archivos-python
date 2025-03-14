"""

"""

from paquete.modulo1 import obtener_estudiantes
from paquete.modulo2 import obtener_docentes
from paquete.modulo3 import presentar_informacion

# Menú principal del programa
if __name__ == "__main__":
    bandera = True  # Variable de control para mantener el programa en ejecución

    while bandera:  # Se ejecuta hasta que el usuario decida salir
        mensaje = "Menú\nIngrese 1 para generar estudiantes; 2 para generar docentes; 3 para generar un estudiante y un docente: "
        opcion = input(mensaje)  # Se solicita al usuario que elija una opción del menú
        opcion = int(opcion)  # Conversión a entero para procesar la elección
        
        if opcion == 1:
            # Solicitar el número de estudiantes a registrar
            elementos = input("Ingrese el número de estudiantes a generar: ")  
            elementos = int(elementos)  # Conversión a entero
            obtener_estudiantes(elementos)  # Se llama a la función para registrar estudiantes
        else:
            if opcion == 2:
                # Solicitar el número de docentes a registrar
                elementos = input("Ingrese el número de docentes a generar: ")  
                elementos = int(elementos)  # Conversión a entero
                obtener_docentes(elementos)  # Se llama a la función para registrar docentes
            else:
                # Se ejecuta la opción por defecto, generando un estudiante y un docente
                # pues en cada función existe un parámetro con un valor por defecto
                obtener_estudiantes()
                obtener_docentes()

        # Se solicita al usuario si desea salir del programa
        salida = input("Ingrese 'si' para salir del proceso, caso contrario use cualquier valor para seguir: ")
        
        if salida.lower() == "si":  # Si el usuario ingresa "si", se termina el bucle
            bandera = False  # Se cambia la variable de control para salir del programa

    presentar_informacion()
