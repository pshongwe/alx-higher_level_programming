#!/usr/bin/python3
for char_code in range(ord('a'), ord('z') + 1):
    if char_code == 101 or char_code == 113:
        continue
    else:
        print("{}".format(chr(char_code)), end="")
