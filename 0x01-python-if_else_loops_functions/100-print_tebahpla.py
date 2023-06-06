#!/usr/bin/python3
output = ''
for i in range(ord('z'), ord('a') - 1, -1):
    output += chr(i % 32 + ord('a' if i % 64 < 32 else 'A'))
print(output)
