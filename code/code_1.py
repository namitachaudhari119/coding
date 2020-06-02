def find_elements(arr):
    list_1 = list(arr)

    sum_dict = dict()
    list_len = len(list_1)
    for i in range(list_len - 1):
        for j in range(i + 1, list_len):
            sum_res = list_1[i] + list_1[j]

            if sum_res in sum_dict.keys():
                value = sum_dict.get(sum_res)
                print("The pair are:", str(value) + " and (%d, %d)"
                      % (list_1[i], list_1[j]))
                return True
            else:
                sum_dict[sum_res] = (list_1[i], list_1[j])

    print("No pairs found")


array_1 = {3, 4, 7, 1, 2, 9, 8}
find_elements(array_1)

# array_2 = {65, 30, 7, 90, 1, 9, 8}
# find_elements(array_2)

# output of array_1: The pair are: (1, 4) and (2, 3)
# output of array_2: No pairs found
