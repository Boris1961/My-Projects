from bs4 import BeautifulSoup
import requests

def start ():
    response = requests.get("http://www.laminat-msc.ru/laminate/alpendorf/")
    # response = requests.get("https://laminat33.ru/category/laminat/balterio/?page=5")
    # response = requests.get("http://santehnika-online.ru/unitazy/podvesnye/")
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup
