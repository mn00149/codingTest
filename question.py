import random
# 1번


def swap(x, y):
    print("inside swap: x is", x,  "y is", y)
    c = x
    x = y
    y = c
    print("inside swap: x is", x, "y is", y)

# 3번 문제


def counting(num):
    for i in range(num):
        print(i+1)


# 4번 문제
def counting2(n, r):
    result = 1
    while result <= n:
        print(result)
        result += r

# 5번 문제


def replaceAll(txt, b, c):
    txt = list(txt)
    for i in range(len(txt)):
        if txt[i] == b:
            txt[i] = c
    print(''.join(txt))


# 6번
lower_alpha = "abcdefghijklmnopqrstuvwxyz"
upper_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def make_lower(txt):
    lower_alpha_list = list(lower_alpha)
    upper_alpha_list = list(upper_alpha)
    txt = list(txt)
    for i in range(len(txt)):
        for j in range(len(upper_alpha)):
            if txt[i] == upper_alpha_list[j]:
                txt[i] = lower_alpha_list[j]
    print(''.join(txt))

# 7번


def random_generate_list(n):
    rlist = []
    for i in range(n):
        rlist.append(random.randint(0, 100))
    return rlist


# 8번
def sum_number(list):
    result = 0
    for i in list:
        result += i
    return result


set1 = set([1, 2, 3, 4, 5, 6])
set2 = set([3, 4, 5, 6, 8, 9])


print(set1 - set2)
print(set2 - set1)
