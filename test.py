import doctest


def base10_to_202(x: int):
    '''
    Convert valiable(int) to 202Coin(text)

        Parameters:
                x (int): A decimal integer

        Return:
                202coin (int): Sum of a and b

        Test cases:
                >>> base10_to_202(202)
                '0c00000OC2'


        Approach:
                1. 10진수를 8진수로 바꾼다
                2. 8진수를 '0c00000000' 의 8진수의 text 형태로 바꾼다
                3. 각 숫자에 대응하는 202coin 숫자로 바꾼다
        '''
    temp = ""
    while x >= 8:
        spare = x % 8
        spare_to_str = str(spare)
        temp += spare_to_str
        x = x // 8
    temp += str(x)
    ox_num = temp[::-1]
    ref_list = "0c00000000"
    oc_num = ""
    result = ""
    change_num = {"1": "C", "3": "O", "4": "M",
                  "5": "P", "6": "I", "7": "N"}
    for i in range(10 - len(ox_num)):
        oc_num += ref_list[i]
    oc_num += ox_num

    for i in oc_num:
        result += change_num.get(i, i)
    return result


def base202_to_10(str):
    '''
    202Coin 을 10진수로 변환하라

        Parameters:
                str (text): 202coin 형식의 text

        Return:
                result (int): 202coin

        Test cases:
                >>> base202_to_10('0c00000OC2')
                202
                >>> base202_to_10('0c10000OC2')
                2097354


        Approach:
                1. '0cnnnnnnnn' 형태의 coin202수를 '0onnnnnnnn'형태의 8진수로 바꾼다
                2. 0o를 떼어낸 후 숫자 텍스트를 뒤집는다
                3. for문과 텍스트의 index값을 사용하여 각자리수에 8의 index제곱을 해준다
                4. 각자리수를 더한다
    '''
    temp = ""
    count_index = 0
    result = 0
    change_str = {
        "C": "1",
        "O": "3",
        "M": "4",
        "P": "5",
        "I": "6",
        "N": "7",
    }
    big_str = str.upper()
    for i in big_str:
        temp += change_str.get(i, i)
    temp = temp[2:]
    temp = temp[::-1]
    for i in temp:
        num = int(i)
        multy = 8**count_index
        result += num * multy
        count_index += 1
    return result


def is_base202(text):
    '''
     202Coin형식의 숫자인지 판단하여 맞으면 'True', 틀리면 'False'를 return하라

        Parameters:
                text: 202coin 형식의 text

        Return:
                result (Bool): True or False

        Test cases:
                    >>> is_base202('1cCOMPCOIN')
                    False
                    >>> is_base202('0C0C2OMPIN')
                    True
                    >>> is_base202('0c0C2OMPIN')
                    True
                    >>> is_base202('0C7C2OMPIN')
                    False
                    >>> is_base202('<!doctype html><html itemtype="tp://schema.onet/BankPage">')
                    False


        Approach:
                1. input parameter가 10글자인지 확인후 아니면  'False' return
                2. 첫 2글자가 0c or 0C 인지 확인후 아니면 'False' return
                3. set을 이용하여 input parameter를 집합을 만듬
                4. 비교 집합(0, C, 2, O, M, P, I, N)을 만든 후 비교집합과 set으로 만든 합집합이 비교집합과 같으면 return 'True'
                다르면 return 'False'
    '''
    if len(text) != 10:
        return False
    check_second = text[0:2]
    if check_second != "0c" and check_second != "0C":
        return False
    ref_set = set(text)
    check_set = {"0", "C", "2", "O", "o", "M",
                 "m", "P", "p", "I", "i", "N", "n", "c"}
    aa = ref_set | check_set
    if aa == check_set:
        return True
    else:
        return False


