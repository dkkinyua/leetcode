"""
My Approach:
A palindrome is an integer or string wherethe first value of the int/str is equals to the last value of the int/str.

i. Convert the int into a str so that we can reverse the int
ii. If the first value of the int is equal to the last, return True
iii. If not, return False

"""
def is_palindrome(x):
    x = str(x)
    if x == x[::-1]:
        return True
    else:
        return False

print(is_palindrome(101))