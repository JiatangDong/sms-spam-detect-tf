import json
import csv
import re  
import random

f = open('gmSpamSource.json', 'r', encoding="utf8")
data, messages = json.load(f), set()
for d in data:
    d = re.sub('\n', ' ', d)
    d = re.sub('TIME: .*\| ', '', d)
    d = re.sub('Event Name: ', '', d)
    d = re.sub('Event Description: ', '', d)
    d = re.sub('GröupMе Suррört: ', '', d)
    d = re.sub('GröuрMе Suррört: ', '', d)
    d = re.sub('.* Manager: ', '', d)
    d = re.sub('GroupMe Calendar: ', '', d)
    d = re.sub('.* Manager updated the location for the event ', '', d)
    if d[0] == d[-1] == "\'": d = d[1:-1]
    if d[0] == d[-1] == "\"": d = d[1:-1]
    messages.add(d.strip())
f.close()

train, test = [], []
for m in messages:
    if random.random() < 0.9:
        train.append(['spam', m])
    else:
        test.append(m)

f = open('../spam.csv', 'r')
data = csv.reader(f)
for row in data:
    train.append(['ham', row[1]])
f.close()

random.shuffle(train)

f = open('gmTrain.csv', 'w', encoding="utf8")
cw = csv.writer(f) 
cw.writerow(['v1','v2']) 
cw.writerows(train)
f.close()

f = open('gmTest.json', 'w', encoding="utf8")
f.write('[\n')
for l in test:
    f.write('   \"' + l + "\",\n") 
f.write(']')
f.close()

# print(data)