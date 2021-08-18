from abc import ABC, abstractmethod
from os import sep, access, W_OK
from os.path import basename

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
                print(f"Trying to save '{file_name}'...", end=' ')
                with open(self.base_path + sep + file_name, 'xb') as f:
                    f.write(requests.get(img_link).content)
                print("Done")
                self.saved_list.append(file_name)
            except PermissionError:
                print(f"Insufficient permissions for writing to file at path '{self.base_path}'.")
            except FileExistsError:
                print(f"File already exists.")
                self.saved_list.append(file_name)
            except Exception as e:
                print(f"Error creating file at path '{self.base_path}' and or appending content.")
                print(e)

        else:
            print(f"Insufficient permissions for writing at path '{self.base_path}'.")

    def get_saved_list(self) -> list:
        return self.saved_list

    # abstract methods
    @abstractmethod
    def get_latest_image(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def get_image(self, position: object) -> None:
        raise NotImplementedError()

    @abstractmethod
    def get_from_count(self) -> None:
        raise NotImplementedError()
