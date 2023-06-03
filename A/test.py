# import os
#
# # 设置重命名标识：如果为1则添加指定字符，flag取值为2则删除指定字符
# flag = 1
#
# # 获取指定目录
# dir_name = './'
#
# # 获取指定目录的文件列表
# file_list = os.listdir(dir_name)
# # print(file_list)
#
#
# # 遍历文件列表内的文件
# for name in file_list:
#
#     # 添加指定字符
#     if flag == 1:
#         new_name = 'Python-' + name
#     # 删除指定字符
#     elif flag == 2:
#         num = len('Python-')
#         new_name = name[num:]
#
#     # 打印新文件名，测试程序正确性
#     print(new_name)
#
#     # 重命名
#     os.rename(dir_name + name, dir_name + new_name)

import xlwings as xw
excel = xw.App()
#excel.visible = True
# excel.visible = False
wb = excel.books.open(r'/Users/samlee/Documents/程序测试文件夹/月表.xlsx')
# wb.save(r'/Users/samlee/Documents/程序测试文件夹/重要数据.xls')
# ws = wb.sheets.add()
# ws.name = '工作表'
# ws.clear
# ws = wb.sheets.add()
# ws.name = '工作表'
ws = wb.sheets['Sheet1']
# ws.name = '第一章'
# r = ws.range('A1')
# r.value = 'nimei'
x = [24,'男的',26,27,28]
r = ws.range('B2')
r.value = x
r.value = [[3,5,7],[2,4,6],[1,2,3]]
r.value
print(r)