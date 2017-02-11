from flask import Flask, request
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import requests


def laminat33_ru(array=None,tag=None):
    if tag:
        return [ tag.find('span').text , tag.find_next().find_next().find_all('meta')[0].attrs['content'] ]
    if array:


def laminat_msc_ru(tag):
    return [tag.find('span').text, tag.find_next().find_next().find_all('meta')[0].attrs['content']] # wrong

def crummy_com(tag):
    return [ tag.find('span').text , tag.find_next().find_next().find_all('meta')[0].attrs['content'] ]


paths = {
    'laminat33.ru': laminat33_ru,
    'crummy.com' : crummy_com,
    'laminat-msc.ru' : laminat_msc_ru
}

app = Flask(__name__)

@app.route("/")
def index():

    key_word = 'Balterio'
    url = "https://laminat33.ru/category/laminat/balterio/?page = 5"

    # key_word = 'Vinca'
    # url = "https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup"

    func = paths [ urlparse(url).netloc.lower() ]
    if not func:
        return

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    arr = soup.find_all('h5')
    need = [tag for tag in arr if tag.text.find(key_word) >= 0]

    html_str = '<table width="500" bgcolor="#c0c0c0" cellspacing="0" cellpadding="5" border="1" align="left"> <caption> Товар: '
    html_str += key_word
    html_str += '</caption>  <tr> <td> Описание </td> <td> Цена </td> </tr>'


    for tag in need:
        goods, price = func(tag)
        if goods != None:
            html_str += '<tr> <td> ' + goods + ' </td> <td>' + price + '</td> </tr>'

    html_str += ' </table>'

    # print(BeautifulSoup(html_str).contents, "html.parser")

    return html_str


# @app.route("/names")
# def nm():
#     return

if __name__ == "__main__":

    app.run()
