# 5位數
# 0~9 任意組合 0123 ok 0011 no ok
#
import random
import time

from functions import create_all_comb, check_ab, choice_number, get_each_number_total_count_dict

digital = 4
all_comb_list1 = create_all_comb(digital)
remain_comb_list2 = create_all_comb(digital)

guess_count = 0

# while True:
start_time = time.time()
guess_time = len(all_comb_list1)
# for answer in ['1398']:
# print('answer', answer)
while True:
    # 選數字
    max_count_ch_list = list(get_each_number_total_count_dict(remain_comb_list2).keys())[:digital]
    guess_number_str = choice_number(remain_comb_list2)
    print(remain_comb_list2)
    print(guess_number_str)
    guess_count += 1

    # 刪數字
    # # 猜數字
    a = int(input('a:'))
    b = int(input('b:'))
    guess_result = (a, b)
    if guess_result[0] == digital:
        # print('win!')
        break
    else:
        for i in range(len(remain_comb_list2) - 1, -1, -1):
            ab = check_ab(guess_number_str, remain_comb_list2[i])
            if guess_result[0] != ab[0] or guess_result[1] != ab[1]:
                del remain_comb_list2[i]

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
