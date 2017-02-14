import csv
with open('export.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
      # if row[0].find('laminat'):
      print(row[0])
