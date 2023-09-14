def main_menu():
    while True:
        print("Главное меню:")
        print("1. Вывести на экран 51 простое число")
        print("2. Наиболее частый символ в строке")
        print("3. Задание 3")
        print("4. Три самых маленьких значений в словаре")
        print("5. Задание 5")
        print("6. Сумма четных чисел кортежа")
        print("7. Выйти")

        choice = input("Выберите пункт меню: ")

        if choice == '1':
            count = 0
            number = 2

            while count < 51:
                if number > 1:
                    for i in range(2, number):
                        if (number % i) == 0:
                            break
                    else:
                        print(number)
                        count += 1
                number += 1
            pass
        elif choice == '2':
            print("Введите строку")
            from collections import Counter
            stroka = input()
            c = Counter(stroka)
            print(f"Наиболее встречающийся символ = {c.most_common(1)[0][0]}")
            rever_stroka = stroka[::-1]
            print(f"Строка в обратном порядке {rever_stroka}")
            pass
        elif choice == '3':

            my_list = [13, 56, 'Python', 34, 19, 'love']
            num_list=[x for x in my_list if isinstance(x, int)]
            for i in num_list:
                if i%2==0:
                    num=i
                    result=1
                    while num > 0:
                        digit = num % 10
                        result *= digit
                        num //= 10
                    print(result)
                else:
                    index = num_list.index(i)
                    num_list[index] = 1
            print(num_list)
            pass
        elif choice == '4':
            my_dict = {'a': 50, 'b': 5, 'c': 56, 'd': 4, 'e': 58, 'f': 20}
            sorted_values = sorted(my_dict.values())
            for i in range(3):
                print(sorted_values[i])
            pass
        elif choice == '5':

            pass
        elif choice == '6':
            input_string = input("Введите целые числа через пробел: ")
            numbers = [int(num) for num in input_string.split()]
            kor = tuple(numbers)
            sum=0
            for num in kor:
                if num%2==0:
                    sum+=num
            print(f"Сумма = {sum}")
            pass
        elif choice == '7':
            print("Выход из программы")
            break
        else:
            print("Некорректный ввод, введите верное значение")

main_menu()