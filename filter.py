import pandas as pd

df = pd.read_excel('m8.xlsx', sheet_name='Лист1')
df_product = pd.read_excel('product.xlsx', sheet_name='Sheet1')
list_df = df[['Код чека', 'Название короткое']].values.tolist()
list_product = list(df_product['продукты'])


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
                    for k in list_df_old[j][1].lower().split()[:1]:
                        if k in ['пакет', 'пакеты', 'мешки']:
                            break
                        elif k in list_product:
                            index_product = list_product.index(k)
                            name_product = list_product[index_product]
                            code_product_list.append(name_product)
        else:
            continue
    result_list.append(code_product_list)
    return result_list


new_df = pd.DataFrame(filter_df(list_df))
new_df.to_csv('new_m8.csv', encoding="utf-8-sig", header=False, index=False)
