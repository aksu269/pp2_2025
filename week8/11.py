s = input()
s = s.lower()
if s == s[::-1]:
    print("Is palindrome.")
else:
    print("Is not palindrome.")