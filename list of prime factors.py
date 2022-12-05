n = 3250
Ans = set()
d = 2
while d * d <= n:
    if n % d == 0:
        Ans.add(d)
        n //= d
    else:
        d += 1
if n > 1:
    Ans.add(n)
print(list(Ans))
