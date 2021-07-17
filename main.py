from img_dl import XKCD, APOD
from config import ConfigCreator


def run():
    cfg = ConfigCreator()
    path = cfg.get_save_path()

    apod = APOD(path, cfg.get_count_apod())
    apod.get_from_count()
    cfg.update_saved(apod.saved_list)

    xkcd = XKCD(path, cfg.get_count_xkcd())
    xkcd.get_from_count()
    cfg.update_saved(xkcd.saved_list)


if __name__ == '__main__':
    run()
