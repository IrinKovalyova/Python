a = []
odds = []
n = int(input("ВВЕДИТЕ КОЛ ВО ЭЛ В СПИСКЕ: "))
for i in range(n):
    new_elemet = int(input())
    a.append(new_elemet)
    if new_elemet % 2 == 1:
        odds.append(new_elemet)
print(odds)
print(max(odds))

modules=[]
for i in a:
    modules.append(abs(i))
print(modules)
print(min(modules))
