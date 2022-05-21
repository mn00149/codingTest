# 이진탐색
def binery(target, arr, start, end):

    while start <= end:
        mid = (start + end)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1

        else:
            start = mid+1
    return None


# a = binery(5, [1, 2, 3, 4, 5, 8, 9, 10], 0, 7)
# print(a)


def dduk(n, m, arr):
    end = max(arr)
    start = 0
    result = end
    while start <= end:
        mid = (start+end)//2
        total = 0
        for i in arr:
            temp = i - mid
            if temp < 0:
                temp = 0
            total += temp
        if total > m:
            start = mid + 1
            result = min(result, mid)
        elif total == m:
            return mid
        else:
            end = mid - 1
    return result


def dfs(x, y, word, puzzle):
    if x <= -1 or x >= 4 or y <= -1 or y >= 4:
        return False
    if puzzle[x][y] == word:
        puzzle[x][y] = '#'
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False


print('a')
