from img_dl.dl_img import DlImg

import requests
from bs4 import BeautifulSoup
from os.path import sep
from datetime import date, timedelta


class APOD(DlImg):
    base_url = "https://apod.nasa.gov/"

    soup = BeautifulSoup(requests.get(base_url).text, 'html.parser')

    position: date

    def get_latest_image(self) -> str:
        pass

    def get_image(self) -> str:
        pass

    def get_from_count(self) -> None:
        pass
