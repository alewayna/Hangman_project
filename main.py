#HANGMAN
#PASO 1: Lograr pedir una letra al usuario y guardar letra
#PASO 2: Crear un loop para pedir letras al usuario
#PASO 3: Condicionar el loop para que se detenga:
##          cuando ya adivinó la palabra
##          cuando pasaron 5 intentos 
#PASO 4: Buscar la letra en una palabra
#PASO 5:    si la encuentro, entonces...
##          si NO la encuentro, entonces...

##Funciones
def pedir_letra():
    letra = input("Adivina la letra: ")
    return letra


#Variables
maximo_cantidad_de_intentos     = 5
cantidad_de_intentos_actuales   = 0
seguir_el_juego                 = True
palabra                         = "dinosaurio"
letra_a_buscar                  = ''
lista_de_letras_correctas       = []
lista_de_letras_incorrectas     = []



#Proceso principal
while cantidad_de_intentos_actuales < maximo_cantidad_de_intentos and seguir_el_juego:
    letra_a_buscar = pedir_letra()
    print(letra_a_buscar in palabra)


    
    cantidad_de_intentos_actuales += 1
    