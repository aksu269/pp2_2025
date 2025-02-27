import re
text = 'a_b_b_b'
pattern = r'[a-z]+_[a-z]+'
result = re.findall(pattern, text)
print(result)