import re
snake_case = 'camel_case'
res = re.search(r'_(.)', snake_case)
print(re.sub(r'_(.)', res.group(1).upper(), snake_case))