# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number_list = input('Введите целое положительное число ')

count = 0
max_num = 0
while len(number_list) > count:
    number = int(number_list[count])
    if (max_num < number):
        max_num = number
    count += 1
print(f'Самое большое число из {number_list} - {max_num}')

i = 10
temp_num = 0
number = int(number_list)
while number / i > 1:
    if temp_num < int(number / i) % 10:
        temp_num = int(number / i) % 10
    i = i*10
print(f'Самое большое число из {number_list} - {temp_num}')
