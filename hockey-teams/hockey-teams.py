import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass
import csv


@dataclass
class Hockey:
    team: str
    year: str
    wins: str
    losses: str
    ot_losses: str
    win_pct: str
    goals_for: str
    goals_against: str
    diff: str


def main():
    with open("./hockey-teams.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(
            [
                "team",
                "year",
                "wins",
                "losses",
                "ot_losses",
                "win_pct",
                "goals_for",
                "goals_against",
                "diff",
            ]
        )

        for n in range(1, 25):
            url = f"https://www.scrapethissite.com/pages/forms/?page_num={n}"

            soup = get_soup(url)

            for data in get_data(soup):
                writer.writerow(
                    [
                        data.team,
                        data.year,
                        data.wins,
                        data.losses,
                        data.ot_losses,
                        data.win_pct,
                        data.goals_for,
                        data.goals_against,
                        data.diff,
                    ]
                )

                print(data)
                print()

    print("Hockey teams scraped successfully!")


def get_soup(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup


def get_data(soup):
    for item in soup.find_all("tr", class_="team"):
        team = item.find("td", class_="name").text.strip()
        year = item.find("td", class_="year").text.strip()
        wins = item.find("td", class_="wins").text.strip()
        losses = item.find("td", class_="losses").text.strip()
        ot_losses = item.find("td", class_="ot-losses").text.strip()
        win_pct = item.find("td", class_="pct").text.strip()
        goals_for = item.find("td", class_="gf").text.strip()
        goals_against = item.find("td", class_="ga").text.strip()
        diff = item.find("td", class_="diff").text.strip()

        yield Hockey(
            team=team,
            year=year,
            wins=wins,
            losses=losses,
            ot_losses=ot_losses,
            win_pct=win_pct,
            goals_for=goals_for,
            goals_against=goals_against,
            diff=diff,
        )


if __name__ == "__main__":
    main()
