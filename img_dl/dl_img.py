from abc import ABC, abstractmethod

from os.path import basename
from os import sep, access, W_OK

import requests


class DownloadImages(ABC):
    base_url: str
    base_path: str

    saved_list: list = []
    count: int

    def __init__(self, base_path: str, count: int = 0) -> None:
        self.base_path = base_path
        self.count = count

    def save_image(self, img_link: str) -> None:
        file_name = basename(img_link)
        if access(self.base_path, W_OK):
            try:
                with open(self.base_path + sep + file_name, 'xb') as f:
                    f.write(requests.get(img_link).content)

                self.saved_list.append(file_name)
            except PermissionError:
                print(f"Insufficient permissions for writing to file '{file_name}' at path '{self.base_path}'.")
            except FileExistsError:
                print(f"File '{file_name}' already exists.")
            except Exception as e:
                print(f"Error creating file '{file_name}' at path '{self.base_path}' and or appending content.")
                print(e)
        else:
            print(f"Insufficient permissions for writing at path '{self.base_path}'.")

    def get_saved_list(self) -> list:
        return self.saved_list

    # abstract methods
    @abstractmethod
    def get_latest_image(self) -> str:
        raise NotImplementedError()

    @abstractmethod
    def get_image(self, position: object) -> str:
        raise NotImplementedError()

    @abstractmethod
    def get_from_count(self) -> None:
        raise NotImplementedError()
