import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import time
import csv
import xlrd

import util.clean as clean

terror_path = 'src/globalterrorismdb_0616dist.xlsx'

# def clean_data(file):
#     with open('src/terrorism-100.csv') as _file:
#         reader = csv.reader(_file)
#         for row in reader:
#             print(row)

# book = xlrd.open_workbook('src/globalterrorismdb_0616dist.xlsx')
# sheet = book.sheet_by_index(0)

# f = open('src/tab.txt', 'a')

# for row in range(sheet.nrows):
#     for column in range(sheet.ncols):
#         # looping through every row and column
#         f.write(str(sheet.cell_value(row, column)))
#         if column < sheet.ncols - 1:
#             f.write('\t')
#     f.write('\n')

# clean.clean()


if __name__ == "__main__":
    print ('executing __main__')
    clean.clean_excel(terror_path)
