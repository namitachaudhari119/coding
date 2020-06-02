# find 3 consecutive numbers to get the highest sum
def find_numbers(list_1):
    max_sum = 0
    max_numbers = ()

    for x in range(len(list_1) - 2):
        res = list_1[x] + list_1[x + 1] + list_1[x + 2]
        if max_sum < res:
            max_sum = res
            max_numbers = (list_1[x], list_1[x + 1], list_1[x + 2])

    print("The consecutive numbers for max_sum {} is {}:".format(max_sum, max_numbers))


find_numbers([2, 4, 1, 9, 4, 5, 7, 8, 3, 4, 6])
