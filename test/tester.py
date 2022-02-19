from file_generator import add_hashes_files
# import master


if __name__ == "__main__":
    # create hashes and results files
    add_hashes_files()
    # compare between the results file to the output file (line by line)
    results = set()
    with open("./test/results.txt", 'r') as f:
        for line in f:
            results.add(line.strip('\n'))
    with open("output.txt", 'r') as f:
        for line in f:
            if line.strip('\n') not in results:
                print("something wrong...")
