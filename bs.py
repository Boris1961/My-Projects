from flask import Flask, request
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import requests


def laminat33_ru(tag):
    return [ tag.find('span').text , tag.find_next().find_next().find_all('meta')[0].attrs['content'] ]

paths = {
    'laminat33.ru': laminat33_ru
}

app = Flask(__name__)

@app.route("/")
def index():

    key_word = 'Balterio'
    url = "https://laminat33.ru/category/laminat/balterio/"

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
        tg, cprice = func(tag)
        if tg != None:
            html_str += '<tr> <td> ' + tg + ' </td> <td>' + cprice + '</td> </tr>'

    html_str += ' </table>'

    # print(BeautifulSoup(html_str).contents, "html.parser")

    return html_str


# @app.route("/names")
# def nm():
#     return

if __name__ == "__main__":

    app.run()
