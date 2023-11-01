#!/usr/bin/python3
output = ""
for char_code in range(ord('a'), ord('z') + 1):
    output += chr(char_code)
print("{}".format(output), end="")
