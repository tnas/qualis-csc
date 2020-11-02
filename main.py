import pandas


def read_excel_qualis():
    excel_qualis = pandas.read_excel('data/qualis.xlsx', sheet_name='Qualis2019')
    for row in excel_qualis.index:
        print(excel_qualis['SIGLA'][row])


if __name__ == '__main__':
    read_excel_qualis()
