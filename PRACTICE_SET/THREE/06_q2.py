# Return is a string is a palindrome
def is_palindrome(string):
    string = string.lower()
    isPalindrome = string[::-1] == string
    return isPalindrome

print(is_palindrome("dat"))