def get_nth_base202_amount(text, n):
    '''
text 중에 n(0부터시작)번째202coin을 반환하라

        Parameters:
                text: text
                n: int
        Return:
                result : "ocNNNNNNNN"

        Test cases:
        >>> get_nth_base202_amount("BANKING TRANSACTIONS....PLANET ORION......FEBRUARY \
        15, 3019.......0cCCMMPP22........FEBRUARY 16, 3019..........0cOCOCOCOC.........\
        FEBRUARY 17, 3019..........0C24242412", 1)
        '0cOCOCOCOC'
        >>> get_nth_base202_amount("BANKING TRANSACTIONS....PLANET ORION......FEBRUARY \
        15, 3019.......0cCCMMPP22........FEBRUARY 16, 3019..........0c0cOCOCOCOC.........\
        FEBRUARY 17, 3019..........0C24242412", 1)
        '0c0cOCOCOC'
        >>> get_nth_base202_amount("BANKING TRANSACTIONS....PLANET ORION......FEBRUARY \
        15, 3019.......0cCCMMPP22........FEBRUARY 16, 3019..........0c0cOCOCOCOC.........\
        FEBRUARY 17, 3019..........0Cooccppcc", 2)
        '0Cooccppcc'
        >>> get_nth_base202_amount("BANKING TRANSACTIONS....PLANET ORION......FEBRUARY \
        15, 3019.......0cCCMMPP22........FEBRUARY 16, 3019..........0cOCOCOCOC.........\
        FEBRUARY 17, 3019..........0C24242412", 2)
        ''


        Approach:
                1. input text를 모두 대문자로 바꾼후 변수(big_text)에 할당
                2. '0c'로 시작하는 index를 차례로 찾는다
                3. 인덱스 값을 이용해 10글자를 축출하고 그 열글자가 conin202수인지 is_base202함수로 판별한다
                4. 판별 후 통과한 것들은 list에 추가
                5. list에 추가된 경우 index + 10, 아닌 경우 index + 2
                6. list가 빈 배열이거나 len(list) < n+1 일 경우 ''을  return
                7. 5의 경우가 아닐 때 list[n]을 return
    '''
    big_text = text.upper()
    index = 0
    result_list = []
    while index > -1:
        index = big_text.find("0C", index)
        if index > -1:
            check_str = text[index: index + 10]

            if is_base202(check_str):
                result_list.append(check_str)
                index += 10
            else:
                index += 2
    if len(result_list) == 0:
        return ""
    if len(result_list) < (n + 1):
        return ""
    result = result_list[n]
    return result


def get_total_dollar_amount(text):
    '''
    text안에있는 모든 coin202값을 더하여 10진수로 반환하라

        Parameters:
                text:text
        Return:
                result: int

        Test cases:
        >>> get_total_dollar_amount("BANKING TRANSACTIONS....PLANET ORION......FEBRUARY\
            15, 3019.......0cCCMMPP22........FEBRUARY 16, 3019..........0cOCOCOCOC........\
            FEBRUARY 17, 3019..........0C24242412") 
        9167275
        >>> get_total_dollar_amount("BANKING TRANSACTIONS....PLANET ORION......FEBRUARY\
            15, 3019.......0cCCMMPP22........FEBRUARY 16, 3019..........0cOCOCOCOo........\
            FEBRUARY 17, 3019..........0C24242412") 
        9167277

        Approach:
                1. count = 0, result = 0 을 선언
                2. 반복문을 안에 get_nth_base202_amount 함수를 이용해 0 번째부터 ~ count번째까지 coin202를 축출
                3. get_nth_base202_amount = "" 일경우 result를 return하여 반복문을 빠져나오도록함
    '''
    count = 0
    result = 0
    while True:
        if get_nth_base202_amount(text, count) == "":
            return result
        temp = get_nth_base202_amount(text, count)
        plus_element = base202_to_10(temp)
        result += plus_element
        count += 1
    return result


def reduce_amounts(text, limit):
    '''
    text안에있는 모든 coin202값의 총합이 limit을 넘는 경우 감소율(10진수)을 구하여 각 coin202값에 적용한다.
    이때 감소율의 적용은 coin202값이 아닌 그에 대응 하는 10진수 값에 한후 소수자리는 내림한다.
    그후 10진수 값을 다시 coin202 값으로 변환하여 원래의 input 의 coin202값과 교체한다.
    변경된 coin202값을 제외한 모든값은 그대로 보존한체 반환하다. 

        Parameters:
                text:text
                limit: int
        Return:
                result: text

        Test cases:
        >>> reduce_amounts('0c000000C2', 5)
        '0c0000000P'
        >>> reduce_amounts("0cCCMMPP22     0cOCOCOCOC", 9000000)
        '0cCCOCMCI0     0cO0NOPNCN'
        >>> reduce_amounts("0cCCMMPP22vregvr     0cOCOCOCOC", 9000000)
        '0cCCOCMCI0vregvr     0cO0NOPNCN'

        Approach:
                1. total(int) 값과 percent_decrease(difference / total)을 구한다
                2. total <= limit 인 경우 input값을 그대로 반환
                3. get_nth_base202_amount = "" 일경우 result를 return하여 반복문을 빠져나오도록함
                4. 반복문을 이용해 input속에 202coin 값을 하나씩 축출
                5. 축출된 값을 10진수로 변환후 감소율을 적용
                6. 감소율이 적용된 값을 coin202값으로 변환
                7. 변환된 값을 input에서 축출된 위치에 다시 끼워 넣기
    '''
    count = 0
    result = text
    total = get_total_dollar_amount(text)
    difference = total - limit
    percent_decrease = difference / total
    if difference <= 0:
        return result
    while True:
        if get_nth_base202_amount(text, count) == "":
            return result
        base202 = get_nth_base202_amount(text, count)
        base10 = base202_to_10(base202)
        decrease_dollar = base10 * percent_decrease
        result_dollar = base10 - decrease_dollar
        result_202 = base10_to_202(int(result_dollar))
        result = result.replace(base202, result_202, 1)
        count += 1


if __name__ == '__main__':
    doctest.testmod()
