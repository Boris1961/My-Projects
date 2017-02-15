import csv

mydict = {
        1: {'q': 'w'} ,
        2: 17 ,
        3: '1' ,
        4: 'r'
}

with open('tst_csv_wrt.csv', 'w', newline='') as csvfile:

    writer = csv.DictWriter(csvfile, fieldnames=mydict.keys())
    writer.writeheader()
    writer.writerow(mydict)
    writer.writerow({1:0,2:9,3:8,4:7})
    writer.writerow({1: 1, 2: 2})

with open('tst_csv_wrt.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        a = row
        print(row)

'''
   www.laminat - msc.ru, td > table[cellpadding], img[src]$$$src, "span[itemprop=""name""]", span.catalog - price
    laminat33.ru, div.prd - wrapper, img[src]$$$src, "span[itemprop=""name""]", span.price
    santehnika - online.ru, "div[itemprop=""itemListElement""]", img$$$src, div.vidname > a, "meta[itemprop=""price""]$$$content"
    bikeparts.pythonanywhere.com, div.panel,, div.b - title, div.b - price
'''

# print(a.keys())
# print(type(a['1']))
