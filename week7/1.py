import re
text = 'a'
pattern = r'ab*'
result = re.search(pattern, text)
if result:
    print('Yes')
else:
    print('No')