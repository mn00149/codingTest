# base10_to_202
def base10_to_202(x: int):
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


# test base10_to_202
# result = base10_to_202(202)
# print(result)

# ---------------------------------------------------------
# base202_to_10


def base202_to_10(str):
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
        "c": "o",
    }
    for i in str:
        temp += change_str.get(i, i)
    temp = temp[2:]
    temp = temp[::-1]
    for i in temp:
        num = int(i)
        multy = 8**count_index
        result += num * multy
        count_index += 1
    return result


# test base202_to_10
# result = base202_to_10("0c00000OC2")
# print(result)

# ---------------------------------------------------------
# is_base202
def is_base202(text):
    if len(text) != 10:
        return False
    check_second = text[0:2]
    if check_second != "0c" and check_second != "0C":
        return False
    ref_set = set(text)
    check_set = {"0", "C", "2", "O", "M", "P", "I", "N", "c"}
    aa = ref_set | check_set
    if aa == check_set:
        return True
    else:
        return False


# test is_base202
# result = is_base202("1cCOMPCOIN")
# print(result)
# result = is_base202("0c0C2OMPIN")
# print(result)
# result = is_base202('<!doctype html><html itemtype="tp://schema.onet/BankPage">')
# print(result)

# ---------------------------------------------------------
# get_nth_base202_amount
def get_nth_base202_amount(text: str, n: int):
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


# test get_nth_base202_amount
# result = get_nth_base202_amount(
#     "BANKING TRANSACTIONS....PLANET ORION......FEBRUARY \
# 15, 3019.......0cCCMMPP22........FEBRUARY 16, 3019..........0cOCOCOCOC.........\
# FEBRUARY 17, 3019..........0C24242412",
#     1,
# )
# print(result)

# result = get_nth_base202_amount(
#     "BANKING TRANSACTIONS....PLANET ORION......FEBRUARY \
# 15, 3019.......0cCCMMPP22........FEBRUARY 16, 3019..........0cOCOCOCOC.........\
# FEBRUARY 17, 3019..........0C24242412",
#     2,
# )
# print(result)

# ---------------------------------------------------------
# get_total_dollar_amount


def get_total_dollar_amount(text):
    index = 0
    check_list = []
    result_list = []
    total = 0
    while index > -1:
        index = text.find("0c", index)
        if index > -1:
            check_str = text[index: index + 10]
            check_list.append(check_str)
            index += len("0c")
    for i in check_list:
        if is_base202(i) == True:
            result_list.append(i)
    for i in result_list:
        temp = base202_to_10(i)
        total += temp
    return total


# test get_total_dollar_amount
# result = get_total_dollar_amount(
#     "BANKING TRANSACTIONS....PLANET ORION......FEBRUARY\
# 15, 3019.......0cCCMMPP22........FEBRUARY 16, 3019..........0cOCOCOCOC........\
# FEBRUARY 17, 3019..........0C24242412"
# )
# print(result)

# ---------------------------------------------------------
# reduce_amounts
# def reduce_amounts(text, limit):
#     total = get_total_dollar_amount(text)
#     difference = total - limit
#     percent_decrease = difference / total
#     index = 0
#     index_list = []
#     coin202_in_text_list = []
#     result_list = []
#     count_for_result_list = 0
#     if difference <= 0:
#         return text
#     while index > -1:
#         index = text.find("0c", index)
#         if index > -1:
#             check_str = text[index: index + 10]
#             if is_base202(check_str) == True:
#                 coin202_in_text_list.append(check_str)
#                 index_list.append(index)
#             index += len("0c")
#     for i in coin202_in_text_list:
#         temp = base202_to_10(i)
#         dollar = temp * percent_decrease
#         result_dollar = temp - dollar
#         result = base10_to_202(int(result_dollar))
#         result_list.append(result)
#     for i in index_list:
#         new_text = text[:i] + \
#             result_list[count_for_result_list] + text[i + 10:]
#         count_for_result_list += 1
#         text = new_text
#     return text


def reduce_amounts(text, limit):
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


# test reduce_amounts
# result = reduce_amounts("0c000000C2", 5)
# print(result)
# result = reduce_amounts("0cCCMMPP22     0cOCOCOCOC", 9000000)
# print(result)

def universe_to_str(input):

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
    result += "+\n"
    return result


block = [[0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
str_block = universe_to_str(block)
print(str_block)
tub = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0],
       [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
str_tub = universe_to_str(tub)
print(str_tub)

toad = [[0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0],
        [0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0]]
str_toad = universe_to_str(toad)
print(str_toad)
# ------------------------------------------------------------------------------------------------------
# >>> tub = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
# >>> get_next_gen_universe(tub)
# [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
# >>> toad =
# [
# [0, 0, 0, 0, 0, 0],
# [0, 0, 1, 1, 1, 0],
# [0, 1, 1, 1, 0, 0],
# [0, 0, 0, 0, 0, 0]]
# >>> get_next_gen_universe(toad)
# [[0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 1, 0], [0, 1, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0]]
# >>> pentadec = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0], [0,0,0,0,1,0,0,0,0], [0,0,0,1,0,1,0,0,0], [0,0,0,0,1,0,0,0,0], [0,0,0,0,1,0,0,0,0], [0,0,0,0,1,0,0,0,0], [0,0,0,0,1,0,0,0,0], [0,0,0,1,0,1,0,0,0], [0,0,0,0,1,0,0,0,0], [0,0,0,0,1,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
# >>> pentadec_gen2 = get_next_gen_universe(pentadec)
# >>> pentadec_gen2[0:3]
# [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
# >>> pentadec_gen2[3:6]
# [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 1, 0, 1, 0, 0, 0]]
# >>> pentadec_gen2[6:9]
# [[0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 1, 0, 0, 0]]
# >>> pentadec_gen2[9:12]
# [[0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 1, 0, 1, 0, 0, 0], [0, 0, 0, 1, 1, 1, 0, 0, 0]]
# >>> pentadec_gen2[12:15]
# [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
# >>> pentadec_gen2[15]
# [0, 0, 0, 0, 0, 0, 0, 0, 0]
