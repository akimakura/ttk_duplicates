import numpy as np
import pandas as pd

d = {"Резерв": "ОПР",
     "ОПР": "Резерв"}

# d = {"Лист2": "Лист3",
#      "Лист3": "Лист2"}

all_results = []

for i in d.keys():

    open_one = pd.read_excel('exl/Проба 1.xls', engine='xlrd', sheet_name=d[i])
    one_data = open_one.iloc[:, 4]
    open_two = pd.read_excel('exl/Проба 2.xls', engine='xlrd', sheet_name=i)
    two_data = open_two.iloc[:, 4]

    # превращаем наши данные в массив numpy
    one_arr = one_data.to_numpy()
    two_arr = two_data.to_numpy()

    # меняем тип данных на строковый //тк вылезает float//
    one_arr = one_arr.astype(str)
    two_arr = two_arr.astype(str)

    # находим пересечения в двух массивах
    result = np.intersect1d(one_arr, two_arr)
    print(result)
    all_results.extend(result)


# создаем excel файл
data_frame = pd.DataFrame(all_results, columns=['При одновременных авариях по обоим напрвлениям пострадают заказы:'])
excel_file = 'exl/new_xl.xlsx'
data_frame.to_excel(excel_file, index=False)
