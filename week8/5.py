array = ['apple', 'banana', 'pineapple']
with open('ex.txt', 'w') as f:
    for x in array:
        f.write(f'{x} ')
