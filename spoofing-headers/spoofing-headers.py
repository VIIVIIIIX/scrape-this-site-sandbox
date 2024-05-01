import requests


def main():
    url = "https://www.scrapethissite.com/pages/advanced/?gotcha=headers"
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    }
    print(get_soup(url, headers))


def get_soup(url, headers):
    response = requests.get(url, headers=headers)
    return response.text


if __name__ == "__main__":
    main()
