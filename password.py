"""
Requirement: 
-Min 8 chars, and
3 out of the followings
-Uppercase
-Lowercase
-Numbers
-Symbols
"""


import re
from itertools import groupby

password = input().strip()
l = len(password)

#Addition

check = [False, False, False, False, False]

#Min 8 Chars
if l > 8:
	check[0] = True

#Length * 4
score = l*4

for i in range(l):
	#Uppercase
	if password[i].isupper():
		score -= 2
		check[1] = True
	#Lowercase	
	if password[i].islower():
		score -= 2
		check[2] = True
	#Numbers
	if re.match(r'[\d]', password[i]):
		score += 4
		check[3] = True
	#Symbols
	if re.match(r'[^a-zA-Z0-9]', password[i]):
		score += 6
		check[4] = True
score += l*4

#count if requirements are met
for i in check:
	if i == True:
		score += 2

#Numbers or symbols between letters
chopped_password = re.sub(r'(?<=[a-zA-Z])[^a-zA-Z]+(?=[a-zA-Z])', '', password)
score += (l-len(chopped_password))*2


#Deduction
deduct = 0

#All letters
chopped_password = re.sub(r'[a-zA-Z]', '', password)
if len(chopped_password) == 0:
	deduct += l

#All numbers
chopped_password = re.sub(r'[\d]', '', password)
if len(chopped_password) == 0:
	deduct += l

#repeated chars
count = 0
con = [(k, len(list(c))) for k,c in groupby(password.upper())]
for i in con:
	if i[1]>1:
		count += 2
deduct += count

#consecutive chars
count = 0
for i in range(1, len(password)):
	if chr(ord(password[i-1]) + 1) == password[i]:
		count = count + 2
deduct += count

#sequential chars ie 3+
count = 0
upper_password = password.upper()
for i in range(1, len(upper_password)-1):
	if chr(ord(upper_password[i-1]) + 1) == upper_password[i] and chr(ord(upper_password[i]) + 1) == upper_password[i+1]:
		count += 3
deduct += count

#sum up from Deduction part
score -= deduct

if score<0:
	score = 0
elif score > 100:
	score = 100