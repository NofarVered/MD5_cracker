#!/usr/bin/env python3

import hashlib
import argparse
from popular_passwords_struct import popularPasswords
import threading

TOTAL_NUMBER = 100_000_000


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


# the tpl_rng is a tuple with start and end numbers for limit search
def guess_numbers(start, end, hashes, founds):
    for num in range(start, end+1):
        current_guess = '05' + str(num).zfill(8)
        enc_curr_guess = hashlib.md5(current_guess.encode("utf-8")).hexdigest()
        if enc_curr_guess in hashes:
            founds[enc_curr_guess] = current_guess
            hashes.remove(enc_curr_guess)


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
    print(popularPasswords)
    cheack_popular_passwords(hashes, founds)
    # --- create threads
    limit = int(TOTAL_NUMBER / threads_cnt)
    range_pool = [(end - limit, end - 1)
                  for end in range(limit, TOTAL_NUMBER+limit, limit)]
    thread = []
    try:
        for i in range(threads_cnt):
            run = threading.Thread(target=guess_numbers,
                                   args=(range_pool[i][0], range_pool[i][1], founds))
            run.start()
            thread.append(run)
        for j in thread:
            j.join()
    except:
        # print "Erro"
        pass

    # 3 --- @ Function definitions
    # 4 --- Read me file
    # 5 --- TESTER
    creat_output_file(founds)
    print("------------------ The output file is ready in your folder... :-) ")
