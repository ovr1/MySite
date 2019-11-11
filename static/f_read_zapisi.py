file_name = 'number.txt'

print("Ваши записи: \n")
with open(file_name, 'r', encoding='utf-8') as f:
    text = f.readlines()
    for line in text:
        bs = eval(str(line[1:-2]))
        print(bs['E-mail'])
        print(bs['-Месяц-'])
        print(bs['-Дата-'])
        print(bs['-Время-'])
        print(bs['-Место-'])
        print('\n')