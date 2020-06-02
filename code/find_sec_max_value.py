def find_sec_max_value(l1):
    max_num = l1[0]
    sec_max_num = l1[0]

    for x in l1:
        if max_num < x:
            sec_max_num = max_num
            max_num = x
        elif x > sec_max_num:
            sec_max_num = x

    print("Max number: {}".format(max_num))
    print("The second max number: {}". format(sec_max_num))


# find_sec_max_value([-5,-6,3,-2,5,10])
find_sec_max_value([15, 10, 50, 30, 140])
