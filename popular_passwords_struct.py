import hashlib

# Popular passwords like ascending series, descending series and series with identical numbers.
# THE SCHEMA --- "the_encrypted_password":"the_decrypted_password"
popularPasswords = dict()
ser1 = '05'+''.join(["{}".format(num) for num in range(1, 9)])  # 1 to 8
ser2 = '05'+''.join(["{}".format(num) for num in range(8, -1, -1)])  # 8 to 1
popularPasswords[hashlib.md5(ser1.encode("utf-8")).hexdigest()] = ser1
popularPasswords[hashlib.md5(ser2.encode("utf-8")).hexdigest()] = ser2

for i in range(0, 9):
    current_series = ('05'+''.join(["{}".format(i)
                      for num in range(0, 8)]))  # same number 8 times
    popularPasswords[hashlib.md5(current_series.encode(
        "utf-8")).hexdigest()] = current_series
