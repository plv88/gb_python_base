# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма.
# Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки. Выведите соответствующее сообщение.

while True:
    try:
        billing = int(input("Введите выручку вашкей фирмы, только целые числа) "))
        costs = int(input("Введите издержки фирмы, только целые числа) "))
        break
    except:
        print("Не могу посчитать, введите корректные цифры")

if billing > costs:
    print(f"Фирма работает с прибылью - {billing - costs}")
elif billing < costs:
    print(f"Фирма работает с убытком - минус {costs - billing}")
else:
    print("Фирма в нуле")
