import re
pattern = r'[ .,]'
text = 'My name is Aksu'
result = re.sub(pattern, ':', text)
print(result)