import re

file = open('members.txt', 'r')
content = file.read()
file.close()
new = content.replace("\\", "")

raw = new.split('\n')
database = []
for l in raw:
    if re.search('email', l):
        m = l.replace('"email": "', '').replace('",', '').strip()
        database.append(m)

google = open('google.csv', 'r').read()
googleList = []
for n in google.split(','):
    if re.search('@', n):
        googleList.append(n)

for i in database:
    found = False
    for j in googleList:
        if i == j:
            found = True
    if not found:
        print(i)
