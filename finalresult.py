import csv

ds_1 = []
ds_2 = []

with open("ds1.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        ds_1.append(row)

with open("ds2_sorted.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        ds_2.append(row)

headers_1 = ds_1[0]
planet_data_1 = ds_1[1:]

headers_2 = ds_2[0]
planet_data_2 = ds_2[1:]

headers = headers_1 + headers_2
planet_data = []
for index, data_row in enumerate(planet_data_1):
    planet_data.append(planet_data_1[index] + planet_data_2[index])

with open("finalresult.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)