from flask import Flask, render_template, request
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import requests

# CSS_selector

paths = {
    'laminat33.ru': ['div.prd-wrapper', 'span[itemprop="name"]', 'span.price'],
    'bikeparts.pythonanywhere.com' : ['div.panel', 'div.b-title', 'div.b-price'],
    'laminat-msc.ru' : []
}

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("inp.html")

@app.route("/search/")
def search():

    key_word = request.form.get("goods")
    url = request.form.get("site")

    print(key_word, url)

    # key_word = 'Balterio'
    # url = "https://laminat33.ru/category/laminat/balterio/?page=5"

    # key_word = 'Vinca'
    # url = "http://bikeparts.pythonanywhere.com/"

    try:
        sel_items, sel_goods, sel_price = paths [ urlparse(url).netloc.lower() ]
    except KeyError:
        return

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    need = [tag for tag in soup.select(sel_items) if tag.text.find(key_word) > 0]

    html_str  = """  '<div class="wa-field wa-field-email">
                <div class="wa-name"> URL </div>
                <div class="wa-value">
                <input type="text" name="url" value=""> </div> </div>'
                """

    html_str = '<table width="500" bgcolor="#c0c0c0" cellspacing="0" cellpadding="5" border="1" align="left"> <caption> Товар: '
    html_str += key_word
    html_str += '</caption>  <tr> <td> Описание </td> <td> Цена </td> </tr>'


    for tag in need:
        html_str += '<tr> <td> ' + tag.select(sel_goods)[0].text + ' </td> <td>' + tag.select(sel_price)[0].text + '</td> </tr>'

    html_str += ' </table>'

    # print(BeautifulSoup(html_str).contents, "html.parser")

    # return html_str
    key_list = [ [tag.select(sel_goods)[0].text, tag.select(sel_price)[0].text] for tag in need]

    return render_template("bs_index.html", key = key_word, list = key_list)

if __name__ == "__main__":

    app.run()

