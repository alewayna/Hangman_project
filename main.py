#HANGMAN
#PASO 1:  Lograr pedir una letra al usuario y guardar letra
#PASO 2:  Crear un loop para pedir letras al usuario
#PASO 3:  Condicionar el loop para que se detenga:
##          cuando ya adivinó la palabra
##          cuando pasaron 5 intentos 
#PASO 4:  Buscar la letra en una palabra
#PASO 5:    si la encuentro, agregar la letra en la lista de letras correctas
##          si NO la encuentro, sumar uno a la cantidad de intentos actuales 
###                             agregar la letra a la lista de letras incorrectas
#PASO 6:  Crear una funcion que escriba en pantalla los espacios de la palabra que se pase por parametros.
##          ejemplo: mostrar_espacios("daniel") entonces arrojará  _ _ _ _ _ _
#PASO 7:  Crear la variable "lista_de_letras_introducidas_por_el_usuario"
##        Crear la funcion "guardar_letra(letra)", esta funcion deberá almacenar en la variable nueva la letra que se le pase por parametro
#PASO 8:  Crear la funcion "guardar_letra_correcta(letra)", esta funcion deberá almacenar en la lista "lista_de_letras_correctas" la letra que se le pase por parametro
##        Crear la funcion "guardar_letra_incorrecta(letra)", esta funcion deberá almacenar en la lista "lista_de_letras_incorrectas" la letra que se le pase por parametro
#PASO 9:  Agregar en el "proceso principal" las funciones:
#           guardar_letra, guardar_letra_correcta y guardar_letra_incorrecta       
#PASO 10: En cada iteracion, imprimir en pantalla las letras incorrectas.
##              HINT(recorrer con un ciclo la lista de letras incorrectas e imprimirlas)



##Funciones
def pedir_letra():
    letra = input("Adivina la letra: ")
    return letra


def mostrar_espacios(palabra):
    """Esta funcion recibe una palabra e imprime en pantalla el caracter "_" 
    repetido la cantidad de letras de la palabra pasada por parámetro"""
    incognito = ""
    for l in palabra:
        incognito += "_ "
    print(incognito)

# Paso 7?
def guardar_letra(letra_a_guardar):
    lista_de_letras_introducidas_por_el_usuario.append(letra_a_guardar)
    

#Variables
maximo_cantidad_de_intentos     = 5
cantidad_de_intentos_actuales   = 0
seguir_el_juego                 = True
lista_de_palabras               = ['queso', 'elefante', 'dinosaurio', 'juguete', 'tomate', 'huevo']
letra_a_buscar                  = ''
lista_de_letras_correctas       = []
lista_de_letras_incorrectas     = []
lista_de_letras_introducidas_por_el_usuario = []
palabra = 'dinosaurio'

mostrar_espacios(palabra)

#Proceso principal
while cantidad_de_intentos_actuales < maximo_cantidad_de_intentos and seguir_el_juego:
    
    letra = pedir_letra()
    print(f"La letra que colocaste es: {letra}")
    

    esta_en_palabra = False
    # se usa el operador de pertenencia IN para devolver un booleano
    esta_en_palabra = letra in palabra
    if esta_en_palabra == True:
        print("La letra esta en la palabra!")
        lista_de_letras_correctas.append(letra)
    else:
        print("La letra no esta en la palabra ")
        lista_de_letras_incorrectas.append(letra)
    
    mostrar_espacios(palabra)
    # Si esta en la palabra, imprimir mensaje está
    # Si no está en la palabra, imprimir no está
    
    cantidad_de_intentos_actuales += 1    