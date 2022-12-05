from up import up


def term(coefficient, exponent):
    if coefficient == 0:
        return ""
    elif coefficient == 1:
        if exponent == 0:
            return "1 + "
        elif exponent == 1:
            return "x + "
        else:
            return "x" + up(exponent) + " + "
    else:
        if exponent == 0:
            return str(coefficient) + " + "
        elif exponent == 1:
            return str(coefficient) + "x" + " + "
        else:
            return str(coefficient) + "x" + up(exponent) + " + "
