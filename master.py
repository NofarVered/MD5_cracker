#!/usr/bin/env python3

import hashlib
import argparse
from popular_passwords_struct import popularPasswords
import threading

TOTAL_NUMBER = 100_000_000  # we have 10^8 option of numbers with eight digits


# open the given hashes-file and update the hashes-set with each md5-hash-password
def open_read_hashes_file(file, hashes):
    with open(file, 'r') as f:
        for line in f:
            hashes.add(line.strip('\n'))


# creat an output file for the user, using the founds dictionary.
def creat_output_file(founds):
    output_f = open("output.txt", mode="w")
    for key, val in founds.items():
        output_f.write(key + ":" + val + "\n")
    output_f.close


# My assumption: the number of popular passwords is less than the number of hashes passwords.
# so I choose to go over the data structure with a smaller number of objects - popularPasswords.
# in case it is wrong, I will just need to go over the hashes-set.
def cheack_popular_passwords(hashes, founds):
    for key, val in popularPasswords.items():
        if key in hashes:
            founds[key] = val
            hashes.remove(key)


# each thread should go over all the numbers in his range, from start-number to end-number.
# then, check if the current number guess is in the hashes-set (should we crack it?)
# for true only, we will put the deciphering password at founds-dictionary and remove it from hashes-set (cause we already found it)
def guess_numbers(start, end, hashes, founds):
    for num in range(start, end+1):
        current_guess = '05' + str(num).zfill(8)
        enc_curr_guess = hashlib.md5(current_guess.encode("utf-8")).hexdigest()
        if enc_curr_guess in hashes:
            founds[enc_curr_guess] = current_guess
            hashes.remove(enc_curr_guess)


if __name__ == "__main__":
    # handeling with files and args:
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
    # create range based the number of threads:
    limit = int(TOTAL_NUMBER / threads_cnt)
    range_pool = [(end - limit, end - 1)
                  for end in range(limit, TOTAL_NUMBER+limit, limit)]
    # create threads:
    thread = []
    try:
        for i in range(threads_cnt):
            run = threading.Thread(target=guess_numbers,
                                   args=(range_pool[i][0], range_pool[i][1], hashes, founds))
            run.start()
            thread.append(run)
        for j in thread:
            j.join()
    except:
        # print "Erro"
        pass
    # create an output file by the founds passwords:
    creat_output_file(founds)
    print("------------------ The output file is ready in your folder... :-) ")
