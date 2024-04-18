import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass
import csv


@dataclass
class Country:
    country: str
    capital: str
    population: str
    area: str


def main():
    url = "https://www.scrapethissite.com/pages/simple/"
    soup = get_soup(url)

    with open("./countries.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["country", "capital", "population", "area"])

        for data in get_data(soup):
            writer.writerow([data.country, data.capital, data.population, data.area])

            print(data)
            print()

    print("Countries scraped successfully!")


def get_soup(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    return soup


def get_data(soup):
    for item in soup.find_all("div", class_="country"):
        country = item.find("h3", class_="country-name").text.strip()
        capital = (
            item.find("div", class_="country-info")
            .find("span", class_="country-capital")
            .text
        )
        population = (
            item.find("div", class_="country-info")
            .find("span", class_="country-population")
            .text
        )
        area = (
            item.find("div", class_="country-info")
            .find("span", class_="country-area")
            .text
            + " cm²"
        )

        yield Country(
            country=country, capital=capital, population=population, area=area
        )


if __name__ == "__main__":
    main()
