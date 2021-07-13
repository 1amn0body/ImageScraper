from img_dl.dl_img import DownloadImages

import requests
from bs4 import BeautifulSoup
from datetime import date, timedelta


class APOD(DownloadImages):
    base_url = "https://apod.nasa.gov/"

    def get_latest_image(self) -> None:
        soup = BeautifulSoup(requests.get(self.base_url).text, 'html.parser')
        pass

    def get_image(self, position: date) -> None:
        pass

    def get_from_count(self) -> None:
        pass
