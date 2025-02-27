import re
text = 'abbb'
pattern = r'abb|abbb'
result = re.search(pattern, text)
if result:
    print('Yes')
else:
    print('No')