roman_nums = {
    "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
}

def deromanize(romans):
    result = 0
    tracker = 0
    while tracker < len(romans):
        code = romans[tracker]

        # Check if next character exists
        if tracker + 1 < len(romans):
            next_code = romans[tracker + 1]

            # Check for subtractive combinations
            if (code == 'C' and next_code in ['M', 'D']) or \
               (code == 'X' and next_code in ['C', 'L']) or \
               (code == 'I' and next_code in ['X', 'V']):
                result += roman_nums[next_code] - roman_nums[code]
                tracker += 2
                continue

        # If not a subtractive combination or no next character, add the current value
        result += roman_nums[code]
        tracker += 1

    return result
