from img_dl.dl_img import DlImg

import requests
from bs4 import BeautifulSoup
from os.path import sep


class XKCD(DlImg):
    base_url = "https://xkcd.com/"

    soup = BeautifulSoup(requests.get(base_url).text, 'html.parser')

    position: int

    def get_latest_image(self) -> str:
        pass

    def get_image(self) -> str:
        pass

    def get_from_count(self) -> None:
        pass
