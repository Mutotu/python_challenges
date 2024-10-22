import math

def min_squares(n):
    # Base case: if n is 0, no squares are needed
    if n == 0:
        return 0

    # Initialize the result to a large number
    min_count = float('inf')

    # Check all perfect squares less than or equal to n
    for i in range(1, int(math.sqrt(n)) + 1):
        square = i * i
        # Recursively find the minimum squares for the remaining value
        count = min_squares(n - square)
        # Update the minimum count if a smaller value is found
        min_count = min(min_count, count + 1)

    return min_count

# Test cases
print(min_squares(17))  # Should return 2
print(min_squares(15))  # Should return 4
print(min_squares(16))  # Should return 1
