import xlrd

# 行操作

data = xlrd.open_workbook('resources/data1.xlsx')

sheet = data.sheet_by_index(0)

# 查看列
print(sheet.ncols)

# 查看第一列
print(sheet.col(0))
# 第一列的 类型
print(sheet.col_types(1))




