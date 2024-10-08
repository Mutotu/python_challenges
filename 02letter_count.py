# Write a function called `letter_count` to count the occurances of each letter
# in a string. Use a dictionary.
#
# You can iterate over a string one letter at a time using
# a for loop.
#
# for letter in "alpha":
#   print(letter)
#
# Create a dictionary with `dd = {}`. Assign values with `dd["foo"] = 1`.
# Check to see if a dictionary has a key using the `in` operator.
#
#
# Careful. Python requires that you insert a key into a dictionary
# before you try to modify it's value. If you try to access a dictionary
# at a key that hasn't been added you'll get an error and the program will
# crash. Remember to use an if statement to see if a key is "in" a dictionary
# before you try to read it!
#
# d2 = {}
# d2["foo"]
# > KeyError: 'foo'
#
# Example function call:
#
# letter_count('banana')
#
# > {'a': 3, 'b': 1, 'n': 2}

# def letter_count(str):
#     result = {}
#     for i in range(len(str)):
#         if str[i] not in result:
#             result[str[i]] = 1
#         else:
#             result[str[i]] += 1
#     return result

def letter_count(s):
    result = {}
    for char in s:
        if char not in result:
            result[char] = 1
        else:
            result[char] += 1
    return result

def main():
    print(letter_count("lolloll"), " == {'l':5, 'o':2}")
    print(letter_count("ababab"), " == {'a':3, 'b':3}")

main()