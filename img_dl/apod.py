from img_dl import DownloadImages
from bs4 import BeautifulSoup
from datetime import date, timedelta

import requests


class APOD(DownloadImages):
    base_url = "https://apod.nasa.gov/apod/"

    def save_image(self, soup: BeautifulSoup) -> None:
        img_s = soup.findAll('img')

        for img in img_s:
            super(APOD, self).save_image(self.base_url + img['src'])

    def get_latest_image(self) -> None:
        url = self.base_url + 'astropix.html'

        try:
            soup = BeautifulSoup(requests.get(url).text, 'html.parser')
            self.save_image(soup)
        except requests.RequestException:
            print(f"Error requesting '{url}'.")
        except Exception as e:
            print('An error occurred.')
            print(f"Details:\n{e}")

    def get_image(self, position: date) -> None:
        url = self.base_url + f"ap{position.strftime('%Y%m%d')[2:]}.html"

        try:
            soup = BeautifulSoup(requests.get(url).text, 'html.parser')
            self.save_image(soup)
        except requests.RequestException:
            print(f"Error requesting '{url}'.")
        except Exception as e:
            print('An error occurred.')
            print(f"Details:\n{e}")

    def get_from_count(self) -> None:
        if self.count > 0:
            self.get_latest_image()
            pos_now = date.today()

            i = 1
            while i < self.count:
                self.get_image(pos_now - timedelta(days=i))
                i += 1
