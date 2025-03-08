f1 = open('ex.txt', 'r')
cont = f1.read()
with open('ex2.txt', 'w') as f2:
    f2.write(cont)
f1.close()
