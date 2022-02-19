import hashlib
import string
import random


def add_hashes_file():
    f = open("./test/hashes.txt", mode="w")
    for i in range(0, 101):
        num = '05'+''.join(random.choice(string.digits)
                           for _ in range(8))
        f.write(hashlib.md5(num.encode(
            "utf-8")).hexdigest()+'\n')
    print('------------------ Hashes file created, and ready for tests!')
    f.close
