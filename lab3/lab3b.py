from urllib.request import urlopen
import webbrowser
import time
import subprocess

url = input("Введите адрес интернет страницы: ")

if not url.startswith("https://") and not url.startswith("www."):
    url = "https://www." + url
elif not url.startswith("https://"):
    url = "https://" + url

webbrowser.open(url)

delay = int(input("Введите временную задержку в секундах: "))
time.sleep(delay)

executablefile = input("Введите путь к исполняемому файлу (exe): ")
subprocess.Popen(executablefile)
