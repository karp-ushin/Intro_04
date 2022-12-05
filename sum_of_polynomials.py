from term2 import term2
from term import term
with open('input_1.txt', 'r') as input_1:
    str1 = input_1.read()
with open('input_2.txt', 'r') as input_2:
    str2 = input_2.read()
l1 = str1.replace(" ", "").replace("-", " -").replace("+", " ").split()
l2 = str2.replace(" ", "").replace("-", " -").replace("+", " ").split()
d = dict()
for t in l1:
    exp, coefficient = term2(t)
    d[exp] = 0
for t in l2:
    exp, coefficient = term2(t)
    d[exp] = coefficient
for t in l1:
    exp, coefficient = term2(t)
    d[exp] += coefficient
sorted_d = dict(sorted(d.items(), reverse=True))
result = ""
for k in sorted_d:
    result += term(sorted_d[k], k)
with open('output.txt', 'w') as output:
    output.write(result[:-3:])
