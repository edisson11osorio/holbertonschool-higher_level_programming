#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    av = (sys.argv)
    argv_len = len(av)
    result = 0

    if argv_len > 1:
        for i in range(1, argv_len):
            result += int(av[i])

    print(result)
