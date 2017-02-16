import csv

sites = [

    ['laminat33.ru',
            'div.prd-wrapper',
            'img[src]$$$src',
            'span[itemprop="name"]',
            'span.price'],

    ['bikeparts.pythonanywhere.com',
            'div.panel',
            '',
            'div.b-title',
            'div.b-price'],

    ['santehnika-online.ru',
            'div[itemprop="itemListElement"]',
            'img$$$src',
            'div.vidname > a',
            'meta[itemprop="price"]$$$content' ],

    ['www.laminat-msc.ru',
            'td > table[cellpadding]',
            'img[src]$$$src',
            'span.pr_name',  #вчера ещё было 'span[itemprop="name"]'   !!!!
            'span.catalog-price'],
    ['www.avito.ru',
            'div.item',
            'img[src]$$$src',
            'h3 > a$$$title',
            'div.about']

]

keys = ['key_netloc',       # имя(локация) сайта
        'key_pos',          # селектор товарной позиции (контейнера)
        'key_img',          # селектор картинки внутри контейнера
        'key_goods',        # селектор наименования внутри контейнера
        'key_price']        # селектор цены внутри контейнера


with open('sites.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file,fieldnames=keys)
    dict_writer.writeheader()
    for site in sites:
        dict_writer.writerow({keys[n]: site[n] for n in range(5)})


# debug

with open('sites.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)
