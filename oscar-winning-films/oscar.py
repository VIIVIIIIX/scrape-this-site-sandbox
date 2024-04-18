import requests
from dataclasses import dataclass
import csv


@dataclass
class Movie:
    title: str
    year: str
    nominations: str
    awards: str
    best_movie_of_the_year: str


def main():
    with open("./oscar.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["title", "year", "nominations", "awards", "best_movie"])

        for n in range(2015, 2009, -1):
            url = f"https://www.scrapethissite.com/pages/ajax-javascript/?ajax=true&year={n}"
            json = get_json(url)

            for data in get_data(json):
                writer.writerow(
                    [
                        data.title,
                        data.year,
                        data.nominations,
                        data.awards,
                        data.best_movie_of_the_year,
                    ]
                )

                print(data)
                print()

    print("Movies scraped successfully!")


def get_json(url):
    response = requests.get(url)
    return response.json()


def get_data(json):
    for n in range(len(json)):
        title = json[n]["title"].strip()
        year = json[n]["year"]
        nominations = json[n]["nominations"]
        awards = json[n]["awards"]
        best_movie_of_the_year = "Yes" if "best_picture" in json[n].keys() else "No"

        yield Movie(
            title=title,
            year=year,
            nominations=nominations,
            awards=awards,
            best_movie_of_the_year=best_movie_of_the_year,
        )


if __name__ == "__main__":
    main()
