content = open('a.txt','r').readlines()
f = open('b.txt','w')
for line in reversed(content):
    f.write(line)
