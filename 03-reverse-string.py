'''
Write a recursive function called reverse that accepts a string and returns a reversed string.

Examples:

input: "computer"
output: "retupmoc"

input: "ab"
output: "ba"

input: "abcdefghijklmnopqrstuvwxyz"
output: "zyxwvutsrqponmlkjihgfedcba"
'''

def reverse(s):
    if len(s) <= 1:
        return s
    return s[-1] + reverse(s[:-1])

def main():
    print(reverse("computer"), "== 'retupmoc'")
    print(reverse("ab"), "== 'ba'")
    print(reverse("abcdefghijklmnopqrstuvwxyz"), "== 'zyxwvutsrqponmlkjihgfedcba'")

main()