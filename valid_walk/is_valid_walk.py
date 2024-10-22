def is_valid_walk(walk):
    # Check if the length of the walk is 10
    walk_length = len(walk)
    if walk_length != 10: return False

    # Count the occurrences of each direction
    counts = {
        'n_c': walk.count('n'),
        's_c': walk.count('s'),
        'w_c': walk.count('w'),
        'e_c': walk.count('e'),
    }

    total_count = sum(counts[key] for key in counts) == walk_length

    # Check if there are equal north and south, and equal west and east
    return counts['n_c'] == counts['s_c'] and counts['w_c'] == counts['e_c'] and total_count
