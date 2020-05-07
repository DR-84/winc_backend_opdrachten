def reverse(s):
    return s[::-1]


def is_palindrome(s):
    rev = reverse(s)
    if s == rev:
        return True
    return False


def is_odd(num):
    if (num % 2) != 0:
        return True
    else:
        return False


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
