x = [1,2,3,4,5,6,7]

x.append(8)
x.insert(0,420)
x.remove(5)
x.remove(x[3])

print(x.index(420))
print(x.count(2))
print(x)
print(x[-1])
print(x[3:6])

x.sort()
print('sort:',x )