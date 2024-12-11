def total_salary(path):
    total = 0
    count = 0
    try:
        with open(path, "r") as salary:
            for num in salary:
                all_num = num.strip().split(",")
                if len(all_num) == 2:
                    try:
                        total += int(all_num[1])
                        count += 1
                    except ValueError:
                        return print("Incorrect salary format")
                else:
                    return print('Incorrect data format')
        if count > 0:
            average = total/count
            return total, average
        else:
            return print('There is no salary data')
    except FileNotFoundError:
        return print(f'file {path} not found')
            
total, average = total_salary("./Task_1/for_task_1.txt")
print(f"Загальна сума заробітної плати: {int(total)}, Середня заробітна плата: {int(average)}")