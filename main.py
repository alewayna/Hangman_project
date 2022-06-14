#HANGMAN
#PASO 1: lograr pedir una letra al usuario y guardar letra
#PASO 2: Crear un loop para pedir letras al usuario
#PASO 3:    condicionar el loop para que se detenga:
##          cuando ya adivinó la palabra
##          cuando pasaron 5 intentos 


def pedir_letra():
    letra = input("Adivina la letra: ")
    return letra


intentos = 0
while intentos < 5:
    print(pedir_letra())
    intentos += 1
