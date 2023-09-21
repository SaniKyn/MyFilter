import pandas as pd

df = pd.read_excel('m9.xlsx', sheet_name='Лист1')

list_df = df[['Заголовок чека. Код чека', 'Карточка товара. Название короткое']].values.tolist()


def filter_df(list_df_old):
    code_product_list = []
    result_list = []
    n = 0
    for i in range(len(list_df_old)):
        if list_df_old[i][0] != n:
            for j in range(i, len(list_df_old)):
                if list_df_old[i][0] != list_df_old[j][0]:
                    result_list.append(','.join(code_product_list))
                    code_product_list = []
                    n = list_df_old[i][0]
                    break
                else:
                    new_list = [k.lower() for k in list_df_old[j][1].split()[:2] if k.isupper()]
                    code_product_list.append(' '.join(new_list))
        else:
            continue
    result_list.append(''.join(code_product_list))
    return result_list


new_df = pd.DataFrame(filter_df(list_df))
new_df.to_csv('new_m9.csv', encoding='cp1251', index=False)

# Название короткое
# Код чека
