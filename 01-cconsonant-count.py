'''
Write a function that given a string, counts total number of consonants in it. 
A consonant is a English alphabet character that is not vowel (a, e, i, o and u). 
Examples of constants are b, c, d, f, g, ..
input will never have spaces or non letter characters

Examples: 

Input: 'snakes'
Output: 4

Input: 'SpamAndEggs'
Output: 8
'''

def consonant_counter(s, t=0):
    vowels = {"a", "e", "i", "o", "u"}

    # Base case: If we've reached the end of the string
    if t == len(s):
        return 0

    # Check if the current character is a consonant
    if s[t].lower() not in vowels:
        return 1 + consonant_counter(s, t + 1)  # Add 1 and move to the next character
    else:
        return consonant_counter(s, t + 1)  # Just move to the next character

def main():
    print(consonant_counter("snakes"), " == 4")
    print(consonant_counter("SpamAndEggs"), " == 8")

main()
