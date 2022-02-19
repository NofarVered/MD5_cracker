#!/usr/bin/env python3
import os
from file_generator import add_hashes_files


if __name__ == "__main__":
    add_hashes_files()
    os.system('python master.py -f ./test/hashes.txt')
    results = set()
    with open("./test/results.txt", 'r') as f:
        for line in f:
            results.add(line.strip('\n'))
    ans = True
    with open("output.txt", 'r') as f:
        for line in f:
            if line.strip('\n') not in results:
                ans = False
                break
    if ans:
        print(" ------------------ Success! ")
    else:
        print(" ------------------ Somthing is Wrong... ")
    os.remove("./test/results.txt")
    os.remove("output.txt")
    os.remove("./test/hashes.txt")
