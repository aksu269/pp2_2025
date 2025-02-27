import re
snake_case = 'camel_case'
words = snake_case.split('_')
result = words[0] + ''.join(word.capitalize() for word in words[1:])
print(result)