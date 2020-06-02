def is_palindrome(string):
    str_len = len(string)
    for i in range(0, int(str_len / 2)):
        if string[i] != string[str_len - i - 1]:
            return False
    return True


response = is_palindrome("level")

if response:
    print("The string is palindrome")
else:
    print("The string is not palindrome")
