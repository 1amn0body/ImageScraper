from img_dl import XKCD, APOD


def run():
    path = ""

    APOD(path, 10).get_from_count()

    XKCD(path, 10).get_from_count()
    pass


if __name__ == '__main__':
    run()
