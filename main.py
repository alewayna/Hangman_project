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
#PASO 8:  Modificar la funcion mostrar_espacios para que sustituya los espacios por la letra correcta
#PASO 9:  Agregar en el "proceso principal" las funciones:
#           guardar_letra, guardar_letra_correcta y guardar_letra_incorrecta       
#PASO 10: En cada iteracion, imprimir en pantalla las letras incorrectas.
##              HINT(recorrer con un ciclo la lista de letras incorrectas e imprimirlas)



##Funciones

def pedir_letra():
    letra = input("Adivina la letra: ")
    return letra


def mostrar_espacios(palabra, lista_de_letras_correctas):
    """Esta funcion recibe una palabra e imprime en pantalla el caracter "_" 
    repetido la cantidad de letras de la palabra pasada por parámetro
    Por cada iteracion (letra encontrada) voy agregar una barrita o un espacio a la variable incognito
    y al final de eso voy a imprimir incognito"""
    incognito = ""
    for l in palabra:
        letra_correcta = l in lista_de_letras_correctas
        if letra_correcta == True:
            incognito += l
        else:
            incognito += "_ "
        
        # print(f'L= {l}')
        # print(f'incognito= {incognito}')
    print(incognito)

# Paso 7?
def guardar_letra(letra_a_guardar):
    lista_de_letras_introducidas_por_el_usuario.append(letra_a_guardar)
    

#Variables
maximo_cantidad_de_intentos_fallidos = 5
cantidad_de_intentos_fallidos        = 0
seguir_el_juego                      = True
lista_de_palabras                    = ['queso', 'elefante', 'dinosaurio', 'juguete', 'tomate', 'huevo']
letra_a_buscar                       = ''
lista_de_letras_correctas            = []
lista_de_letras_incorrectas          = []
lista_de_letras_introducidas_por_el_usuario = []
palabra = 'dinosaurio'

mostrar_espacios(palabra, lista_de_letras_correctas)

#Proceso principal
while cantidad_de_intentos_fallidos < maximo_cantidad_de_intentos_fallidos and seguir_el_juego:
    
    letra = pedir_letra()
    print(f"La letra que colocaste es: {letra}")
    guardar_letra(letra)

    esta_en_palabra = False
    # se usa el operador de pertenencia IN para devolver un booleano
    esta_en_palabra = letra in palabra
    if esta_en_palabra == True:
        print("La letra esta en la palabra!")
        lista_de_letras_correctas.append(letra)
        
    else:
        print("La letra no esta en la palabra ")
        lista_de_letras_incorrectas.append(letra)
        cantidad_de_intentos_fallidos += 1
    print("\n")
    print(f"Letras correctas: {lista_de_letras_correctas}")
    print(f"Letras incorrectas: {lista_de_letras_incorrectas}")
    print("\n")
    mostrar_espacios(palabra, lista_de_letras_correctas)
    # Si esta en la palabra, imprimir mensaje está
    # Si no está en la palabra, imprimir no está

        