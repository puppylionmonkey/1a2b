import time
from itertools import permutations


def create_all_comb(digital):
    permutation_list = list(permutations("0123456789", digital))
    str1_list = list()
    for one_permutation in permutation_list:
        str1 = ''
        for ch in one_permutation:
            str1 += ch
        str1_list.append(str1)
    return str1_list


def check_ab(answer, number_str):
    result = 0
    for i in range(0, len(number_str)):
        for j in range(0, len(number_str)):
            if answer[i] == number_str[j]:
                if i == j:
                    result += 10
                else:
                    result += 1
    return int(result / 10), result % 10


def get_count_dict(remain_comb_list2):
    test_str1 = ''
    for remain in remain_comb_list2:
        test_str1 += remain
    count_dict = dict()
    for i in range(10):
        count_dict[i] = test_str1.count(str(i))
    return {k: v for k, v in sorted(count_dict.items(), key=lambda item: item[1], reverse=True)}


def choice_number(max_count_ch_list, remain_comb_list2):
    count_dict = dict()
    for remain_comb in remain_comb_list2:
        count = 0
        for ch in remain_comb:
            if int(ch) in max_count_ch_list:
                count += 1
        count_dict[remain_comb] = count
        if count == digital:
            return remain_comb
    count_dict = {k: v for k, v in sorted(count_dict.items(), key=lambda item: item[1], reverse=True)}
    return list(count_dict.keys())[0]


digital = 4
all_comb_list1 = create_all_comb(digital)
# remain_comb_list2 = create_all_comb(digital)

guess_count = 0

# while True:
start_time = time.time()
guess_time = len(all_comb_list1)
for answer in all_comb_list1:
    remain_comb_list2 = create_all_comb(digital)
    while True:
        # 選數字
        max_count_ch_list = list(get_count_dict(remain_comb_list2).keys())[:digital + 0]
        guess_number_str = choice_number(max_count_ch_list, remain_comb_list2)
        # guess_number_str = random.choice(remain_comb_list2)
        # print(guess_number_str)
        guess_count += 1

        # 刪數字
        guess_result = check_ab(answer, guess_number_str)
        # print(guess_number_str, guess_result)
        if guess_result[0] == digital:
            # print('win!')
            break
        else:
            remain_comb_list2.remove(guess_number_str)
            for remain_comb in remain_comb_list2:
                ab = check_ab(guess_number_str, remain_comb)
                if guess_result[0] != ab[0] or guess_result[1] != ab[1]:
                    remain_comb_list2.remove(remain_comb)
end_time = time.time()
print(guess_count)
print(guess_count / guess_time)
print(end_time - start_time)
# print(remain_comb_list2)
# print(guess_number_str, guess_result, len(remain_comb_list2))

# 6573

# 9874 1A
# 0123

#
