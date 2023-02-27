# lines_list = []
with open('1.txt', 'r', encoding='utf-8') as f_1:
	lines_1 = len(f_1.readlines())
	print('Total Number of lines:', lines_1)

with open('2.txt', 'r', encoding='utf-8') as f_2:
	lines_2 = len(f_2.readlines())
	print('Total Number of lines:', lines_2)
	
with open('3.txt', 'r', encoding='utf-8') as f_3:
	lines_3 = len(f_3.readlines())
	print('Total Number of lines:', lines_3)
	
if lines_1 < lines_2 and lines_2 < lines_3:
	1, 2, 3
elif lines_1 < lines_2 and lines_3 < lines_2 and lines_1 < lines_3:
	1, 3, 2

# min()