file_name = 'registration3.txt'

print("Список пациентов: \n")
with open(file_name, 'r', encoding='utf-8') as f:
    contents = f.readlines()
    for line in contents:
        ds = eval(str(line[1:-2]))
        for k, v in ds.items():
            print(v)
        print('\n')





