"""

"""
def obtener_reporte(tipo, lista):

    reporte = ""
     
    if tipo == 1:
        reporte = "\nListado de Estudiantes\n"  # Cadena para almacenar la lista de docentes
        
        # Construcción del reporte de estudiantes a partir de la lista de estudiantes
        for i in lista:
            reporte = f"{reporte}{i[0]} {i[1]} -correo:{i[2]}-, edad:{i[3]}\n"
        guardar_informacion(reporte, 1)
    else:
        if tipo == 2:
            reporte = "\nListado de Docentes\n"  # Cadena para almacenar
            
            # Construcción del reporte de docentes a partir de la lista de docentes
            for i in lista:
                reporte = f"{reporte}{i[0]} {i[1]} -ciudad de residencia:{i[2]}\n"

            guardar_informacion(reporte, 2)
    return reporte


def guardar_informacion(cadena_final, tipo):
    """
    Función que guarda la información recibida en un archivo de texto.
    
    Parámetros:
    cadena_final (str): Cadena de texto que contiene la información 
                        que se almacenará en el archivo.
    """
    # El archivo se abrirá y cerrará automáticamente al salir del bloque with
    # Se usa el modo "w" para escritura, lo que sobrescribe el contenido del archivo si ya existe.
    
    if tipo == 1:
        cadena = "data/informacion-estudiantes.txt"
    else:
        if tipo == 2:
            cadena = "data/informacion-docentes.txt"

    with open(cadena, "a") as archivo:
        # Se escribe la información en el archivo usando write()
        archivo.write(f"{cadena_final}")  # Se guarda la cadena en el archivo
    
    # Al salir del bloque 'with', el archivo se cierra automáticamente

def presentar_informacion():
    # 1. Utilizar la estructura "with" para abrir el archivo en modo lectura ("r")
    # El archivo se abrirá y cerrará automáticamente al salir del bloque with
    
    with open("data/informacion-estudiantes.txt", "r") as archivo:
        # 2. Leer todas las líneas del archivo y almacenarlas en una lista
        textos = archivo.readlines()
        for t in textos:
            print(t)

    with open("data/informacion-docentes.txt", "r") as archivo:
        # 2. Leer todas las líneas del archivo y almacenarlas en una lista
        textos = archivo.readlines()
        for t in textos:
            print(t)
