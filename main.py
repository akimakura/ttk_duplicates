import numpy as np
import pandas as pd

import time

start_time = time.time()



# указываем путь к файлу/название файла, пропускаем первую заголовочную строку, указываем номер страницы
# при помощи .iloc записываем нужный нам столбец
# open_one = pd.read_excel('exl_ttk/1_one_ttk.xls', engine='xlrd', skiprows=1, sheet_name=1)
# one_data = open_one.iloc[:, 1]
# one_data = pd.concat([open_one[i].iloc[:, 1] for i in open_one.keys()], axis=0)
# open_two = pd.read_excel('exl_ttk/2_two_ttk.xls', engine='xlrd', skiprows=1, sheet_name=2)
# two_data = open_two.iloc[:, 1]
# two_data = pd.concat([open_two[i].iloc[:, 1] for i in open_two.keys()], axis=0)


# Прочитать данные из первого файла Excel, выбрав третий столбец со второй и третьей страницы
# Прочитать данные из второго файла Excel, выбрав третий столбец со второй и третьей страницы


def find_duplicates(arr1, arr2):
    arr1.sort()
    arr2.sort()
    duplicates = []
    ptr1, ptr2 = 0, 0

    while ptr1 < len(arr1) and ptr2 < len(arr2):
        if arr1[ptr1] == arr2[ptr2]:
            duplicates.append(arr1[ptr1])
            ptr1 += 1
            ptr2 += 1
        elif arr1[ptr1] < arr2[ptr2]:
            ptr1 += 1
        else:
            ptr2 += 1
    return duplicates




# d = {"ОПР": "Резерв",
#      "Резерв": "ОПР"}

d = {"Лист2": "Лист3",
     "Лист3": "Лист2"}

for i in d.keys():

    open_one = pd.read_excel('exl/1_one_ttk.xlsx', skiprows=0, sheet_name=d[i])
    one_data = open_one.iloc[:, 1]

    open_two = pd.read_excel('exl/2_two_ttk.xlsx', skiprows=0, sheet_name=i)
    two_data = open_two.iloc[:, 1]

    # превращаем наши данные в массив numpy
    one_arr = one_data.to_numpy()
    two_arr = two_data.to_numpy()


    result = find_duplicates(one_arr, two_arr)
    print(result)

    data_frame = pd.DataFrame(result)
    excel_file = f'exl/new_xl_{i}.xlsx'
    data_frame.to_excel(excel_file, index=False)



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









# def find_duplicates(arr1, arr2):
#     # Хэш-таблица для подсчета вхождений строк из первого массива
#     hash_table = {}
#     for word in arr1:
#         hash_table[word] = hash_table.get(word, 0) + 1
#
#     duplicates = []
#     # Поиск дубликатов во втором массиве
#     for word in arr2:
#         if word in hash_table and hash_table[word] > 0:
#             duplicates.append(word)
#             hash_table[word] -= 1
#
#     return duplicates
#
# result = find_duplicates(one_arr, two_arr)
# print(result)



# duplicates = np.intersect1d(one_arr, two_arr)
# result = np.concatenate((one, two))
# unique_result = np.unique(result)



# создаем excel файл




end_time = time.time()
execution_time = end_time - start_time
print("Время выполнения:", execution_time, "секунд")