from random import randint
from term import term
k = 3
li = [randint(0, 10) for i in range(k+1)]
result = ""
for i in range(k, -1, -1):
    result += term(li[i], i)
with open('file.txt', 'w') as f:
    f.write(result[:-3:])
print(result[:-3:])
