from img_dl.dl_img import DownloadImages

import requests
from bs4 import BeautifulSoup
from datetime import date, timedelta


class APOD(DownloadImages):
    base_url = "https://apod.nasa.gov/apod/"

    def save_image(self, soup: BeautifulSoup) -> None:
        imgs = soup.findAll('img')

        for img in imgs:
            super(APOD, self).save_image(self.base_url + img['src'])

    def get_latest_image(self) -> None:
        url = self.base_url + 'astropix.html'

        try:
            soup = BeautifulSoup(requests.get(url).text, 'html.parser')
            self.save_image(soup)
        except requests.RequestException:
            print(f"Error requesting '{url}'.")
        except Exception:
            print('An error occurred.')

    def get_image(self, position: date) -> None:
        url = self.base_url + f"ap{position.strftime('%Y%m%d')[2:]}.html"

        try:
            soup = BeautifulSoup(requests.get(url).text, 'html.parser')
            self.save_image(soup)
        except requests.RequestException:
            print(f"Error requesting '{url}'.")
        except Exception:
            print('An error occurred.')

    def get_from_count(self) -> None:
        if self.count > 0:
            self.get_latest_image()
            pos_now = date.today()

            i = 1
            while i < self.count:
                self.get_image(pos_now - timedelta(days=i))

                i += 1
