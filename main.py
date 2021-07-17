from img_dl import XKCD, APOD
from config import ConfigCreator


def run():
    cfg = ConfigCreator()
    path = cfg.get_save_path()

    APOD(path, cfg.get_count_apod()).get_from_count()
    XKCD(path, cfg.get_count_xkcd()).get_from_count()


if __name__ == '__main__':
    run()
