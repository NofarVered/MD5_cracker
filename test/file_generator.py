import hashlib
import string
import random

f = open("./test/hashes.txt", mode="w")
for i in range(0, 101):
    num = '05'+''.join(random.choice(string.digits)
                       for _ in range(8))
    f.write(hashlib.md5(num.encode(
        "utf-8")).hexdigest()+'\n')

print('hashes file created, and ready for tests!')
f.close
