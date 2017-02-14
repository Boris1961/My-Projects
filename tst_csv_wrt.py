import csv
mydict = {
    'laminat33.ru': ['div.prd-wrapper', 'img[src]$$$src', 'span[itemprop="name"]', 'span.price'],
    'bikeparts.pythonanywhere.com' : ['div.panel', '', 'div.b-title', 'div.b-price'],
    'santehnika-online.ru': ['div[itemprop="itemListElement"]', 'img$$$src', 'div.vidname > a', 'meta[itemprop="price"]$$$content' ],
    'laminat-msc.ru' : ['', '', '', '']
}

keys = ['key_netloc',       # имя(локация) сайта
        'key_pos',          # селектор товарной позиции (контейнера)
        'key_img',          # селектор картинки внутри контейнера
        'key_goods',        # селектор наименования внутри контейнера
        'key_price']  # селектор цены внутри контейнера


with open('export.csv', 'w', newline='') as output_file:
    dict_writer = csv.writer(output_file)
    for key in mydict.keys():
        dict_writer.writerow([key, mydict[key][0], mydict[key][1], mydict[key][2], mydict[key][3]])
