from os import path, curdir, sep, access, R_OK, W_OK
import yaml


class ConfigCreator:
    cfg_name: str = 'image-scraper-config.yaml'
    yaml_data: yaml

    cfg_exists: bool = False
    cfg_isfile: bool = False

    read_permission: bool = False
    write_permission: bool = False

    def __init__(self):
        f_name = curdir.join(self.cfg_name)

        if access(curdir, R_OK):
            self.read_permission = True
        if access(curdir, W_OK):
            self.write_permission = True

        if path.exists(f_name):
            self.cfg_exists = True

            if path.isfile(f_name):
                self.cfg_isfile = True

        # configure
        if self.cfg_exists and self.cfg_isfile:
            if self.read_permission:
                pass
            else:
                pass
        elif self.cfg_exists and not self.cfg_isfile:
            pass
        else:
            if self.write_permission:
                pass
            else:
                pass
