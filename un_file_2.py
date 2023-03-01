# import os
# combined_list = []
# file_list = ['1.txt', '2.txt', '3.txt']

# for file in file_list:
#     with open(file, 'r', encoding='utf-8') as cur_file:
#       for line in cur_file:



#         combined_list[-1][2].append(line.strip())
#         combined_list[-1][1] += 1

# return sorted(combined_list, key= lambda x: x[2], reverse = True)

# def create_file_from_directory(directory):
#   with open ('combined.txt', 'w+') as newfile:
#       for file in create_combined_list(directory):
#         newfile.write(f'File name: {file[0]}\n')
#         newfile.write(f'Length: {file[1]} string(s)\n')
#         for string in file[2]:
#           newfile.write(string + '\n')
#         newfile.write('-------------------\n')

# create_file_from_directory('C:\PYTHON\GIT\python_GitHub_projects\hw_open_read_write_file')

filenames = ['1.txt', '2.txt', '3.txt']
with open('4.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            outfile.write(infile.read())