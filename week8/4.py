f = open('ex.txt', 'r')
cnt = 0
for x in f:
    cnt += 1
print(cnt)
f.close()