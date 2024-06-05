file_name = 'pomesch.txt'
with open(file_name, mode='r', encoding='utf8') as file:
    for line in file:
        print(line.upper()[:1] + '.' + list[1:])


# как сделать все буквы в верхнем регистре и после второго символа поставить во всех элементах точку
# было 3б8.1     стало 3Б.8.1
#      2б1             2Б.1



