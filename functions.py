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


def choice_number(digital, max_count_ch_list, remain_comb_list2):
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

# digital = 4
# print(check_ab('0134', '4567'))
