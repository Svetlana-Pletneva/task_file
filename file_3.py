from pprint import pprint
data = dict()

def read_data(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        text = file.readlines()
        data[file_name] = { 'text': text, 'count': len(text)}

    return data

def write_data(file_name):
    with open(file_name,'w', encoding='utf-8') as file:
        file.write(f'{" ".join(file_list)} \n')




read_data('1.txt')
read_data('2.txt')
read_data('3.txt')

file_list = []
max_count = 0

for count in data.values():
    file_count = count['count']
    if file_count > max_count:
        file_list.append(" ".join(count['text']))
        max_count = file_count
    else:
        file_list.insert(0, " ".join(count['text']))

write_data('4.txt')

