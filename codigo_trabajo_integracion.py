# Agrega un directorio o archivo a la estructura del árbol (en lista anidada).
def agregar_directorio_o_archivo(arbol, ruta, tipo): 
    if not ruta:
        return
    nombre = ruta[0] 


# Se agrega un archivo a una lista que representa un directorio, pero solo si el archivo aún no existe.
    if len(ruta) == 1 and tipo == 'archivo': 
        if nombre not in arbol: 
            arbol.append(nombre) 
        else:
            print(f"El archivo '{nombre}' ya existe en este directorio.") 
        return
    

# Buscar si ya existe un directorio con ese nombre, si lo encuentra sigue agregando los niveles restantes de la ruta forma recursiva
    for item in arbol: 
        if isinstance(item, list) and item[0] == nombre: 
            agregar_directorio_o_archivo(item[1], ruta[1:], tipo)
            return 

    

    # Si no existe, crear nuevo directorio
    nuevo_directorio = [nombre, []] 
    arbol.append(nuevo_directorio) 
    agregar_directorio_o_archivo(nuevo_directorio[1], ruta[1:], tipo)

    #Busqueda en preorden de un archivo determinado
def buscar_archivo_preorden(arbol, nombre_archivo):

    for item in arbol: 
        if isinstance(item, list): 
            resultado = buscar_archivo_preorden(item[1], nombre_archivo) 
            if resultado:
                return resultado 
        elif item == nombre_archivo: 
            return item 
    return None

# Solicita una ruta y tipo al usuario.
def ingresar_directorio_y_archivo():
    ruta = input("Ingresa la ruta (ejemplo: home/user/docs/archivo.txt): ").strip() 
    ruta_split = ruta.split('/')
    tipo = input("¿Es un directorio o un archivo? (directorio/archivo): ").strip().lower()
    return ruta_split, tipo 


#================================================== Programa principal ============================================
"""
Este código simula un sistema de carpetas y archivos usando listas anidadas en un estructura de albol, permitiendo:

Crear un árbol de directorios.

Agregar archivos o directorios.

Buscar archivos.

Mostrar la estructura completa del árbol.

"""
arbol = [] #Se crea el árbol principal como una lista vacía.


# Se Agregan  elementos al árbol
while True:  #Se crea un bucle para ingresar directorio o archivo
    ruta, tipo = ingresar_directorio_y_archivo() #Pide al usuario que ingrese una ruta y si es un archivo o carpeta.
    agregar_directorio_o_archivo(arbol, ruta, tipo) #Llama a agregar_directorio_o_archivo() para construir el árbol.

    continuar = input("¿Deseas agregar otro directorio/archivo? (s/n): ").strip().lower() #Pregunta si quiere agregar dorectorio o archivo
    if continuar != 's':
        break  #si coloca "n" se sale del bucle

#Funcion para imprimir el arbol(forma jerarquica)

def imprimir_arbol(arbol, nivel=0):# Define la función con un parámetro nivel (por defecto 0), que se usa para dar sangrías y mostrar la profundidad.
    for item in arbol: #Recorre cada elemento dentro del árbol actual.
        if isinstance(item, list): #Verifica si el item es una lista, lo que significa que es un directorio.
            print("  " * nivel + f"[{item[0]}]")#Imprime el nombre del directorio con sangría dependiendo del nivel.[carpetas]
            imprimir_arbol(item[1], nivel + 1) #Llama a sí misma para imprimir lo que hay dentro de esa carpeta, aumentando el nivel para que haya más sangría.
        else:
            print("  " * nivel + f"- {item}")#Si el item no es una lista, entonces es un archivo.Lo imprime con guión - y sangría según el nivel.

# Búsqueda de archivo
nombre_a_buscar = input("Ingresa el nombre del archivo a buscar: ").strip() # Pide al usuario un nombre de archivo y llama a la función buscar_archivo_preorden 
resultado = buscar_archivo_preorden(arbol, nombre_a_buscar)

# Mostar si se encontro el archivo y imprimir el arbol 
if resultado:
    print(f"Archivo encontrado: {resultado}" )
else:
    print(f"Archivo '{nombre_a_buscar}' no encontrado.")
    
imprimir_arbol(arbol)