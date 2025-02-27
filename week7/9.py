import re
text = 'HelloWorld'
pattern = r'([a-z])([A-Z])'
res = re.sub(pattern, r'\1 \2', text)
print(res)