'''
The Fibonacci Sequence is a series of numbers where each number is the sum of the two preceding ones, starting from 0 and 1.

Read more about it:

https://www.mathsisfun.com/numbers/fibonacci-sequence.html

Write a recursive function called fib that accepts a number N greater than zero and returns the Nth fibonacci number

Examples:

input: 10
output: 55

input: 3
output: 2

input: 30
output: 832040
'''

def fib(n):
    if n == 0 or n == 1:
        return n
    return  fib(n-1) + fib(n-2)

def main():
    print(fib(10), "== 55")
    print(fib(3), "== 2")
    print(fib(30), "== 832040")
    print(fib(4))
main()