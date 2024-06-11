file_name = 'pomesch.txt'
with open(file_name, mode='r', encoding='utf8') as file:
    for line in file:
        stroka_s_to4koj = line[:2] + '.' + line[2:]
        stroka_s_to4koj_UP = stroka_s_to4koj.upper().strip()
        print(stroka_s_to4koj_UP)






