from img_dl import XKCD, APOD
from config import ConfigCreator


def run():
    cfg = ConfigCreator(scraper_names=[
        {
            'name': 'apod',
            'long_name': 'Astronomy Picture of the Day'
        },
        {
            'name': 'xkcd',
            'long_name': 'XKCD'
        }
    ])
    path = cfg.get_save_path()

    print('Downloading APOD...')
    apod = APOD(path, cfg.get_scraper_count('apod'))
    apod.get_from_count()
    cfg.update_saved(apod.saved_list)
    print('Done.\n')

    print('Downloading XKCD...')
    xkcd = XKCD(path, cfg.get_scraper_count('xkcd'))
    xkcd.get_from_count()
    cfg.update_saved(xkcd.saved_list)
    print('Done.')


if __name__ == '__main__':
    run()
