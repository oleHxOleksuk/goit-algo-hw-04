def get_cats_info(path):
    pet_list = []
    try:
        with open(path, 'r') as list:
            for line in list:
                all_line = line.strip().split(",")
                if len(all_line) == 3:
                    new_dict = {'id': all_line[0], 'name': all_line[1], 'age' : all_line[2]}
                    pet_list.append(new_dict)
                else:
                    return print('Incorrect data format')
    except FileNotFoundError:
        return print(f'file {path} not found')
    return pet_list

print(get_cats_info('./Task_2/cats_file.txt'))