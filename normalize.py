def normalize(input_string):
    dictionary = dict(zip(list("⁰¹²³⁴⁵⁶⁷⁸⁹"), [str(i) for i in range(10)]))
    result = ""
    for char in input_string:
        result += dictionary[char]
    return int(result)
