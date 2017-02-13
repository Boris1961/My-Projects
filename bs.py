from flask import Flask, render_template, request
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import requests

# CSS_selector

paths = {
    'laminat33.ru': ['div.prd-wrapper', 'img[src]', 'span[itemprop="name"]', 'span.price'],
    'bikeparts.pythonanywhere.com' : ['div.panel', '', 'div.b-title', 'div.b-price'],
    'laminat-msc.ru' : []
}

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("inp.html")

@app.route("/search", methods=["post"])
def search():

    key_word = request.form.get("goods")
    url = request.form.get("site")

    # key_word = 'Balterio'
    # url = "https://laminat33.ru/category/laminat/balterio/?page=5"

    netloc = urlparse(url).netloc.lower()
    if paths.get(netloc) == None:
        key_word = 'Balterio'
        url = "https://laminat33.ru/category/laminat/balterio/?page=5"

    netloc = urlparse(url).scheme.lower() + ':\\' + urlparse(url).netloc.lower()
    sel_items, sel_img, sel_goods, sel_price = paths[netloc]

    try:
        response = requests.get(url)
    except:
        return

    soup = BeautifulSoup(response.content, 'html.parser')

    need = [tag for tag in soup.select(sel_items) if tag.text.find(key_word) > 0]

    key_list = [ [ netloc+tag.select(sel_img)[0]['src'], tag.select(sel_goods)[0].text, tag.select(sel_price)[0].text ] for tag in need ]

    return render_template("bs_index.html", key = key_word, list = key_list)

if __name__ == "__main__":

    app.run()
