import zipfile
import os


to_path = r"/Users/samlee/Documents/南网业务/RPA/zip/"
src_path = r"/Users/samlee/Documents/南网业务/RPA/2019-2022年职工食堂打卡记录（机关和下属所有食堂）.zip"
def unzip_file(zip_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        for old_name in zip_ref.infolist():
            try:
                new_name = old_name.filename.encode('cp437').decode('gbk')
                if old_name.filename != new_name:
                    old_name.filename = new_name
                    zip_ref.extract(old_name,to_path) 
            except:
                
        # zip_ref.extractall(path=to_path)  # 解压到当前目录

def unzip_recursive(zip_path):
    unzip_file(zip_path)
    # extracted_files = [ f for f in os.listdir(to_path)]zip_path
    extracted_files = [f.filename for f in zipfile.ZipFile(zip_path).filelist]
    for extracted_file in extracted_files:
        if extracted_file.endswith('.zip'):
            unzip_recursive(extracted_file)
                    
unzip_recursive(src_path)

# import os
# import zipfile

# zip_path = '/Users/samlee/Documents/南网业务/RPA/2019-2022年职工食堂打卡记录（机关和下属所有食堂）.zip'
# output_dir= '/Users/samlee/Documents/南网业务/RPA/zip'


# def unzip_file(zip_path, output_dir):
#     with zipfile.ZipFile(zip_path, 'r') as zip_ref:
#         for info in zip_ref.infolist():
#             filename = info.filename.encode('cp437').decode('gbk')  # 先转换编码再解压
#             output_path = os.path.join(output_dir, filename)
#             if info.is_dir():
#                 os.makedirs(output_path, exist_ok=True)
#             else:
#                 os.makedirs(os.path.dirname(output_path), exist_ok=True) #返回目录名
#                 with open(output_path, 'wb') as f:
#                     f.write(zip_ref.read(info.filename))
                    
#                     # 如果解压后是zip文件，则递归解压缩
#                     if filename.endswith('.zip'):
#                         unzip_file(output_path, output_dir)

# unzip_file(zip_path, output_dir)

import os
import zipfile

zip_path = r"/Users/samlee/Documents/南网业务/RPA/src_zip/2019-2022年职工食堂打卡记录（机关和下属所有食堂）"
#zip_path = r"/Users/samlee/Documents/南网业务/RPA/src_zip/2019-2022年职工食堂打卡记录（机关和下属所有食堂）/2019-2022年广东电网有限责任公司广州黄埔供电局食堂打卡记录"

to_path = r"/Users/samlee/Documents/南网业务/RPA/zip/"

def un_zip(zip_path):
    """遇到一批压缩包有的路径有中文，有的没中文，就出现中文路径ok，非中文不行情况。需要先手动把一层解压缩

    Args:
        zip_path (_type_): _description_
    """
    file_list = os.listdir(zip_path)
    for item in file_list:
        item_path = os.path.join(zip_path, item)
        if os.path.isdir(item_path):
            un_zip(item_path)
        elif item.endswith(".zip"):
             with zipfile.ZipFile(item_path, 'r') as zip_ref:
                 for old_name in zip_ref.infolist():
                    #  zip_ref.extract(old_name,to_path)
                    try:
                        new_name = old_name.filename.encode('cp437').decode('gbk')
                    except:
                        new_name = old_name.filename.encode('gbk').decode('cp437')
                    if old_name.filename != new_name:
                        old_name.filename = new_name
                        zip_ref.extract(old_name,to_path)   
                #  zip_ref.extractall(path=to_path)  # 解压到当前目录


un_zip(zip_path)

# 以下疑似可以解压中文路径,只解压缩了第一层

# import zipfile
# import os

# filename = r"//Users/samlee/Documents/南网业务/RPA/src_zip/2019-2022年职工食堂打卡记录（机关和下属所有食堂）.zip"
# output_dir = r"/Users/samlee/Documents/南网业务/RPA/zip/"

# def unpack_zipfile(filename, output_dir):
#     with zipfile.ZipFile(filename, 'r') as zip_ref:
#         for info in zip_ref.infolist():
#             name = info.filename.encode('cp437').decode('gbk')
#             path = os.path.join(output_dir,name)
#             if name.endswith('/'):
#                 os.makedirs(path, exist_ok=True)
#             else:
#                 os.makedirs(os.path.dirname(path), exist_ok=True)
#                 with open(path, 'wb') as f:
#                     f.write(zip_ref.read(info))                
# unpack_zipfile(filename,output_dir) 



# import zipfile
# import os

# filename = r"/Users/samlee/Documents/南网业务/RPA/src_zip/2019-2022年职工食堂打卡记录（机关和下属所有食堂）.zip"
# output_dir = r"/Users/samlee/Documents/南网业务/RPA/zip/"

# def unpack_zipfile(filename, output_dir):
#     with zipfile.ZipFile(filename, 'r') as zip_ref:
#         for info in zip_ref.infolist():
#             name = info.filename.encode('cp437').decode('gbk')
#             path = os.path.join(output_dir, name)
#             if name.endswith('/'):
#                 os.makedirs(path, exist_ok=True)
#             else:
#                 os.makedirs(os.path.dirname(path), exist_ok=True)
#                 if name.endswith('.zip'):
#                     unpack_zipfile(os.path.join(output_dir, name), os.path.splitext(path)[0])
#                 else:
#                     with open(path, 'wb') as f:
#                         f.write(zip_ref.read(info))
                        
                        
# unpack_zipfile(filename,output_dir) 