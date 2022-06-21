import json
import csv 

f = open('gmSpam.json', 'r', encoding="utf8")
data = json.load(f)
res = []
for d in data:
    d = d.replace('Event Name: ', ' ')
    d = d.replace('Event Description: ', ' ')
    d = d.replace('\n', ' ')
    res.append(['spam', d.strip()])
f.close()

f = open('gm.csv', 'w', encoding="utf8")
cw = csv.writer(f) 
cw.writerow(['v1','v2']) 
cw.writerows(res)

# print(data)