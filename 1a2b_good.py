# 5位數
# 0~9 任意組合 0123 ok 0011 no ok
#
import time

from functions import create_all_comb, check_ab, choice_number, get_count_dict

digital = 4
all_comb_list1 = create_all_comb(digital)
remain_comb_list2 = create_all_comb(digital)

guess_count = 0

# while True:
start_time = time.time()
guess_time = 100  # len(all_comb_list1)
# for answer in ['1398']:
for answer in all_comb_list1[:guess_time]:
    remain_comb_list2 = create_all_comb(digital)
    while True:
        # 選數字
        max_count_ch_list = list(get_count_dict(remain_comb_list2).keys())[:digital]
        guess_number_str = choice_number(digital, max_count_ch_list, remain_comb_list2)
        # guess_number_str = random.choice(remain_comb_list2) # 65078
        # print(guess_number_str)
        guess_count += 1

        # 刪數字
        guess_result = check_ab(answer, guess_number_str)
        # # 猜數字
        # a = int(input('a:'))
        # b = int(input('b:'))
        # guess_result = (a, b)
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
