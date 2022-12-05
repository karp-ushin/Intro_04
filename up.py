def up(input_number):
    ups = "⁰¹²³⁴⁵⁶⁷⁸⁹"
    lifted = ""
    while input_number > 0:
        reminder = input_number % 10
        lifted += ups[reminder]
        input_number = input_number // 10
    return lifted[::-1]
