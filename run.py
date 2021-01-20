from iphone.search_iphone import SearchIphone
from excel.create_excel import CreateExcelFile

if __name__ == '__main__':
    page = 1
    filename = 'iPhone_Produtos_pagina_{}.xlsx'
    search = SearchIphone()
    iphones = search.get(page)
    if iphones is not None:
        excel = CreateExcelFile(filename.format(page))
        excel.create_file(iphones, page)
        print('Arquivo "{}" criado com sucesso.'.format(filename.format(page)))
    else:
        print('Não foi possível criar o arquivo.')