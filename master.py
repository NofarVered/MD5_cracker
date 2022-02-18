#!/usr/bin/env python3
# Usage: python master.py -f ./test/hashes.txt -t 4

import hashlib
import argparse
from popular_passwords_struct import popularPasswords


# Assumption: the number of popular passwords is less than the number of hashes passwords
# so I choose the data structure with a smaller number of objects.
def cheack_popular_passwords(hashes, founds):
    for key, val in popularPasswords.items():
        if key in hashes:
            founds[key] = val
            hashes.remove(key)


def open_read_hashes_file(file, hashes):
    with open(file, 'r') as f:
        for line in f:
            hashes.add(line.strip('\n'))


def creat_output_file(founds):
    output_f = open("output.txt", mode="w")
    for key, val in founds.items():
        output_f.write(key + ":" + val + "\n")
    output_f.close


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-f', help='File containing hashes', dest='file')
    parser.add_argument('-t', help='Number of threads',
                        dest='threads', type=int)
    args = parser.parse_args()
    file = args.file
    assert file
    threads_cnt = args.threads or 4
    founds = dict()
    hashes = set()
    open_read_hashes_file(file, hashes)
    cheack_popular_passwords(hashes, founds)
    # 1 --- create threads
    # 2 --- do some shit inside the threads
    # 3 --- @ Function definitions
    # 4 --- Read me file
    creat_output_file(founds)
