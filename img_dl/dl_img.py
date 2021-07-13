from abc import ABC, abstractmethod

import requests
from bs4 import BeautifulSoup
from os.path import basename, sep


class DlImg(ABC):
    base_url: str
    soup: BeautifulSoup

    saved_list: list = []
    base_path: str
    count: int

    position: object

    def __init__(self, base_path: str, count: int) -> None:
        self.base_path = base_path
        self.count = count

    def save_image(self, img_link: str) -> None:
        file_name = basename(img_link)

        try:
            with open(self.base_path + sep + file_name, 'xb') as f:
                f.write(requests.get(img_link).content)

            self.saved_list.append(file_name)
        except PermissionError:
            print(f"Writing of file '{file_name}' not allowed.")
        except FileExistsError:
            print(f"File '{file_name}' already exists.")
        except Exception:
            print(f"Error creating file '{file_name}' and or appending content.")

    def get_saved_list(self) -> list:
        return self.saved_list

    # abstract methods
    @abstractmethod
    def get_latest_image(self) -> str:
        raise NotImplementedError()

    @abstractmethod
    def get_image(self) -> str:
        raise NotImplementedError()

    @abstractmethod
    def get_from_count(self) -> None:
        raise NotImplementedError()
