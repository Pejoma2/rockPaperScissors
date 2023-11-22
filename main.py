import random

rounds = 1

while True:
    print("")
    print("")
    print("")
    print("*" * 20)
    print("ROUND", rounds)
    print("*" * 20)
    print("")

    options = ("piedra", "papel", "tijera")

    user_option = input("piedra, papel o tijera => ")
    user_option = user_option.lower()

    if not user_option in options:
        print("No es una opció válida...")

    computer_option = random.choice(options)

    print("User Option => ", user_option)
    print("Computer Option => ", computer_option)

    if user_option == computer_option:
        print("empate")
    elif user_option == "piedra":
        if computer_option == "tijera":
            print("PIEDRA gana a Tijera => User ganó")
        else:
            print("PAPEL gana a Piedra => CPU ganó")
    elif user_option == "papel":
        if computer_option == "piedra":
            print("PAPEL gana a Piedra => User ganó")
        else:
            print("TIJERA gana a Papel => CPU ganó")
    elif user_option == "tijera":
        if computer_option == "papel":
            print("TIJERA gana a Papel => User ganó")
        else:
            print("PIEDRA gana a Tijera => CPU ganó")