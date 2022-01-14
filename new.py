import os

def write_file(result_file):
    str_dict = dict()
    temp_dict= dict()
    path = '2.4.files/sorted'
    path_1 = '2.4.files'
    res = sorted(os.listdir(path))
    with open(os.path.join(path_1,result_file), "a", encoding="utf-8") as file_1:
        for file_name in res:
            temp_list = list()
            count = 0
            with open(os.path.join(path, file_name), "r", encoding="utf-8") as file:
                for count, line in enumerate(file):
                    temp_list.append(line)
                str_dict[file_name] = temp_list
                count += 1
                temp_dict[count] = file_name
        list_keys = list(temp_dict.keys())
        list_keys.sort()
        for item in list_keys:
            file_1.write(f'{temp_dict[item]}\n {"".join(str_dict[temp_dict[item]])}\n\n')

write_file('4.txt')