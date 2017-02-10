from bs4 import BeautifulSoup
import requests

def start3 ():
    response = requests.get("https://laminat33.ru/category/laminat/balterio/")
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup
