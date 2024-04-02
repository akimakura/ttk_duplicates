import numpy as np
import pandas as pd

# d = {"ОПР": "Резерв",
#      "Резерв": "ОПР"}

d = {"Лист2": "Лист3",
     "Лист3": "Лист2"}

for i in d.keys():

    open_one = pd.read_excel('exl/1_one_ttk.xlsx', sheet_name=d[i])
    one_data = open_one.iloc[:, 1]

    open_two = pd.read_excel('exl/2_two_ttk.xlsx', sheet_name=i)
    two_data = open_two.iloc[:, 1]

    # превращаем наши данные в массив numpy
    one_arr = one_data.to_numpy()
    two_arr = two_data.to_numpy()

    result = np.intersect1d(one_arr, two_arr)
    print(result)

    # создаем excel файл
    data_frame = pd.DataFrame(result)
    excel_file = f'exl/new_xl_{i}.xlsx'
    data_frame.to_excel(excel_file, index=False)
