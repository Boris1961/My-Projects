from bs4 import BeautifulSoup
import requests

def start ():
    response = requests.get("http://bikeparts.pythonanywhere.com/")
    # response = requests.get("https://laminat33.ru/category/laminat/balterio/?page=5")
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup
