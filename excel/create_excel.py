import xlsxwriter

class CreateExcelFile:
    def __init__(self, filename):
        self.filename = filename
        self.worksheetname = 'Busca da página {}'
    
    def create_file(self, data, page=1):
        workbook = xlsxwriter.Workbook(self.filename) 
        worksheet = workbook.add_worksheet(self.worksheetname.format(page))

        bold = workbook.add_format({'bold': True})

        worksheet.set_column(0, 0, 108)
        worksheet.set_column(1, 1, 14)

        worksheet.write('A1', 'Nome Produto', bold) 
        worksheet.write('B1', 'Preço', bold)

        row = 1
        col = 0

        for name, price in data: 
            worksheet.write(row, col, name) 
            worksheet.write(row, col + 1, price) 
            row += 1
        
        workbook.close()