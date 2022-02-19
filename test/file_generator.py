import hashlib
import string
import random


def add_hashes_files():
    f = open("./test/hashes.txt", mode="w")
    r = open("./test/results.txt", mode="w")
    for i in range(0, 100):
        num = '05'+''.join(random.choice(string.digits) for _ in range(8))
        num_after_hash = hashlib.md5(num.encode("utf-8")).hexdigest()
        f.write(num_after_hash+'\n')
        r.write(num_after_hash + ':' + num+'\n')
    f.close
    r.close
    print('------------------ Hashes file created, and ready for tests!')
