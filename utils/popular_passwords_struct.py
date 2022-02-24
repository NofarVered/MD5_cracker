import hashlib

NUM_OF_DIGITS = 8
# My assumption: the number of popular passwords is less than the number of hashes passwords.
# so I choose to go over the data structure with a smaller number of objects - popularPasswords.
# in case it is wrong, I will just need to go over the hashes-set.


def cheack_popular_passwords(hashes, founds):
    for key, val in popularPasswords.items():
        if key in hashes:
            founds[key] = val
            hashes.remove(key)
            print("------------------ Hit with popular passwords dicionary!")


# Popular passwords like ascending series, descending series and series with identical numbers.
# THE SCHEMA --- "the_encrypted_password":"the_decrypted_password"
popularPasswords = dict()
ser1 = '05'+''.join(["{}".format(num)
                    for num in range(1, NUM_OF_DIGITS+1)])  # 1 to 8
ser2 = '05'+''.join(["{}".format(num)
                    for num in range(NUM_OF_DIGITS, -1, -1)])  # 8 to 1
popularPasswords[hashlib.md5(ser1.encode("utf-8")).hexdigest()] = ser1
popularPasswords[hashlib.md5(ser2.encode("utf-8")).hexdigest()] = ser2

for i in range(0, NUM_OF_DIGITS+1):
    current_series = ('05'+''.join(["{}".format(i)
                      for num in range(0, NUM_OF_DIGITS)]))  # same number 8 times
    popularPasswords[hashlib.md5(current_series.encode(
        "utf-8")).hexdigest()] = current_series
