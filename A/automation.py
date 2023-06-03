
import os
import pandas as pd


# 定义要合并的Excel文件所在的根文件夹路径
root_folder_path = "/Users/samlee/Documents/程序测试文件夹/2019-2022年广东电网有限责任公司广州白云供电局食堂打卡记录_副本"

# 定义要保存的合并后的Excel文件名
merged_file_name = "merged.xlsx"

# 定义每次读取的行数
# chunk_size = 10000

# 定义一个空的DataFrame，用于存储合并后的数据
merged_data = pd.DataFrame()


# 定义一个函数，用于递归查询指定文件夹下的所有Excel文件
def find_excel_files(folder_path):
    global merged_data
    # 获取文件夹中所有的文件和子文件夹
    files_and_folders = os.listdir(folder_path)
    # 遍历所有的文件和子文件夹
    for item in files_and_folders:
        item_path = os.path.join(folder_path, item)
        # 如果是文件夹，递归查询该文件夹下的Excel文件
        if os.path.isdir(item_path):
            find_excel_files(item_path)
        # 如果是Excel文件，将其读取并添加到合并后的DataFrame中
        elif item.endswith(".xls"):
            data = pd.read_excel(item_path, engine="openpyxl")
            merged_data = pd.concat([merged_data, data])

            # for chunk in pd.read_excel(item_path, chunksize=20000):
            #     merged_data = pd.concat([merged_data, chunk])


# 调用函数，递归查询所有的Excel文件
find_excel_files(root_folder_path)

# 将合并后的数据保存到一个新的Excel文件中
merged_data.to_excel(os.path.join(root_folder_path, merged_file_name), index=False)