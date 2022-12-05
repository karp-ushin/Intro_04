from normalize import normalize


def term2(s):
    pos = s.find("x")
    if pos == -1:
        coefficient = int(s)
        exp = 0
    elif pos == 0:
        coefficient = 1
        if len(s) == 1:
            exp = 1
        else:
            exp = normalize(s[pos + 1::])
    else:
        coefficient = int(s[:pos:])
        if len(s) == pos + 1:
            exp = 1
        else:
            exp = normalize(s[pos + 1::])
    return exp, coefficient
