import re
text = 'abnb'
pattern = r'^a.*b$'
result = re.findall(pattern, text)
print(result)