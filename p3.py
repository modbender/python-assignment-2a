import re

f = open('p3.txt','r').readlines()
digits = []
for line in f:
    num = re.findall(r'[\d]+',line)
    if len(num)>0:
        for n in num:
            digits.append(n)
print(", ".join(digits))
