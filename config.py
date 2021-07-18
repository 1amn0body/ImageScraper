from os import path, curdir, access, R_OK, W_OK
from sys import platform

import os
import yaml


class ConfigCreator:
    cfg_name: str = 'image-scraper-config.yaml'
    cfg_path = path.join(curdir, cfg_name)

    cfg_exists: bool = False
    cfg_isfile: bool = False

    read_permission: bool = False
    write_permission: bool = False

    scraper_names: list
    config_data: dict = {}

    def __init__(self, scraper_names: list = []) -> None:
        self.scraper_names = scraper_names

        self.test_permissions()

        # configure
        if self.cfg_exists:
            self.read_config()
        else:
            self.config_input()
            self.write_config()

        if 'saved_images' not in self.config_data:
            self.config_data['saved_images'] = []

        if self.config_data.get('remove_saved', False):
            self.remove_saved()

    def test_permissions(self) -> None:
        if access(curdir, R_OK):
            self.read_permission = True
        if access(curdir, W_OK):
            self.write_permission = True

        if path.exists(self.cfg_path):
            self.cfg_exists = True

            if path.isfile(self.cfg_path):
                self.cfg_isfile = True

    def read_config(self) -> None:
        if self.cfg_isfile:
            if self.read_permission:
                with open(self.cfg_path, 'rt') as f:
                    self.config_data = yaml.load(stream=f, Loader=yaml.FullLoader)
            else:
                print(f"Insufficient permissions to read config '{self.cfg_name}' from '{curdir}'.")
        else:
            print(f"'{self.cfg_name}' already exists at path '{curdir}' but is not a file...")

    def write_config(self) -> None:
        if self.write_permission:
            with open(self.cfg_path, 'wt') as f:
                yaml.dump(self.config_data, stream=f)
        else:
            print(f"Insufficient permissions to write config file '{self.cfg_name}' at '{curdir}'.")

    def update_saved(self, added_saved_images: list = []) -> None:
        self.config_data['saved_images'] = list(set(self.config_data['saved_images'] + added_saved_images))
        self.write_config()

    def config_input(self) -> None:
        # TODO setup scheduler

        while True:  # set save path for images
            try:
                _save_path: str = input("Save path for the images: ")
                _path_ok: bool = self.check_save_path(_save_path)

                if _path_ok:
                    break
            except Exception:
                not_valid_msg()

        while True:  # remove saved images?
            try:
                _remove_saved: str = input("Remove saved images (yes/no): ")[0].lower()

                if _remove_saved == 'y':
                    self.config_data['remove_saved'] = True
                elif _remove_saved == 'n':
                    self.config_data['remove_saved'] = False
                else:
                    continue
                break
            except Exception:
                not_valid_msg()

        self.add_scraper_counts()

        print()

    def add_scraper(self, scraper: dict):
        """
        scraper scheme:

        scraper = {
            'name': 'your_scraper_name'
            'long_name': 'your long name'  # is optional
        }
        """
        self.scraper_names.append(scraper)

    def add_scraper_counts(self):
        for scraper in self.scraper_names:
            while True:  # count
                try:
                    count: int = int(input(f"Image count for '{scraper.get('long_name', scraper.get('name'))}': "))

                    if count > 0:
                        self.config_data[f"count_{scraper.get('name')}"] = count
                    else:
                        self.config_data[f"count_{scraper.get('name')}"] = 0
                    break
                except TypeError:
                    print("Your input was not a number. Try again.\n")
                except Exception:
                    not_valid_msg()

    def remove_saved(self) -> None:
        save_path = self.config_data.get('save_path')
        saved_images = set(self.config_data.get('saved_images'))

        for img in saved_images:
            try:
                os.remove(path.join(save_path, img))
            except PermissionError:
                print(f"Failed to remove '{img}' at '{save_path}'.")
            except FileNotFoundError:
                print(f"File '{img}' not found at '{save_path}'.")
            except Exception as e:
                print(f"An unknown error occurred trying to remove '{img}' from '{save_path}'...")
                print(f"Details:\n{e}")

            self.config_data['saved_images'].remove(img)
        self.update_saved()

    def check_save_path(self, save_path) -> bool:
        if path.exists(save_path):
            if path.isdir(save_path):
                self.config_data['save_path'] = str(save_path)
            else:
                print('Path is not a directory...')
                return False
        else:
            try:
                if len(save_path) > 0:
                    os.mkdir(save_path)
                    self.config_data['save_path'] = str(save_path)
                else:
                    _save_path = path.join(curdir, 'images')
                    if not path.exists(_save_path):
                        os.mkdir(_save_path)

                    self.config_data['save_path'] = str(_save_path)
            except PermissionError:
                print(f"Insufficient permissions for creating directory '{str(save_path)}'...")
                return False
            except Exception as e:
                print(f"Error creating directory '{str(save_path)}'...")
                print(f"Details:\n{e}")
                return False
        return True

    def os_background_image(self):
        # TODO set background image of desktop in os specific way

        if platform.startswith('linux'):
            print('Linux')
        elif platform.startswith('darwin'):
            print('macOS')
        elif platform.startswith('win32'):
            print('Windows')

    def get_save_path(self) -> str:  # call needed info for scraper
        _save_path = path.join(curdir, 'images')
        save_path = self.config_data.get('save_path', _save_path)

        if self.check_save_path(save_path):
            return save_path
        return _save_path

    def get_scraper_count(self, name: str):
        count: int = self.config_data.get(f"count_{name}", 0)

        if count > 0:
            return count

        self.config_data[f"count_{name}"] = 0
        return 0


def not_valid_msg() -> None:
    print("Your input was not valid. Try again.\n")
