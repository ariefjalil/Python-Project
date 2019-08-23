import csv

with open('csvtest.csv ') as file:
    reader = csv.reader(file, delimiter = ';')

    count =0

    for row in reader:
        print (row [0])

        if count > 5 :
            break

        count += 1
