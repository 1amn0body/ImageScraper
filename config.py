from os import path, curdir, access, R_OK, W_OK
import yaml


class ConfigCreator:
    cfg_name: str = 'image-scraper-config.yaml'
    cfg_path = curdir.join(cfg_name)

    cfg_exists: bool = False
    cfg_isfile: bool = False

    read_permission: bool = False
    write_permission: bool = False

    config_data: dict = {}

    def __init__(self):
        self.test_permissions()

        # configure
        if self.cfg_exists:
            self.read_config()
        else:
            self.write_config()

    def test_permissions(self):
        if access(curdir, R_OK):
            self.read_permission = True
        if access(curdir, W_OK):
            self.write_permission = True

        if path.exists(self.cfg_path):
            self.cfg_exists = True

            if path.isfile(self.cfg_path):
                self.cfg_isfile = True

    def read_config(self):
        if self.cfg_isfile:
            if self.read_permission:
                with open(self.cfg_path, 'rt') as f:
                    self.config_data = yaml.load(stream=f, Loader=yaml.FullLoader)

                # TODO
            else:
                print(f"Insufficient permissions to read config '{self.cfg_name}' from '{curdir}'.")
        else:
            print(f"'{self.cfg_name}' already exists at path '{curdir}' but is not a file...")
            return

    def remove_saved(self):
        # TODO
        pass

    def write_config(self):
        if self.write_permission:
            self.config_input()
            # TODO
        else:
            print(f"Insufficient permissions to write config file '{self.cfg_name}' at '{curdir}'.")

    def update_saved(self):
        if self.write_permission:
            with open(self.cfg_path, 'wt+') as f:
                # TODO
                yaml.dump(self.config_data.get('saved'), stream=f)
        else:
            print(f"Insufficient permissions to write config file '{self.cfg_name}' at '{curdir}'.")

    def config_input(self):
        while True:  # remove saved?
            try:
                remove_saved: str = input("Remove saved images (y/n): ")[0].lower()

                if remove_saved == 'y':
                    self.config_data['remove_saved'] = True
                elif remove_saved == 'n':
                    self.config_data['remove_saved'] = False
                else:
                    continue
                break
            except Exception:
                not_valid_msg()

        while True:  # xkcd
            try:
                count_xkcd: int = int(input("Image count for xkcd: "))

                if count_xkcd > 0:
                    self.config_data['count_xkcd'] = count_xkcd
                else:
                    self.config_data['count_xkcd'] = 0
                break
            except TypeError:
                print("Your input was not a number. Try again.\n")
            except Exception:
                not_valid_msg()

        while True:  # apod
            try:
                count_apod: int = int(input("Image count for 'Astronomy Picture of the Day': "))

                if count_apod > 0:
                    self.config_data['count_apod'] = count_apod
                else:
                    self.config_data['count_apod'] = 0
                break
            except TypeError:
                print("Your input was not a number. Try again.\n")
            except Exception:
                not_valid_msg()

    # TODO path (creation if not existent), setup scheduler


def not_valid_msg():
    print("Your input was not valid. Try again.\n")
