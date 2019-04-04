content = open('p1.txt','r').readlines()
f = open('p1.txt','w')
for line in content:
    if line.startswith('From:'):
        line = line.replace('From:','To:',1)
    f.write(line)
