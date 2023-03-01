# lines_list = []
# with open('1.txt', 'r', encoding='utf-8') as f_1:
# 	# lines_1 = len(f_1.readlines())
# 	# res = '1.txt', lines_1
# 	file_number = 1
# 	f_4.write(f'{file_number}.txt')
# 	f_4.write(len(f_1.readlines()))
# 	n = 1
# 	for _ in range(len(f_1.readlines())):
# 		f_4.write(f'Строка номер {n} файла номер {file_number}')
# 		n += 1

# 	# print('Total Number of lines:', lines_1)
# with open('2.txt', 'r', encoding='utf-8') as f_2:
# 	lines_2 = len(f_2.readlines())
# 	# print('Total Number of lines:', lines_2)	
# with open('3.txt', 'r', encoding='utf-8') as f_3:
# 	lines_3 = len(f_3.readlines())
# 	# print('Total Number of lines:', lines_3)


# if lines_1 < lines_2 and lines_2 < lines_3:
# 	1, 2, 3
# elif lines_1 < lines_2 and lines_3 < lines_2 and lines_1 < lines_3:
# 	1, 3, 2
# min()

# with open('4.txt', 'w') as f_4:
# 	with open('1.txt', 'r', encoding='utf-8') as f_1:
# 		file_number = 1
# 		f_4.write(f'{file_number}.txt\n')		
# 		f_4.write(f'{str(len(f_1.readlines()))}\n')
# 		n = 1
# 		# f_4.write(str(file_number))
# 		for line in f_1:
# 			# stroke_count = int(f_1.readline)
# 			f_4.write('rrrrr')
# 			for _ in range(stroke_count):
# 				f_4.write('55555')
# 				f_4.write(f'Строка номер {n} файла номер {file_number}')
# 				n += 1
# f = open ('1.txt', 'r', encoding='utf-8')
# f.read()
# f.close()


        # with open(fname) as infile:
        #     outfile.write(infile.read())

# class FilesChange:
filenames = ['1.txt', '2.txt', '3.txt']
    # def make_list_with_metadata_path(self, filenames):
for fname in filenames:
    with open(fname, 'r', encoding='utf-8') as outfile:
                # file_number = 1
        # 		f_4.write(f'{file_number}.txt\n')		
        # 		f_4.write(f'{str(len(f_1.readlines()))}\n')
        # 		n = 1
        # 		# f_4.write(str(file_number))
        strings = outfile.readlines()
                # new_file = FilesChange()
        new_file = [fname.split('/')[-1], len(strings)] + [el.strip() for el in strings]
        
        print(new_new)
                # print([fname.split('/')[-1], len(strings)] + [el.strip() for el in strings])
                # return
        
