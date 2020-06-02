def compare_triplets(l1, l2):
    a = b = 0
    l3 = []

    for x in range(len(l1)):
        if l1[x] > l2[x]:
            a += 1
        elif l1[x] == l2[x]:
            continue
        else:
            b += 1

    l3.append(a)
    l3.append(b)

    print(l3)


compare_triplets([17, 28, 30], [99, 16, 8])
# compare_triplets([5, 6, 7], [3, 6, 10])
