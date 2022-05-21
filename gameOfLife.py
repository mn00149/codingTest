import doctest


def is_valid_universe(input):
    '''
    인풋 값 으로 2차원 list받아 universe가 valid한지 판단 하라.
    (input iist의 차원이 직사각형일것, element가 0 혹은 1 일것)

    Parameters:
            list: 2차원 list

    Return:
            True or False: Bool

    Test cases:
        >>> a=[[0, 0], [1, 0], [1, 0]] 
        >>> is_valid_universe(a)
        True
        >>> b=[[0, 0, 0], [1, 1], [0]] 
        >>> is_valid_universe(b)
        False
        >>> c=[[1, 2], [3, 4]] 
        >>> is_valid_universe(c) 
        False

    Approach:
            1. sub-list의 길이가 0인 경우 False
            2. 각각의 sub-list의 길이가 다른경우 False
            3. 2번째 for문으로 각 elements가 0혹은 1이 아닌 경우 False
            4. 이외의 경우 True
    '''

    lengthToSubList = len(input[0])
    if lengthToSubList == 0:
        return False
    for subList in input:
        if lengthToSubList != len(subList):
            return False
    for subList in input:
        for e in subList:
            if e > 1:
                return False
    return True


def universe_to_str(input):
    '''
    인풋 값 으로 2차원 list받아 해당 차원과 대응 하는 String을 반환하라

    Parameters:
            list: 2차원 list

    Return:
            String: String

    >>> block=[[0,0,0,0], [0,1,1,0], [0,1,1,0], [0,0,0,0]] 
    >>> str_block = universe_to_str(block)
    >>> print(str_block)
    +----+
    |    |
    | ** |
    | ** |
    |    |
    +----+
    >>> tub = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
    >>> str_tub = universe_to_str(tub) 
    >>> print(str_tub)
    +-----+
    |     |
    |  *  |
    | * * |
    |  *  |
    |     |
    +-----+

    >>> toad = [[0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0], [0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0]]
    >>> str_toad = universe_to_str(toad) 
    >>> print(str_toad)
    +------+
    |      |
    |  *** |
    | ***  |
    |      |
    +------+

    Approach:
            1. sub-list의 갯수만큼 행을 바꿀 수 있도록 1차 for문을 설정
            2. 2중 for문 을 이용해 각 elements가 0일 경우 " " 을 result에 추가
            3. 2중 for문 을 이용해 각 elements가 일 경우 "*" 을 result에 추가

    '''
    result = ""
    numberOfElements = len(input[0])
    result += "+"
    for i in range(numberOfElements):
        result += '-'
    result += "+\n"
    for subList in input:
        result += "|"
        for element in subList:
            if element == 0:
                result += " "
            if element == 1:
                result += "*"
        result += "|\n"
    result += "+"
    for i in range(numberOfElements):
        result += '-'
    result += "+"
    return result


def count_live_neighbors(beehive, x, y):
    '''
    인풋 값 으로 2차원 list와 x,y 좌표를 받아 해당 좌표 주위에 살아있는 세포의 수를 반환하라

    Parameters:
            list: 2차원 list
            x, y: int

    Return:
            result: int
    >>> beehive = [[0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0], [0, 1, 0, 0, 1, 0], [0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0]]
    >>> count_live_neighbors(beehive,  1,  3)
    2
    >>> count_live_neighbors(beehive,  3,  1)
    2
    >>> toad = [[0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0], [0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0]]
    >>> count_live_neighbors(toad,  0,  3)
    3
    >>> count_live_neighbors(toad,  2,  3)
    4

    Approach:
            1.지정 좌표에서 갈수 있는 x, y 방향을 설정하여 list화 한다
            2.for문을 이용해 지정좌표의 direction을 돌아다니면서 살아있는 세포를 count한다
            3.좌표 주변이 이차원 리스트의 범위를 벗어날 경우 좌표를 찍기전 0을 카운트하여 바져나간다

    '''
    directionX = [0, -1, 1]
    directionY = [0, -1, 1]
    lengthX = len(beehive)
    lengthY = len(beehive[0])

    result = 0
    for i in directionX:
        if x+i < 0 or x+i == lengthX:
            result += 0
        else:
            for j in directionY:
                if y+j < 0 or y+j == lengthY:
                    result += 0
                elif i == 0 and j == 0:
                    result += 0
                elif beehive[x+i][y+j] == 1:
                    result += 1
                else:
                    result += 0
    return result


