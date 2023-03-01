class FilesParser:

    def make_list_with_metadata_path(self, path):
        with open(path) as f:
            strings = f.readlines()
        return [path.split('/')[-1], len(strings)] + [el.strip() for el in strings]       

if __name__ == '__main__':
    file_class = FilesParser()
    file1 = r'https://raw.githubusercontent.com/netology-code/py-homework-basic-files/master/2.4.files/sorted/1.txt'
    file2 = r'https://raw.githubusercontent.com/netology-code/py-homework-basic-files/master/2.4.files/sorted/2.txt'
    file3 = r'https://raw.githubusercontent.com/netology-code/py-homework-basic-files/master/2.4.files/sorted/3.txt'
    list_of_paths = [file1, file2, file3]
    list_of_files = []
    for path in list_of_paths:
        file = file_class.make_list_with_metadata_path(path)
        list_of_files.append(file)
    list_of_files = sorted(list_of_files, key=lambda file: file[1])
    for file in list_of_files:
        print(*file, sep='\n')

