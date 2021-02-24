import xlrd

# 读取文件
data = xlrd.open_workbook("resources/data1.xlsx")

# 是否完成加载 0 的工作表
# data.sheet_loaded(0)

# 卸载 0 的工作表
# data.unload_sheet(0)

# 获取所有工作表
# print(data.sheets())

# 根据名称 或者索引获取 sheet
# print(data.sheet_by_name('Sheet1'))
# print(data.sheet_by_index(0))

# 打印所有 sheet names
# print(data.sheet_names())

# 工作表的数量
print(data.nsheets)
