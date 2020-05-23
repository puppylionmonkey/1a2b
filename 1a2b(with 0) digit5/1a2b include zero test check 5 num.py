#
# Guess Number Game (Master Mind or 1A2B Game)
#
from random import choice


def digit5(n):
    n1 = int(n / 10000)
    n2 = int((n - n1 * 10000) / 1000)
    n3 = int((n - n1 * 10000 - n2 * 1000) / 100)
    n4 = int((n - n1 * 10000 - n2 * 1000 - n3 * 100) / 10)
    n5 = n - n1 * 10000 - n2 * 1000 - n3 * 100 - n4 * 10
    return (n1, n2, n3, n4, n5)


def isvalid(n):
    d = digit5(n)
    if n < 1234 or n > 98765:
        return False
    if d[0] == d[1] or d[0] == d[2] or d[0] == d[3] or d[0] == d[4] \
            or d[1] == d[2] or d[1] == d[3] or d[1] == d[4] \
            or d[2] == d[3] or d[2] == d[4]:
        return False
    return True


def checkab(m, n):
    a, b = 0, 0
    c, d = digit5(m), digit5(n)
    if c[0] == d[0]: a = a + 1
    if c[1] == d[1]: a = a + 1
    if c[2] == d[2]: a = a + 1
    if c[3] == d[3]: a = a + 1
    if c[4] == d[4]: a = a + 1
    if c[0] == d[1] or c[0] == d[2] or c[0] == d[3] or c[0] == d[4]: b = b + 1
    if c[1] == d[0] or c[1] == d[2] or c[1] == d[3] or c[1] == d[4]: b = b + 1
    if c[2] == d[0] or c[2] == d[1] or c[2] == d[3] or c[2] == d[4]: b = b + 1
    if c[3] == d[0] or c[3] == d[1] or c[3] == d[2] or c[3] == d[4]: b = b + 1
    return (a, b)


def numfilter(n, a, b):
    for i in range(len(numlist) - 1, -1, -1):
        x = checkab(n, numlist[i])
        if x[0] != a or x[1] != b: del numlist[i]


# start
dict_answer = dict()
for answer in range(1234, 98766):
    str_a = str(answer)
    if len(str_a) == 4:
        str_a = "0" + str_a
    if str_a[0] == str_a[1] or str_a[0] == str_a[2] or str_a[0] == str_a[3] or str_a[0] == str_a[4]\
            or str_a[1] == str_a[2] or str_a[1] == str_a[3] or str_a[1] == str_a[4]\
            or str_a[2] == str_a[3] or str_a[2] == str_a[4]:
        continue
    # print(answer, ":", end=" ")
    count = 0
    numlist = []
    for i in range(1234, 98766):
        if isvalid(i):
            numlist.append(i)
    while True:
        count += 1
        guessnum = choice(numlist)
        # if len(str(guessnum)) == 4:
        #     print("I guess the number in your mind is:", "0" + str(guessnum))
        # else:
        #     print("I guess the number in your mind is: %d" % guessnum)
        xa, xb = checkab(guessnum, answer)
        numfilter(guessnum, int(xa), int(xb))
        if len(numlist) == 1:
            # if len(str(numlist[0])) == 4:
            #     print("Thanks! The answer is", "0" + str(numlist[0]), "!")
            # else:
            #     print("Thanks! The answer is %d!" % numlist[0])
            break
        # elif len(numlist) == 0:
        #     print("Oops, something is wrong!")
        #     break
    print(count)
    dict_answer[answer] = count
print(dict_answer)