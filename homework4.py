a = []
n = int(input())
for i in range(n):
    a.append(int(input()))
print(a)
multipy = 1
for i, ai in enumerate(a):
	if i % 2 == 1:
		multipy *= ai
print(multipy)
print(max(a))
a.remove(max(a))
print(a)

