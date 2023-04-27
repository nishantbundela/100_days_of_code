import csv

with open('weather.csv') as file:
    reader1 = file.readlines()
    print(reader1)
    for row in reader1:
        print(row)

    print('-------------------')
    reader2 = csv.reader(file)
    for row in reader2:
        print(row)