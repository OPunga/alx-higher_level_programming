#!/usr/bin/python3

for i in range(0, 26):
    if i not in (4, 16):
        print("{:c}".format(i + 97), end="")
