from math import log

def get_number_length(n):
    return round(log(n, 10)) + 1

# def get_list_of_digits(n):
#     return [int(i) for i in str(n)]

def get_list_of_digits(n):
    n_length = get_number_length(n)
    mult = 10 ** (n_length - 1)

    res = []
    while n_length > 1:
        first_digit = int(n / mult)
        res.append(first_digit)

        n -= (first_digit * mult)

        # NOTE: Can substitute this call with a basic `-=`, but just so we're clear about
        # what we're doing...
        n_length = get_number_length(n)
    res.append(n)
    return res

def combo_check(combo):
    digit_list = get_list_of_digits(combo)

    has_adjacent_digits = False

    cur_val = digit_list[0]
    for val in digit_list[1:]:
        if val < cur_val:
            return False
        if val == cur_val:
            has_adjacent_digits = True
        cur_val = val
    return has_adjacent_digits

def checker(start, end):
    count = 0
    for combo in range(start, end):
        if combo_check(combo):
            count += 1
    return count

