from sys import platform

import os
import ctypes


class SetBackground:
    def __init__(self, img_path) -> None:
        img_path: str = str(os.path.join(img_path) if os.path.isabs(img_path) else os.path.abspath(img_path))

        p = platform
        if p.startswith('win32'):  # or p.startswith('cygwin'):
            self.Windows(img_path)
        elif p.startswith('darwin'):
            self.Mac(img_path)
        elif p.startswith('linux'):
            self.Linux(img_path)
        else:
            print('Unsupported Operating System')

    class Windows:
        # https://github.com/judge2020/ghstatic.judge.sh/blob/master/ducky/wallpaper.ps1
        # use win api (PyWin32)
        # https://stackoverflow.com/questions/1977694/how-can-i-change-my-desktop-background-with-python
        # https://docs.python.org/3/library/winreg.html#winreg.OpenKey
        def __init__(self, img_path: str) -> None:
            SPI_SETDESKWALLPAPER = 0x0014  # =20

            ctypes.windll.user32.SystemparametersInfoA(SPI_SETDESKWALLPAPER, 0, img_path, 0)

    class Mac:
        def __init__(self, img_path: str) -> None:
            pass

    class Linux:
        def __init__(self, img_path: str) -> None:
            # https://stackoverflow.com/questions/2035657/what-is-my-current-desktop-environment/21213358

            desktop_env: str = os.environ.get('DESKTOP_SESSION').lower()

            if desktop_env.startswith('kde') or desktop_env.startswith('kubuntu'):
                self.kde_plasma()
            elif desktop_env.startswith('gnome'):
                pass
            elif desktop_env.startswith('lxde') or desktop_env.startswith('lubuntu'):
                pass
            else:
                print('Unsupported or no desktop environment found.')

        def kde_plasma(self) -> None:
            pass

        def gnome(self) -> None:
            pass

        def lxde(self) -> None:
            pass
