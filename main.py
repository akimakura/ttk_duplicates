import numpy as np
import pandas as pd

import time

start_time = time.time()

# указываем путь к файлу/название файла, пропускаем первую заголовочную строку, указываем номер страницы
# при помощи .iloc записываем нужный нам столбец
open_one = pd.read_excel('exl_ttk/1_one_ttk.xls', engine='xlrd', skiprows=0, sheet_name=[1, 2])
one_data = pd.concat([open_one[i].iloc[:, 1] for i in open_one.keys()], axis=0)

open_two = pd.read_excel('exl_ttk/2_two_ttk.xlsx', engine='xlrd', skiprows=0, sheet_name=[1, 2])
two_data = pd.concat([open_two[i].iloc[:, 1] for i in open_two.keys()], axis=0)

# open_one = pd.read_excel('exl/1_one_ttk.xlsx', skiprows=1, sheet_name=1)
# one_data = open_one.iloc[:, 1]
# open_two = pd.read_excel('exl/2_two_ttk.xlsx', skiprows=1, sheet_name=2)
# two_data = open_two.iloc[:, 1]



# превращаем наши данные в массив numpy
one_arr = one_data.to_numpy()
two_arr = two_data.to_numpy()

# меняем тип данных на строковый //тк вылезает float//
one_arr = one_arr.astype(str)
two_arr = two_arr.astype(str)



# выбираем наиболее короткий массив, чтобы начать с него //оптимизация
# бинарным поиском ищем и записываем дубликаты (тех клиентов, у кого обе ветки связи могут быть оборваны)



# long, short = (one_arr, two_arr) if len(one_arr) > len(two_arr) else (two_arr, one_arr)
# short.sort()
# short_length = len(short)
#
# def bin_search(needle):
#     start, finish = 0, short_length - 1
#     while start <= finish:
#         mid = (start + finish) // 2
#         if short[mid] < needle:
#             start = mid + 1
#         elif short[mid] > needle:
#             finish = mid - 1
#         else:
#             return True
#     return False
#
# result = [item for item in long if bin_search(item)]
# print(result)

# def ukazateli(arr1, arr2):
#     arr1.sort()
#     arr2.sort()
#     duplicates = []
#     ptr1, ptr2 = 0, 0
#
#     while ptr1 < len(arr1) and ptr2 < len(arr2):
#         if arr1[ptr1] == arr2[ptr2]:
#             duplicates.append(arr1[ptr1])
#             ptr1 += 1
#             ptr2 += 1
#         elif arr1[ptr1] < arr2[ptr2]:
#             ptr1 += 1
#         else:
#             ptr2 += 1
#
#     return duplicates
#
# result = ukazateli(one_arr, two_arr)
# print(result)


def hash(arr1, arr2):
    hash_table = {}
    for word in arr1:
        hash_table[word] = hash_table.get(word, 0) + 1
#
    duplicates = []
#
    for word in arr2:
        if word in hash_table and hash_table[word] > 0:
            duplicates.append(word)
            hash_table[word] -= 1
    return duplicates
#
result = hash(one_arr, two_arr)
print(result)



# создаем excel файл
data_frame = pd.DataFrame(result)
excel_file = 'exl/new_xl.xlsx'
data_frame.to_excel(excel_file, index=False)



end_time = time.time()
excution_time = end_time - start_time
print(excution_time)