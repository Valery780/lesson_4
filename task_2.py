count = 0
summa = 0
proiz = 1
medium_value = 0

max_number = 0
max_number_index = 0
max_value_count = 0

even_number_count = 0
odd_number_count = 0

last_number = 1
second_max_value = 0

while last_number > 0:
    last_number = int(input("Введите число: "))
    if last_number == 0:
        break
    count += 1
    summa += last_number
    proiz *= last_number

    if max_number < last_number:
        second_max_value = max_number
        max_number = last_number
        max_number_index = count - 1
        max_value_count = 0

    if max_number == last_number:
        max_value_count += 1

    if last_number % 2 == 0:
        even_number_count += 1
    else:
        odd_number_count += 1

medium_value = summa/count

print(
    'количество введённых чисел', count,
    '\nsum', summa,
    '\nпроизведение', proiz,
    '\nсреднее арифметическое', medium_value,
    '\nзначение наибольшего элемента', max_number,
    '\nпорядковый номер наибольшего элемента', max_number_index,
    '\nколичество  элементов равны наибольшему элементу', max_value_count,
    '\neven_number_count', even_number_count,
    '\nodd_number_count', odd_number_count,
    '\nsecond_max_value', second_max_value,
)
