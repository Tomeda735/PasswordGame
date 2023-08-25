import random

print("Приветствую. В этой игре тебе предстоит угадать пароль, загаданный компьютером."
      " Пароль состоит  из четырёх цифр. у тебя есть 15 попыток.")

code = str(random.randint(1111, 9999))
e = []
for i in code:
    e.append(int(i))
code = e
answer = 0

while answer < 15:
    a = input("Введите пароль: ")
    complete_parse = True

    h = []
    for i in a:  # a = '1234' '1' -> 1, i = '2' -> 2
        try:
            h.append(int(i))  # c = [1, 2, 3, 4]
        except ValueError:
            complete_parse = False
            break

    if not complete_parse:
        print("Можно вводить только цифры")
        break
    a = h
    if len(a) != 4:
        print("Можно вводить только четыре цифры")
        break
    # a = [int(i) for i in a]
    b = 0
    if (a[0] == code[0]) and (a[1] == code[1]) and (a[2] == code[2]) and (a[3] == code[3]):
        print("Вы угадали пароль.")
        break

    for i in range(len(a)):
        if a[i] == code[i]:
            print(f'Цифра совпала на позиции: {i + 1}')

    for i in range(len(code)):
        if code[i] in a:
            b += 1

    print(f'\n\nОбщее число совпавших цифр: {b}\n')
    answer += 1

if answer == 15:
    print("Слишком много попыток")
