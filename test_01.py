import os
import pandas as pd
import shutil
import operator
import logging as lg




def log(path):
    # 此处进行Logging.basicConfig() 设置，后面设置无效
    lg.basicConfig(filename=path,
                   format='%(asctime)s - %(name)s - %(levelname)s - %(message)s-%(funcName)s',
                   level=lg.INFO)
    lg.info('日志初始化')

def get_files(path):
    '''获取文件列表'''

    if not os.path.exists(path + r'\所有Excel文件'):
        '''判断是否存在'''
        os.makedirs(path + r'\所有Excel文件')
    for home, dirs, files in os.walk(path):
        '''获取目标路径下的所有文件和子文件夹'''
        for file in files:
            if (file.endswith(".xlsx") or file.endswith(".xls")) and not os.path.exists(path + '\\所有Excel文件\\' + file):
                '''获取Excel文件'''
                # 拼接路径
                # file_list.append(os.path.join(home, file))
                # print(os.path.join(home, file))
                # 移动文件
                # /home/file
                shutil.move(os.path.join(home, file), path + r'\所有Excel文件')
                # list file
    files = os.listdir(path + r'\所有Excel文件')
    return files


def merge_data(files, merge_excel_path, header_position):
    '''合并Excel数据'''
    # 创建空表接受数据
    frames_17 = []
    frames_9 = []
    frames = []
    # 总行数
    rows_total = 0
    # 计数器
    idenx = 0
    # 表头
    header = []
    # 循环读取数据，并累计到frames
    for file in files:
        idenx += 1
        # df = pd.read_excel(os.path.join(path+"\\"+file))
        dt_sheets = pd.read_excel(path + "\\" + file, sheet_name=None)
        for a in dt_sheets.keys():
            if idenx == 1:
                '''获取第一个Excel的第一个sheet的表头'''
                header = list(dt_sheets[a].loc[header_position])
            elif operator.eq(header, list(dt_sheets[a].loc[header_position])):
                '''判断是否是同一个模版的数据表'''
                rows, columns = dt_sheets[a].shape
                print(f"{file}--行数：({rows},{columns})")
                frames.append(dt_sheets[a])
            else:
                '''将不是一个格式的数据表，写入到新Excel文件待下次处理'''
                pass

            # 按不同模版合并数据
            if columns == 17:
                frames_17.append(dt_sheets[a])
            elif columns == 9:
                frames_9.append(dt_sheets[a])

            # 累计总行数用于验证
            rows_total += rows
    print(f"合并之后的总行数：{rows_total}")
    # 合并数据
    if len(frames_17) > 0:
        result_17 = pd.concat(frames_17)
    if len(frames_9) > 0:
        result_9 = pd.concat(frames_9)
    # print(result)
    # 写入到Excel
    if merge_excel_path:
        writer = pd.ExcelWriter(merge_excel_path)
        if len(frames_17) > 0:
            result_17.to_excel(writer, 'sheet1', index=False)
        if len(frames_9) > 0:
            result_9.to_excel(writer, 'sheet2', index=False)
        writer.close()


path = r"/Users/samlee/Documents/程序测试文件夹/周表.xlsx"
merge_excel_path = r"/Users/samlee/Documents/程序测试文件夹/周表.xlsx"
merge_data(get_files(path), merge_excel_path, 0)
# get_files(path)