def get_next_gen_cell(beehive, x, y):
    '''
    인풋 값 으로 2차원 list와 x,y 좌표를 받아 해당 좌표 가 다음 세대에 생존여부를 반환하라
    Parameters:
            list: 2차원 list
            x, y: int

    Return:
            1 or 0: int
    Test:
    >>> beehive=[[0,0,0,0,0,0], [0,0,1,1,0,0], [0,1,0,0,1,0], [0,0,1,1,0,0], [0, 0, 0, 0, 0, 0]]
    >>> get_next_gen_cell(beehive, 1, 3)
    1
    >>> get_next_gen_cell(beehive, 3, 1)
    0
    >>> toad = [[0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0], [0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0]]
    >>> get_next_gen_cell(toad, 0, 3)
    1
    >>> get_next_gen_cell(toad, 2, 3)
    0
    >>> get_next_gen_cell(toad, 2, 4)
    1
    >>> get_next_gen_cell(toad, 2, 2)
    0
    >>> get_next_gen_cell(toad, 0, 0)
    0
    >>> get_next_gen_cell(toad, 0, 4)
    0
    >>> get_next_gen_cell(toad, 2, 4)
    1

    Approach:
            1.count_live_neighbors을 사용해 해당 좌표 주위의 생존세포 수를 구한다
            2.좌표의 세포가 죽었는지 살았는지 에 따라 경우를 나눈다
            3.다음세대 세포생존 조건을 이용하여 조건식을 세우고 그에따라 알맞은 값은 리턴한다 

    '''
    if beehive[x][y] == 1:
        if count_live_neighbors(beehive, x, y) < 2:
            return 0
        elif count_live_neighbors(beehive, x, y) == 2 or count_live_neighbors(beehive, x, y) == 3:
            return 1
        else:
            return 0
    elif count_live_neighbors(beehive, x, y) == 3:
        return 1
    else:
        return 0


def get_next_gen_universe(tub):
    '''
    인풋 값 으로 2차원 list를 받아 해당 좌표 가 다음 세대에 universe를 2차원 배열로 반환하라
    Parameters:
            list: 2차원 list


    Return:
        list:2차원 list
    >>> tub = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
    >>> get_next_gen_universe(tub)
    [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
    >>> toad = [[0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0], [0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0]]
    >>> get_next_gen_universe(toad)
    [[0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 1, 0], [0, 1, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0]]
    >>> pentadec = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0], [0,0,0,0,1,0,0,0,0], [0,0,0,1,0,1,0,0,0], [0,0,0,0,1,0,0,0,0], [0,0,0,0,1,0,0,0,0], [0,0,0,0,1,0,0,0,0], [0,0,0,0,1,0,0,0,0], [0,0,0,1,0,1,0,0,0], [0,0,0,0,1,0,0,0,0], [0,0,0,0,1,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    >>> pentadec_gen2 = get_next_gen_universe(pentadec)
    >>> pentadec_gen2[0:3]
    [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    >>> pentadec_gen2[3:6]
    [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 1, 0, 1, 0, 0, 0]]
    >>> pentadec_gen2[6:9]
    [[0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 1, 0, 0, 0]]
    >>> pentadec_gen2[9:12]
    [[0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 1, 0, 1, 0, 0, 0], [0, 0, 0, 1, 1, 1, 0, 0, 0]]
    >>> pentadec_gen2[12:15]
    [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    >>> pentadec_gen2[15]
    [0, 0, 0, 0, 0, 0, 0, 0, 0]

    Approach:
            1.result에 초기화한 2차원 배열을 할당
            2.2중 for문으로 모든 input-list의 모든 element를 get_next_gen_cell함수에 넣는다
            3.결과 값을 해당 좌표의 result element에 할당 한다

    '''
    lenghtX = len(tub)
    lenghtY = len(tub[0])
    result = [[0]*lenghtY for _ in range(lenghtX)]
    for x in range(lenghtX):
        for y in range(lenghtY):
            result[x][y] = get_next_gen_cell(tub, x, y)

    return result


# def get_n_generations(tub, n):
#     '''
#       >>> tub = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
#       >>> g = get_n_generations(tub, 5)
#       >>> len(g)
#       1
#       >>> g[0] == universe_to_str(tub)
#       True
#       >>> toad = [[0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0], \
#                   [0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0]]
#       >>> g = get_n_generations(toad, 5)
#       >>> len(g)
#       2
#     '''
#     result = get_next_gen_universe(tub)
#     if n == 0:
#         finalResult = universe_to_str(result)
#         return finalResult

#     n -= 1
#     return get_n_generations(result, n)


if __name__ == '__main__':
    doctest.testmod()
