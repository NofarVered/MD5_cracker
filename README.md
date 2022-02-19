# MD5_cracker

There are two ways to run this code, (1) with the tester (100 random MD5 passwords file that the tester generates ) or (2) without, on a real file.

- (1) For a tester check, try:

**_ python ./test/tester.py _**

After the test all the files are deleted automatically ... also the output.

- (2) If you want to check with your own file, try:

**_ python master.py -f ./test/hashes_example.txt -t 4 _**

"./test/hashes.txt" is an example for a directory path,

and 4 is the number of threads you want, you can choose any number you want, the defult is 4.

# time

BY MY TESTS:

A file with a hundred passwords took my computer, a pretty lame machine with two cores, 3.05209198395411 minutes (= 183.1255190372467 seconds).
