def longest_palindrome(s: str) -> int:
    if len(s) < 2: return len(s)
    max_pal = 0
    for i in range(len(s)):
        for j in range(len(s)):
            sub_str = s[i:j+1]
            print(sub_str)
            if is_palindrome(sub_str) and len(sub_str) > max_pal:
                max_pal = len(sub_str)
    return max_pal



def is_palindrome(s: str) -> bool:
    if len(s) == 1: return False
    return s ==  ''.join(reverse_string(list(s)))

def reverse_string(s: list[str]) -> str:
    return ''.join(s[::-1])


