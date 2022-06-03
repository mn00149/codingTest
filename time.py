

def time(n):
    count = 0
    for hour in range(0, n+1):
        for minit in range(0, 60):
            for sec in range(0, 60):
                if(hour % 10 == 3 or minit % 10 == 3 or sec % 10 == 3 or hour / 10 == 3 or minit / 10 == 3 or sec / 10 == 3):
                    count += 1
    print(count)


time(5)

# 구현 문제의 코드는 dx, dy를 설정 하여 풀것


def nightKing(input):
    dx, dy = [1, -1, 2, 2, -2, -2, 1, -1], [2, 2, 1, -1, 1, -1, -2, -2]
    trans = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
    x = int(input[1])
    y = trans[input[0]]
    count = 0
    for i in range(0, 8):
        nx = x + dx[i]
        ny = y + dy[i]
        if(nx >= 1 and nx <= 8 and ny >= 1 and ny <= 8):
            count += 1
        nx, ny = 0, 0
    print(count)


nightKing("a1")
