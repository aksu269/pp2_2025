import re
text = 'AAksuAbaidullayeva'
pattern = '[A-Z][a-z]*'
res = re.findall(pattern, text)
print(res)