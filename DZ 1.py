# Урок 1. Знакомство с Python# 1. Поработайте с переменными, создайте несколько, выведите на экран.# Запросите у пользователя некоторые числа и строки и сохраните в переменные, затем выведите на экран.a = 10b = 5c = 25print("Данны числа:", a, b, c)print("Сумма чисел:", a + b + c)print("Перемноджение чисел:", a * b * c)number = input("Введите ваше любимое число:")text = input("Введите ваше любимое слово:")print("Ваше любимое число - это", number, "Ваше любимое слово - это", text)# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.# Используйте форматирование строк.sec = input("Введите количество секунд:")sec = int(sec)min = sec // 60sec2 = (sec % 60)hour = sec // (60 * 60)print(hour, ":", min, ":", sec2)# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.n = int(input("Введите значение n: "))nstr = str(n)nn = nstr+nstrnnn = nn + nstrsum = n + int(nn) + int(nnn)print(n, nn, nnn, "n+nn+nnn=", sum)# 4. Пользователь вводит целое положительное число.# Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.number = int(input("Введите целое положительное число:"))maxnumber = number % 10number = number // 10while number > 0:    if number % 10 > maxnumber:        maxnumber = number % 10    number = number // 10print("Самая большая цифра в числе:", maxnumber)# 5 Запросите у пользователя значения выручки и издержек фирмы.# Определите, с каким финансовым результатом работает фирма.# Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки. Выведите соответствующее сообщение.receipt = int(input("Введите значение выручки:"))expenses = int(input("Введите значение издержек:"))if receipt > expenses:    print("Ваша фирма работает хорошо, Вы богач")if receipt == expenses:    print("Фухх, Вы на мили, но никому ничего не должны")if receipt < expenses:    print("Вы банкрот")# 6. Если фирма отработала с прибылью, вычислите рентабельность выручки.# Это отношение прибыли к выручке. Далее запросите численность сотрудников фирмы# и определите прибыль фирмы в расчёте на одного сотрудника.receipt = int(input("Введите значение выручки:"))expenses = int(input("Введите значение издержек:"))if receipt > expenses:    print("Ваша фирма работает хорошо, Вы богач")    profit = receipt - expenses    rent = profit / receipt    print("Рентабельность равна", rent)    employee = int(input("Введите количество сотрудников:"))    print("Прибыль в расчете на одного сотрудника", profit / employee)else: print("Вы банкрот")# 7 (Дополнительно). Спортсмен занимается ежедневными пробежками.# В первый день его результат составил a километров. Каждый день спортсмен увеличивал результат# на 10% относительно предыдущего. Требуется определить номер дня,# на который результат спортсмена составит не менее b километров.# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.a = int(input("Введите значение а:"))b = int(input("Введите значение b:"))day = 1while a < b:    print("На", day, "спортсмен достиг результата:", a)    a = a + a / 10    day = day + 1print("На", day, "спортсмен достиг результата:", a)