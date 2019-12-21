def checker(start, end):
    count = 0
    for combo in range(start, end + 1):
        if combo_check(combo):
            count += 1
    return count

def combo_check(combo):
    # Break out our 6 digit number into a list of single-digit ints
    digit_list = [int(i) for i in str(combo)]

    has_adjacent_pair = False
    current_digit_count = 1

    # TODO: Groups to the "right" are overriding "good" groups to the "left"

    cur_val = digit_list[0]
    for val in digit_list[1:]:
        if val < cur_val:
            return False
        elif val == cur_val:
            current_digit_count += 1
        elif val > cur_val:
            if current_digit_count == 2:
                has_adjacent_pair = True
            current_digit_count = 1
        cur_val = val
    return has_adjacent_pair or (current_digit_count == 2)
