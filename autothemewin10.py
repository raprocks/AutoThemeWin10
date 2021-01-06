import subprocess
from datetime import datetime
import typer
app = typer.Typer()


@app.command()
def set_app_theme(light: bool) -> None:
    if light:
        theme = '1'
    else:
        theme = '0'
    command = ['reg.exe',
               'add',
               r'HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize',
               '/v',
               'AppsUseLightTheme',
               '/t',
               'REG_DWORD',
               '/d',
               theme,
               '/f']
    subprocess.run(command)


@app.command()
def set_system_theme(light: bool) -> None:
    if light:
        theme = '1'
    else:
        theme = '0'
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
    if time_now.hour > 7 and time_now.hour < 18:
        day = True
    else:
        day = False
    return day


@app.command()
def register_scheduled_task():
    command = ["schtasks.exe",
               r"/Create",
               r"/SC",
               r"HOURLY",
               r"/D",
               r"*",
               r"/M",
               r"*",
               r"/TN",
               r"AutoThemeWin10",
               r"/TR",
               r"autothemewin10"]
    subprocess.command(command)


@app.command()
def runner():
    light = isDay()
    if light:
        set_app_theme(True)
        set_system_theme(True)
    else:
        set_app_theme(False)
        set_system_theme(False)


if __name__ == '__main__':
    app()
