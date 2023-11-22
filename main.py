import random

computer_wins = 0
user_wins = 0
rounds = 1

while True:
    print("")
    print("")
    print("")
    print("*" * 20)
    print("ROUND", rounds)
    print("*" * 20)
    print("")

    print("CPU WINS =>", computer_wins)
    print("USER WINS =>", user_wins)

    options = ("piedra", "papel", "tijera")

    user_option = input("piedra, papel o tijera => ")
    user_option = user_option.lower()

    if not user_option in options:
        print("No es una opción válida...")
        continue

    computer_option = random.choice(options)

    print("User Option => ", user_option)
    print("Computer Option => ", computer_option)

    if user_option == computer_option:
        print("empate")
    elif user_option == "piedra":
        if computer_option == "tijera":
            print("PIEDRA gana a Tijera => User ganó")
            user_wins += 1
        else:
            print("PAPEL gana a Piedra => CPU ganó")
            computer_wins += 1

    elif user_option == "papel":
        if computer_option == "piedra":
            print("PAPEL gana a Piedra => User ganó")
            user_wins += 1
        else:
            print("TIJERA gana a Papel => CPU ganó")
            computer_wins += 1
    elif user_option == "tijera":
        if computer_option == "papel":
            print("TIJERA gana a Papel => User ganó")
            user_wins += 1
        else:
            print("PIEDRA gana a Tijera => CPU ganó")
            computer_wins += 1
    
    if computer_wins == 2:
        print("🥳🥳El CPU ha ganado!🥳🥳")
        break

    if user_wins == 2:
        print("🥳🥳El USER ha ganado!🥳🥳")
        break

    rounds += 1