import doctest


def same_elements(input_list):
    '''
    인풋 값 으로 2차원 배열을 받아 배열 요소의 배열요소가 같으면 true, 아니면 false 

        Parameters:
                list: 2-demention-list

        Return:
                true or false: bool

        Test cases:
                >>> same_elements([[1, 1, 1], ['a', 'a'], [6]])
                True
                >>> same_elements([[1, 6, 1], [6, 6]])
                False


        Approach:
                1. for 문으로 input_list를 순회한다
                2. 각 배열의 첫번째 요소를 변수에 할당한다
                3. for문을 하나 더 사용하여 input_list의 elements를 순회한다
                4. 할당되 변수와 다르면 false를 return한다
                5. for문을 통과하면 true를 return한다
        '''
    for i in input_list:
        a = i[0]
        for j in i:
            if j != a:
                return False
    return True


def flatten_list(input_list):
    '''
    인풋 값 으로 2차원 배열을 받아 리스트의 모든 요소를 포함한 1차원 리스트를 반환하라

        Parameters:
                list: 2-demention-list

        Return:
                list: 1-demention-list

        Test cases:
                >>> flatten_list([[1, 2], [3], ['a', 'b', 'c']])
                [1, 2, 3, 'a', 'b', 'c']
                >>> flatten_list([[]])
                []


        Approach:
                1. 리턴할 빈 배열 'result'를 선언
                2. 인풋 리스트의 element-list가 빈 배열이 아닌지 확인
                3. 빈배열이 아닌 경우 element-list의 요소를 result에추가
                4. 반복문이 다 끝나면 result를 반환
        '''
    result = []
    for i in input_list:
        if len(i) != 0:
            for j in i:
                result.append(j)
    return result


def get_most_valuable_key(dic):
    '''
    인풋값으로 dictionary를 받아서 가장큰 value를 가진 key 값을 반환하라

    Parameters:
            dictionary: 2-demention-list

    Return:
            key: char

    Test cases:
            >>> get_most_valuable_key({'a' : 3, 'b': 6, 'g': 0, 'q': 9})
            'q'
            >>> get_most_valuable_key({'a' : 18, 'b': 6, 'g': 0, 'q': 9})
            'a'


    Approach:
            1. for 문으로 key값의 list(key-list)를 만든다
            2. list의 첫번째 element를 첫번째값을 key로 가진 inpuut-dictionary의 value를 max값에 할당한다
            3. for문을 하나 더 사용해 나머지 key값에 대응하는 value가 max값보다 큰지 비교하고 크면 해당 value를 max값에 할당한다
            4. result값에 max값에 대응 하는 key를 할당 한다
            5. result를 return한다
    '''
    key_list = []
    for key in dic:
        key_list.append(key)
    max = dic[key_list[0]]
    result = key_list[0]
    for i in key_list:
        if dic[i] > max:
            max = dic[i]
            result = i
    return result


def add_dicts(d1, d2):
    '''
    인풋 값 으로 dictionary 2개를 받아 해당 dictionary의 모든 key-value를 포함한 1개의 dictionary를 반환 한다.
    이때 공통된 key의 value는 모두 더한다  

    Parameters:
            d1, d2: dictionary

    Return:
            dictionary: dictionary

    Test cases:
            >>> get_most_valuable_key({'a' : 3, 'b': 6, 'g': 0, 'q': 9})
            'q'
            >>> get_most_valuable_key({'a' : 18, 'b': 6, 'g': 0, 'q': 9})
            'a'


    Approach:
            1. for 문으로 d1, d2의 key값의 list(key-list)를 각각 만든다
            2. 각 key-list를 set으로 변환한다
            3. 각set의 교집합과 차집합을 만든다
            4. 교집합을 이용해 공통된 key값의 합을 구하여 result에 할당
            5. 차집합을 이용해 서로 다른 key값의 구하여 result에 할당
            6. result를 반환한다
    '''
    result = {}
    key_list_d1 = []
    key_list_d2 = []
    for key1 in d1:
        key_list_d1.append(key1)
    for key2 in d2:
        key_list_d2.append(key2)
    set1 = set(key_list_d1)
    set2 = set(key_list_d2)
    common_set = set1 & set2
    set_for_d1 = set1 - set2
    set_for_d2 = set2 - set1
    for key in common_set:
        result[key] = d1[key] + d2[key]
    for key in set_for_d1:
        result[key] = d1[key]
    for key in set_for_d2:
        result[key] = d2[key]

    return result


def reverse_dict(dic):
    # Note that the order of the elements in the list might not be the same, and that’s ok!
    '''
    인풋 값 으로 dictionary 받아 해당 dictionary의 key-value가 반전된 dictionary를 출력하라
반전된 dictionary의 공통된 key 의 value는 list의 형태로 포함한다

    Parameters:
            dictionary: dictionary

    Return:
            dictionary: key-value = num-list형태

    Test cases:
            >>> a = reverse_dict({'a': 3, 'b': 2, 'c': 3, 'd': 5, 'e': 2, 'f': 3})
            >>> a == {3 : ['a', 'c', 'f'], 2 : ['b', 'e'], 5 : ['d']}
            True


    Approach:
            1. 2중 for 문으로 input_dictionary의 value가 같은 key 값을 찾는다
            2. value가 같은 key는 임시 ㅣist에 append한다
            3. 2번째 for문이 끝날때마다 
            해당하는 value를 key로, 임시로 만든 list를 value로 하여 result dictionary에 할당한다
            4. result를 반환한다
    '''
    result = {}
    for key1 in dic:
        temp = [key1]
        for key2 in dic:
            if key1 != key2 and dic[key1] == dic[key2]:
                temp.append(key2)
        result[dic[key1]] = temp
    return result


if __name__ == '__main__':
    doctest.testmod()
