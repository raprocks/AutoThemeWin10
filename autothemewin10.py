import subprocess
from datetime import datetime


def set_app_theme(light: bool) -> None:
    if light:
        theme = '1'
    else:
        theme = '0'
    print(theme, light)
    command = ['reg.exe',
               'add', r'HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize',
               '/v',
               'AppsUseLightTheme',
               '/t',
               'REG_DWORD',
               '/d',
               theme,
               '/f']
    subprocess.run(command)


def set_system_theme(light: bool) -> None:
    if light:
        theme = '1'
    else:
        theme = '0'
    print(light, theme)
    command = ['reg.exe',
               'add', r'HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize',
               '/v',
               'SystemUsesLightTheme',
               '/t',
               'REG_DWORD',
               '/d',
               theme,
               '/f']
    subprocess.run(command)


def isDay() -> bool:
    time_now = datetime.now()
    if 7 < time_now.hour > 18:
        day = True
    else:
        day = False
    return day


def runner():
    light = isDay()
    if light:
        set_app_theme(True)
        set_system_theme(True)
    else:
        set_app_theme(False)
        set_system_theme(False)


if __name__ == '__main__':
    runner()
