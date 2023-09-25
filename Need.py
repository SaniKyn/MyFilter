import pandas as pd

df = pd.read_excel('m2.xlsx', sheet_name='Лист1')
list_df = df[['Код чека', 'Название короткое']].values.tolist()


def filter_df(list_df_old):
    code_product_list, result_list = [], []
    n = 0
    for i in range(len(list_df_old)):
        if list_df_old[i][0] != n:
            for j in range(i, len(list_df_old)):
                if list_df_old[i][0] != list_df_old[j][0]:
                    result_list.append(code_product_list)
                    code_product_list = []
                    n = list_df_old[i][0]
                    break
                else:
                    for k in list_df_old[j][1].split()[:1]:
                        if k.isupper() or (k in ['Форель', 'Скумбрия']):
                            code_product_list.append(k.lower())

        else:
            continue
    result_list.append(code_product_list)
    return result_list


new_df = pd.DataFrame(filter_df(list_df))
new_df.to_csv('new_m2.csv', encoding='1251', header=False, index=False)
