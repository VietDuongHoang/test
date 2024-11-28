import array as arr

n = 3
m = 2

a = arr.array('i', [4] * m)

a.append(3)

print(a)

for i in range(m):
    print(a[i], end=" ")