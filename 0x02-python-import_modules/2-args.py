#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    str(sys.argv)
    argv_len = len(sys.argv) - 1

    if argv_len > 1:
        print("{:d} arguments:".format(argv_len))
        for i in range(1, argv_len + 1):
            print("{:d}: {:s}".format(i, sys.argv[i]))
    elif argv_len == 1:
        print("1 argument:")
        print("{:d}: {:s}".format(argv_len, sys.argv[1]))
    elif argv_len == 0:
        print("0 arguments.")
