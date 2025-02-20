import csv

print(max(float(row['rawWpm']) for row in csv.DictReader(open('./datatyping.csv', 'r'))))