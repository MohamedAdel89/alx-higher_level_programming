#!/usr/bin/python3
import sys

def add_args(args):
    total = sum(int(arg) for arg in args)
    return total

if __name__ == "__main__":
    args = sys.argv[1:]  # Exclude the script name itself
    result = add_args(args)
    print(result)
