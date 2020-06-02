def capital(string):
    new_str = ''
    for s in string:
        if s == 'l':
            new_str += s.upper()
        else:
            new_str += s
    print(new_str)


capital("Hello")
