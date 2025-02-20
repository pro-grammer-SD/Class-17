import csv

with open('datatyping.csv') as d:
    v = csv.DictReader(f=d, fieldnames="rawWpm")
    
for wpm in v:
    print(wpm)