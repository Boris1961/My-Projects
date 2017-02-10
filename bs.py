from flask import Flask, request
from bs4 import BeautifulSoup
import requests
import re


app = Flask(__name__)

@app.route("/")
def index():

    key_word = 'Balterio'

    response = requests.get("https://laminat33.ru/category/laminat/balterio/")
    soup = BeautifulSoup(response.content, 'html.parser')

    arr = soup.find_all('h5')
    need = [tag for tag in arr if tag.text.find(key_word) >= 0]

    html_str = '<table width="500" bgcolor="#c0c0c0" cellspacing="0" cellpadding="5" border="1" align="left"> <caption> Товар: '
    html_str += key_word
    html_str += '</caption>  <tr> <td> Описание </td> <td> Цена </td> </tr>'


    for tag in need:
        tg = tag.find('span').text
        if tg != None:
            cprice = tag.find_next().find_next().find_all('meta')[0].attrs['content']
            html_str += '<tr> <td> ' + tg + ' </td> <td>' + cprice + '</td> </tr>'

    html_str += ' </table>'

    # print(BeautifulSoup(html_str).contents, "html.parser")

    return html_str


# @app.route("/names")
# def nm():
#     return

if __name__ == "__main__":

    app.run()
