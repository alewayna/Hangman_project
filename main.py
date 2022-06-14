#HANGMAN
#PASO 1: Lograr pedir una letra al usuario y guardar letra
#PASO 2: Crear un loop para pedir letras al usuario
#PASO 3: Condicionar el loop para que se detenga:
##          cuando ya adivinó la palabra
##          cuando pasaron 5 intentos 


def pedir_letra():
    letra = input("Adivina la letra: ")
    return letra

maximo_cantidad_de_intentos     = 5
cantidad_de_intentos_actuales   = 0
esta_el_juego_terminado         = False


while cantidad_de_intentos_actuales < maximo_cantidad_de_intentos and not esta_el_juego_terminado:
    print(pedir_letra())
    cantidad_de_intentos_actuales += 1
