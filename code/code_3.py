def find_substring(string):
    new_string = ''
    for i in string:
        if i not in new_string:
            new_string += i
    print("The substring is: {} and length is {}".format(new_string, len(new_string)))


# find_substring("namita")
# output: The substring is: namit and length is 5

# find_substring("Chaudhari")
# output: The substring is: Chaudri and length is 7

find_substring("abcabcbb")
# output: The substring is: abc and length is 3
