import time
import datetime

# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и
# выведите в формате чч:мм:сс. Используйте форматирование строк.

time_sec = int(input("Введите время в секундах, я переведу в формат чч:мм:сс "))

hour = time_sec // 3600
minute = (time_sec - (hour * 3600)) // 60
second = time_sec - (hour * 3600) - (minute * 60)

print("Получилось: {:02}:{:02}:{:02}".format(hour, minute, second))

# нашел в яндексе еще 2 варианта
#str_time_1 = time.strftime("%H:%M:%S", time.gmtime(time_sec))
print(f"Получилось через (time.gmtime): {time.strftime('%H:%M:%S', time.gmtime(time_sec))}")
print(f"Получилось через (timedelta): {str(datetime.timedelta(seconds = time_sec))}")