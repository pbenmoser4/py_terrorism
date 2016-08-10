import xlrd

def clean():
    print('cleaning')

def clean_excel(filepath, write_file='src/terrorism.csv', delimiter='\t', newline='\n'):
    """
    Clean the global terrorism database file and convert it into a csv

    @param filepath {String} - The path to the global database xlsx file
    @param write_file {String} - Path to the .csv output file
    @param delimiter {String} - Delimiter for the csv output file
    @param newline {String} - Newline string to use for csv output file
    """
    book = xlrd.open_workbook(filepath)
    sheet = book.sheet_by_index(0)

    f = open(write_file, 'a')

    for row in range(sheet.nrows):
        for column in range(sheet.ncols):
            f.write(str(sheet.cell_value(row, column)))
            if column < sheet.ncols - 1:
                f.write(delimiter)
        f.write(newline)
