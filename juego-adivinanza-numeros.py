import random
def juego_adivinanza():
    # Generar un número del 1 al 100
    numero_secreto = random.randint(1, 10)
    intentos = 0
    adivinado = False
    
    print("Bienvenido al juego adivinanza número")
    print("Debes adivinar el número del 1 al 100")
    print("¡Intenta Adivinarlo!")
    
    while not adivinado:
        # Solicitar un número del 1 al 100
        adivinanza = input("Ingrese un número del 1 al 10: ")
        
        # verificar que la entrada sea un número
        
        if adivinanza.isdigit:
            adivinanza = int(adivinanza) # lo estamos pasando de string a number
            intentos += 1
            if adivinanza < numero_secreto:
                print(f"El número secreto es mayor a {adivinanza}")
            elif adivinanza > numero_secreto:
                print(f"El número secreto es menor a {adivinanza}")
            else:
                print(f"¡FELICITACIONES has ganado! El número {adivinanza} es el secreto y lo has logrado en {intentos} intentos. ")
                adivinado = True
        else:
            print("Por favor ingrese un número válido entre el 1 al 100")

juego_adivinanza()