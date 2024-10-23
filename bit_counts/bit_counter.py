def count_bits(n):
    # return bin(n).count('1')
    bins = []
    while n > 0:
        remainder = n % 2
        bins.append(remainder)
        n = n // 2
    return sum(b for b in bins)


print(count_bits(1532))
