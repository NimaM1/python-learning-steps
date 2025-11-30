from random import randint
guess_num = 6
print(f"""Hello and welcome to the "Guess the Number Game"
which the rules of the game are basically the title
of the game i'm going to pick a number between 1, 100
and if you guess it right you win!!!! you have {guess_num}
chances to guess, here we go!!!!!!!
      """)


def main():
    guess_num = 6
    number = randint(1, 101)

    while True:
        if guess_num == 0:
            print("you'r chances are done")
            again = input("wanna play again? ").strip().lower()
            if "y" in again:
                main()
            elif "n" in again:
                print("thanks fo playing. ")
                break

        print(f"you have {guess_num} guesses")
        guess = int(input(">>>> "))
        guess_num -= 1

        if guess == number:
            print("congrats you got it")
            again = input("wanna play again? ").strip().lower()
            if "y" in again:
                main()
            elif "n" in again:
                print("thanks fo playing. ")
                break

        elif guess != number:
            print("you are wrong!")


try:
    main()
except ValueError:
    print("please enter an integer")


main()
