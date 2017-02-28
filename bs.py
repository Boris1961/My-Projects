from flask import Flask, render_template, request
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import requests
import csv

# CSS_selector
# tag - тэг содержащий инфо о товаре
# sel_pos - строка <CSS селектор тэга товарного параметра (название, цена, изображение)>[$$$<имя аттрибута искомого параметра>] >
# если $$$ отсутствует, значит параметр содержится в .text тэга
# возвращает строку товарного параметра

def get_pos(tag, sel_pos):
    sel_list = sel_pos.split('$$$')
    try:
        return tag.select_one(sel_list[0])[sel_list[1]] if len(sel_list)>1 else tag.select_one(sel_list[0]).text
    except:
        return 'Чёрте что!'

def get_sites():
    with open('sites.csv', newline='') as f:
        reader = csv.DictReader(f)
        dicts = {d['key_netloc']: [d['key_pos'], d['key_img'], d['key_goods'], d['key_price']] for d in reader}
    return dicts

'''

    Структура момента: {    key_netloc: <имя(локация) сайта>
                            key_pos:  <селектор товарной позиции (контейнера)>
                            key_img:  <селектор картинки внутри контейнера>
                            key_goods: <селектор наименования внутри контейнера>
                            key_price: <селектор цены внутри контейнера>
                       }



    sites = {
                www.laminat-msc.ru,td > table[cellpadding],img[src]$$$src,"span[itemprop=""name""]",span.catalog-price
                laminat33.ru,div.prd-wrapper,img[src]$$$src,"span[itemprop=""name""]",span.price
                santehnika-online.ru,"div[itemprop=""itemListElement""]",img$$$src,div.vidname > a,"meta[itemprop=""price""]$$$content"
                bikeparts.pythonanywhere.com,div.panel,,div.b-title,div.b-price
            }

'''

app = Flask(__name__)


def tst_decor(mes):
    print(mes, app.view_functions)
    def decor(fun):
        def wrap():
            return fun
        return wrap
    return decor


@app.route("/")
def my_index():
    return render_template("index.html")

@app.route("/search", methods=["post"])
def search():

    key_word = request.form.get("goods")
    url = request.form.get("site")
    netloc = urlparse(url).netloc.lower()

    sites = get_sites()
    if not sites.get(netloc):
        print('Cайт ' + netloc + ' пока не обработан.')
        key_word = 'Balterio'
        url = "https://laminat33.ru/category/laminat/balterio/?page=5"
        netloc = "laminat33.ru"

    sel_items, sel_img, sel_goods, sel_price = sites[netloc]
    netloc = urlparse(url).scheme.lower() + '://' + urlparse(url).netloc.lower()

    try:
        response = requests.get(url)
    except:
        print("URL - инвалид")
        return

    soup = BeautifulSoup(response.content, 'html.parser')

    if key_word == '':
        need = [ tag for tag in soup.select(sel_items)]
        key_word = 'Всякий-всякий'
    else:
        need = [tag for tag in soup.select(sel_items) if tag.text.find(key_word)>=0]

    key_list = [["static/img/Donald-Trump.jpg" if not sel_img else
                (netloc+get_pos(tag, sel_img) if get_pos(tag, sel_img)[:2]!="//" else get_pos(tag,sel_img)),
                get_pos(tag,sel_goods), # наименование
                get_pos(tag,sel_price)] # цена
                 for tag in need ]

    return render_template("search.html", key = key_word, list = key_list, page = url)

if __name__ == "__main__":

    app.run()
