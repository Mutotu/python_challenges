def reverse_str(s):
  result = ""
  for i in range(len(s)):
    result += s[len(s) - 1 - i]
  return result


def main():

  print(reverse_str(input("Enter something: ")))

main()
