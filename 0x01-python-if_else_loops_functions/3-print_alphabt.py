#!/usr/bin/python3
for letters in range(97, 123):
    if not letters == 101 and not letters == 113:
        print("{}".format(chr(letters)), end="")
