digital = 4

self_guess_time = 0

while True:
    # 選數字
    if self_guess_time < 10 // digital:
        guess_number_str = '0123456789'[self_guess_time * digital:(self_guess_time + 1) * digital]
        print(guess_number_str)
    self_guess_time += 1

