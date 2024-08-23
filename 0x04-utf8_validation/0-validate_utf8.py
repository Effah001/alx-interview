#!/usr/bin/python3
"""
A method that determines if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    num_bytes = 0
    mask_1 = 1 << 7
    mask_2 = 1 << 6

    for byte in data:
        byte = byte & 0xFF

        if num_bytes == 0:
            if byte & mask_1 == 0:
                continue
            elif byte & (mask_1 | mask_2) == mask_1:
                num_bytes = 1
            elif byte & (mask_1 | mask_2 | (1 << 5)) == (mask_1 | mask_2):
                num_bytes = 2
            elif byte & (mask_1 | mask_2 | (1 << 5) | (1 << 4)) == (
                    mask_1 | mask_2 | (1 << 5)):
                num_bytes = 3
            else:
                return False
        else:
            if byte & (mask_1 | mask_2) != mask_2:
                return False
            num_bytes -= 1

    return num_bytes == 0
