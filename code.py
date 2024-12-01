import array as arr

n = 5
m = 7

a = arr.array('i', [4] * m)

a.append(3)

print(a)

for i in range(m):
    print(a[i], end=" ")