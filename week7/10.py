import re
camel_case = 'aksuAb'
res = re.sub(r'([a-z])([A-Z])', r'\1_\2', camel_case).lower()
print(res)