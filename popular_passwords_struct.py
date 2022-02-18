# Popular passwords like ascending series, descending series and series with identical numbers.
# THE SCHEMA --- "the_encrypted_password":"the_decrypted_password"
import hashlib


popularPasswords = dict()

ser1 = ''.join(["{}".format(num) for num in range(0, 9)])
ser2 = ''.join(["{}".format(num) for num in range(8, -1, -1)])
popularPasswords[hashlib.md5(ser1.encode("utf-8")).hexdigest()] = ser1
popularPasswords[hashlib.md5(ser2.encode("utf-8")).hexdigest()] = ser2

for i in range(0, 9):
    current_series = (''.join(["{}".format(i) for num in range(0, 9)]))
    popularPasswords[hashlib.md5(current_series.encode(
        "utf-8")).hexdigest()] = current_series
