#notes to myself to handle:
-Your solution should include crash handling (What happens if any of the minions, or
the master, stops in mid-run).

# MD5_cracker

There are two ways to run this code, (1) with the tester (100 random MD5 passwords file that the tester generates ) or (2) without, on a real file.

- (1) For a tester check, try:

**_ python ./test/tester.py _**

After the test all the files are deleted automatically ... also the output.

- (2) If you want to check with your own file, try:

**_ python master_server.py -f ./test/hashes_example.txt -t 4 _**

"./test/hashes_example.txt" is just an example for a directory path, and 4 is the number of threads you want, you can choose any number you want, the defult is 4.

# output

The output is a file that will wait for you, if anything didn't went wrong, at the same folder with the master.py.
The schema of the output.txt is : "the_encrypted_password":"the_decrypted_password". Also, the script prints the computation time.

# time

BY MY TESTS:

A file with a hundred passwords took my computer, a pretty lame machine with two cores, 3.05209198395411 minutes (= 183.1255190372467 seconds).

# Example hashes file

There is a hashes_example.txt file for your own use.
