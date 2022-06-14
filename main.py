#HANGMAN
#PASO 1: lograr pedir una letra al usuario y guardar letra
#PASO 2: Crear un loop para pedir letras al usuario
#PASO 3:    condicionar el loop para que se detenga:
##          cuando ya adivinó la palabra
##          cuando pasaron 5 intentos 


def pedir_letra():
    letra = input("Adivina la letra: ")
    return letra


cantidad_de_intentos = 0
juego_terminado = False
while cantidad_de_intentos < 5 and not juego_terminado:
    print(pedir_letra())
    cantidad_de_intentos += 1
