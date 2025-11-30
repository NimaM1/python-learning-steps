import requests
import colorama
import os
import json
from datetime import datetime

print(colorama.Style.BRIGHT + """
>>>>>EXCHANGE CONVERTOR<<<<<
""")
print(colorama.Fore.CYAN + """
[1] Currency converting
[2] Convert history
[3] Exit the program
""")


def main():
    while True:
        while True:
            try:
                option = int(input(colorama.Fore.GREEN + ">>>>>> "))
                break
            except ValueError:
                print(colorama.Fore.RED +
                      "Please enter a valid number of the menu. ")
        if option == 1:
            exchange()
        elif option == 2:
            search()
        elif option == 3:
            answer = input(colorama.Fore.RED +
                           "Do you want to exit the program? ").strip().lower()
            if "y" in answer:
                print(colorama.Fore.YELLOW + "Have a nice day :)")
                break
            elif "n" in answer:
                continue


def exchange():
    # API info
    first = input(colorama.Fore.WHITE +
                  "Enter the currency you want to convert from it: ").strip().upper()
    second = input(colorama.Fore.WHITE +
                   f"Enter the currency you want '{first}' to convert to: ").strip().upper()
    url = f"https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_lYeqyzI3TE8Sj0nNX8qHspqK0GOyqikpuM3RbjdX&base_currency={first}"
    response = requests.get(url)
    data = response.json()
    number = float(input(colorama.Fore.WHITE +
                         f"Enter how much '{first}' you want to convert to '{second}': "))
    converted = round(float(data['data'][second] * number), 3)

    print(colorama.Fore.BLUE + f"{converted} , {second}")
    print(colorama.Fore.BLUE +
          f"evevry {data['data'][first]} '{first}' = {data['data'][second]} '{second}'")

    save(first, second, number, converted)


date_time = datetime.now().strftime("%Y-%m-%d %H-%M-%S")


def save(frm, to, amount, number):
    if not os.path.exists("currency_history.json") or os.stat("currency_history.json").st_size == 0:
        with open("currency_history.json", "w") as file:
            json.dump([], file, indent=4)

    new_search = {"from": frm, "to":
                  to, "amount_converted": amount, "convert_number": number, "date_time": date_time}
    with open("currency_history.json", "r") as file:
        data = json.load(file)
    data.append(new_search)
    with open("currency_history.json", "w") as file:
        json.dump(data, file, indent=4)


def search():
    with open("currency_history.json", "r") as file:
        data = json.load(file)
    print("Here are your last 5 converted currencies info: ")
    for item in data[-5:]:
        print(colorama.Fore.BLUE +
              f"{item['date_time']} > {item['convert_number']} : from '{item['from']}' to '{item['to']}', amount converted '{item['amount_converted']}' ")


main()
