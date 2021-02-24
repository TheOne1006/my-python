import xlrd

# cell操作

data = xlrd.open_workbook('resources/data1.xlsx')

sheet = data.sheet_by_index(0)


# 查看第一行 第一列
print(sheet.cell(0, 0))
# 第一行的 类型
print(sheet.cell_type(1, 1))

