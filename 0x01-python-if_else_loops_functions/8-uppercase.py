#!/usr/bin/python3
def uppercase(str):
    for c in str:
        ord_str = ord(c)
        if ord_str > 96 and ord_str < 123:
            ord_str -= 32
        print("{}".format(chr(ord_str)), end='')
    print(end='\n')
