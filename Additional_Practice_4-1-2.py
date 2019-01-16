"""
3) Write a python module script that contains fib2() method to calculate the
fibonacci series till 1000 and save it as fibo.py.
Note : The module created as fibo.py has to be placed in lib folder 

4) Write a python module script that contains ispalindrome() method to
calculate the input string as palindrome string or not and save it as
palindrome.py

"""

import fibo
fibo.fib2(1000)

import palindrome
lst=["malayalam","acadgild"]
for i in lst:
    res= palindrome.isPalindrome(i)
    if res==1:
        print("given string {} is palindorm".format(i))
    else:
        print("given string {} is not a palindorm".format(i))
