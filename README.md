# MD5_cracker

There is two ways to run this code, with the tester (with a random passwords file that the tester generate ) or without, on a real file!

--- If you want to check with your own file, try:
python master.py -f ./test/hashes.txt -t 4
./test/hashes.txt, is an example for a directory path
and 4 is the number of threads you want, you can choose whatever you want, the defult is 4.

--- For a tester check, try:
python ./test/tester.py

# time

BY MY TESTS:
A file with a hundred passwords took my computer, a pretty lame machine with two cores, 3.05209198395411 minutes (183.1255190372467 seconds).
