def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for current_num in numbers:
        try:
            result += current_num
        except TypeError:
            incorrect_data += 1
            print('Некорректный тип данных для подсчета суммы:', current_num)

    return (result, incorrect_data)


def calculate_average(numbers):
    try:
        try:
            sum_val, incorrect_val = personal_sum(numbers)
            average_sum = sum_val / (len(numbers) - incorrect_val)
        except ZeroDivisionError:
            average_sum = 0
        return (average_sum)
    except TypeError:
        print('В numbers записан некорректный тип данных')


print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
