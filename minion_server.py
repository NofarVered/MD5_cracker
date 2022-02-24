from tkinter import EXCEPTION
import hashlib


# each thread will go over all the numbers in his given range, from start-number to end-number.
# then, will check if the current number guess is in the hashes-set (should we crack it?)
# for true only, we will put the deciphering password at founds-dictionary and remove it from hashes-set (cause we already cracked it)
# there is no need for locks- the diffrent ranges give us isolation at the add, remove and search actions.
def guess_numbers(start, end, hashes, founds):
    try:
        for num in range(start, end+1):
            current_guess = '05' + str(num).zfill(8)
            enc_curr_guess = hashlib.md5(
                current_guess.encode("utf-8")).hexdigest()
            if enc_curr_guess in hashes:
                founds[enc_curr_guess] = current_guess
                hashes.remove(enc_curr_guess)
    except EXCEPTION as e:
        print("------------------ ERROR - inside the thread")
        print(e)
        pass
