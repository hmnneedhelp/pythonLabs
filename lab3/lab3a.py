from urllib.request import urlopen
import webbrowser

url = input("Введите адрес интернет страницы: ")

if not url.startswith("https://") and not url.startswith("www."):
    url = "https://www." + url
elif not url.startswith("https://"):
    url = "https://" + url

webbrowser.open(url)
