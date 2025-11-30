import requests
import os
import json
import colorama

print(colorama.Style.BRIGHT + """
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**********************************************************************************
                        >>>>>>> WEATHER APP <<<<<<<<
**********************************************************************************
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^""")
print(colorama.Fore.BLUE + """
[1] The waether condition of a specific place.
[2] The weather search history.
[3] Exit the program.
""")


def main():
    while True:
        while True:
            try:
                option = int(input(">>>>> "))
                break
            except ValueError:
                print("Please enter a valid number out of the menu. ")
        if option == 1:
            weather()
        elif option == 2:
            search()
        elif option == 3:
            answer = input("Do you want to exit the program? ").strip().lower()
            if "y" in answer:
                print("Have a nice day:)")
                break
            elif "n" in answer:
                continue


def weather():
    # API info
    APIkey = "68b64baca0631c6af9b62bde727a9469"
    city = input("Enter the city >>> ")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={APIkey}"
    response = requests.get(url)
    data = response.json()

    # user Request response
    main_temp = data['main']['temp']
    feel_temp = data['main']['feels_like']
    max = data['main']['temp_max']
    min = data['main']['temp_min']

    info = colorama.Fore.YELLOW + f"""The current sky of {city} has {data['weather'][0]['description']}.
The temperature is {celecuse(main_temp)} C but feels like {celecuse(feel_temp)} C
The maximume temperature is {celecuse(max)} and the minimume temperature of today is {celecuse(min)}
        """
    print(info)
    # saving search
    save(city, main_temp)


def celecuse(n):
    return round(float(n) - 273.15, 2)


saveFile = "weather_search_history.json"


def save(city, temp):
    if not os.path.exists(f"{saveFile}") or os.stat(f"{saveFile}").st_size == 0:
        with open(f"{saveFile}", "w") as file:
            json.dump([], file, indent=4)

    newsearch = {'city': city, 'temp': temp}
    with open(f"{saveFile}", "r") as file:
        data = json.load(file)
    data.append(newsearch)
    with open(f"{saveFile}", "w") as file:
        json.dump(data, file, indent=4)


def search():
    with open(f"{saveFile}", "r") as file:
        data = json.load(file)
    print("These are your last three searches: ")
    for item in data[-3:]:
        print(f"{item['city']} : {celecuse(item['temp'])} C")


main()
