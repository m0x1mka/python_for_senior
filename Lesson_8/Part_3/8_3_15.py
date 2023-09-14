def is_palindrome(s):
    if len(s) in [0, 1]:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])


print(is_palindrome("level"))
print(is_palindrome("stepik"))
