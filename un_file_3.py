filenames = ['1.txt', '2.txt', '3.txt']
with open('4.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            outfile.write(infile.read())