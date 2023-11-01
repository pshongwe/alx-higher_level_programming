#!/usr/bin/python3
count = 0
for char_code in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(char_code - count)), end='')
    count = 32 if count == 0 else 0
