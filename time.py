

def time(n):
    count = 0
    for hour in range(0, n+1):
        for minit in range(0, 60):
            for sec in range(0, 60):
                if(hour % 10 == 3 or minit % 10 == 3 or sec % 10 == 3 or hour / 10 == 3 or minit / 10 == 3 or sec / 10 == 3):
                    count += 1
    print(count)


time(5)
