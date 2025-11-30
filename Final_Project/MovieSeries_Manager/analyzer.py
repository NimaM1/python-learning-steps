import json
from collections import Counter
import statistics
import colorama


def main():
    genrezer()
    imdbezer()


def genrezer(myfile):
    with open(myfile, "r")as file:
        data = json.load(file)
    all_genres = []

    for line in data:
        all_genres.extend(line['genre'].split(", "))

    most_commen = Counter(all_genres).most_common(3)
    print(colorama.Fore.WHITE + "\nYour most commen watch list Genres: ")
    print(colorama.Fore.WHITE + f"({most_commen})")


def imdbezer(myfile):
    with open(myfile, "r") as file:
        data = json.load(file)
    imdb_scores = []
    for line in data:
        imdb_raw = line.get("imdb", "0/10")
        try:
            score = float(imdb_raw.split("/")[0])
            imdb_scores.append(score)
        except ValueError:
            continue

    if imdb_scores:
        average = statistics.mean(imdb_scores)
        print(colorama.Fore.WHITE +
              f"\nThis is your list's average IMDB rate: {average:.2f}")
    else:
        print(colorama.Fore.WHITE + "No valid IMDb scores found.")


if __name__ == "__main__":
    main()
