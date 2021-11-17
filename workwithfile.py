input_txt = open("D:\python\pythonProject\homeworkwithfiles\F1", 'r')
Lines = input_txt.readlines()

input_txt.close()
print(Lines)

lst = []

l = [line.rstrip() for line in Lines]

for word in l:
    if word.isalpha():
        lst.append(word)

print(lst)

with open("D:\python\pythonProject\homeworkwithfiles\F2", 'w') as file:
    for word in lst:
        file.write(word+"\n")

count = 0
for word in lst:
    if word[0] == "A":
        count += 1
print(count)
