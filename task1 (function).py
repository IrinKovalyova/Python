# m = int(input())
# n = int(input())
# p = int(input())

# function with args
def count(m,n,p):  # ищет количество отрицательных чисел
    count = 0
    if m < 0:
        count += 1
    if n < 0:
        count += 1
    if p < 0:
        count += 1
    print(count)

count(1,2,-3)


# function with args
def count():  # ищет количество отрицательных чисел
    m = 4
    n = 5
    p = -6

    count = 0
    if m < 0:
        count += 1
    if n < 0:
        count += 1
    if p < 0:
        count += 1
    print(count)

count()

