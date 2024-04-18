import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass
import csv


@dataclass
class Species:
    species: str
    about: str


def main():
    url = "https://www.scrapethissite.com/pages/frames/?frame=i"

    soup = get_soup(url)
    with open("./species.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["species", "about"])

        for link in get_links(soup):
            soup = get_soup(link)

            for data in get_data(soup):
                writer.writerow([data.species, data.about])

                print(data)
                print()

    print("Species scraped successfully!")


def get_soup(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup


def get_links(soup):
    learn_more_links = list()
    for item in soup.find_all("div", class_="turtle-family-card"):
        learn_more_links.append(
            "https://www.scrapethissite.com"
            + item.find("a", class_="btn btn-default btn-xs").get("href")
        )
    return learn_more_links


def get_data(soup):
    species = soup.find("h3", class_="family-name").text
    about = soup.find("p", class_="lead").text.strip()
    yield Species(species=species, about=about)


if __name__ == "__main__":
    main()
