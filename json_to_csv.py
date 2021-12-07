# this one goes out to all my pants out there, make some noise if you are pants!

import csv
import json

jsonpath = 'C:\\Users\\spenc\\babiesfirst.json'
csvpath = 'C:\\Users\\spenc\\babiesback.csv'

with open(jsonpath) as jsonfile:
    jsondata = json.load(jsonfile)

datafile = open(csvpath, 'w', newline='')
csvwrite = csv.writer(datafile)
# print(jsondata)
count = 0
for data in jsondata['rows']:
#    print(type(data))
    if count == 0:
        header = data.keys()
        csvwrite.writerow(header)
        count += 1
    csvwrite.writerow(data.values())

datafile.close()
