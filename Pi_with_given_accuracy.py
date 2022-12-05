from math import log10
d = 0.001   #calculation of Pi by formula Pi = 4 * (1 - 1/3 + 1/5 - 1/7 + ...)
series = 0
term = 1
k = 1
b = 1
while 4 * abs(term) > d:
    series += term
    b *= -1
    k += 2
    term = b / k
accuracy = int(log10(1/d))
print("Pi is ", round(4 * series, accuracy))
