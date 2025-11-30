import html
import random
import requests


def main():
    print("""
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
          Welcome to the >>> WHAT IS THE ANSWER ?! <<< in this game you will get 5 questions which you have 4 options
          for any of them. If you enter the right option you'll get a point for each right answer. At the end if you got 4 points
           you win else the game is over.
          -----------------------------------------------------------------------------------------------------------------------------
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
""")
    while True:
        game()
        again = input("Do you want to play again? ").strip().lower()
        if "y" in again:
            continue
        elif "n" in again:
            print("Have a nice day :) ")
            break


url = "https://opentdb.com/api.php?amount=5&type=multiple"
response = requests.get(url)
data = response.json()


def game():
    point = 0
    for index, item in enumerate(data["results"], 1):
        question = html.unescape(item["question"])
        correct = html.unescape(item["correct_answer"])
        incorrect = []
        for i in item["incorrect_answers"]:
            incorrect.append(html.unescape(i))
        options = incorrect + [correct]
        random.shuffle(options)
        print(f"\n[{index}] Question {question}")
        for i, option in enumerate(options, 1):
            print(f"[{i}] : {option}")

        while True:
            try:
                answer = int(input(">>>>>>> "))
                if 1 <= answer <= 4:
                    break
                else:
                    print("You have 4 options, your answer should be between 1 and 4.")
                    continue
            except ValueError:
                print("Plesae enter a valid number!!")

        if options[answer - 1] == correct:
            print("✅ Correct!")
            point += 1
        else:
            print(f"❌ Incorrect! The correct answer was: {correct}")

        print(f"Your Points = {point}")

    if point >= 4:
        print("""---------------------------------------------------------------------
                                    YOU WON
        --------------------------------------------------------------------------""")
    else:
        print("""----------------------------------------------------------------------
                                    GAME OVER
         -------------------------------------------------------------------------""")


main()
