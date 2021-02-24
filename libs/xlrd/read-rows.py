import xlrd

# 列操作

data = xlrd.open_workbook('resources/data1.xlsx')

sheet = data.sheet_by_index(0)

# 查看行数
print(sheet.nrows)

# 查看第一行
print(sheet.row(0))
# 第一行的 类型
print(sheet.row_types(1))




