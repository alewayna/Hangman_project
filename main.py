#HANGMAN
#PASO 1: lograr pedir una letra al usuario y guardar letra
def pedir_letra():
    letra = input("Adivina la letra: ")
    return letra




#PASO 2: Crear un loop para pedir letras al usuario

intentos = 0
while intentos < 5:
    print(pedir_letra())
    intentos += 1
