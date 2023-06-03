import os
import zipfile

zip_path = r"/Users/samlee/Documents/南网业务/RPA/2019-2022年职工食堂打卡记录（机关和下属所有食堂）"
to_path = r"/Users/samlee/Documents/南网业务/RPA/zip"

# 当解压之后判断是个压缩文件，进行递归时继续返回使用os.listdir(zip_path)不妥当，应该直接解压掉zip，

def unzip(zip_path):
    """递归解压zip文件"""
    file_list = os.listdir(zip_path)
    #  列出目录文件为列表
    for file in file_list:
        file_path = os.path.join(zip_path, file)
        # 拼接完整路径
        if os.path.isdir(file_path):
            unzip(file_path)

        elif file.endswith(".zip"):
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                for old_name in zip_ref.infolist():
                    try:
                        new_name = old_name.filename.encode('cp437').decode(
                            'gbk')
                        if old_name.filename != new_name:
                            old_name.filename = new_name

                        extracted_path = zip_ref.extract(old_name, to_path)

                        if zipfile.is_zipfile(extracted_path):  # 如果解压后的文件还是一个压缩文件，继续递归解压,下面先写死后面再考虑递归
                            with zipfile.ZipFile(extracted_path, 'r') as n_zip_ref:
                                for o_name in n_zip_ref.infolist():
                                    try:
                                        n_name = o_name.filename.encode('cp437').decode('gbk')
                                        if o_name.filename != n_name:
                                            o_name.filename = n_name
                                        target_path = n_zip_ref.extract(o_name, os.path.dirname(extracted_path))
                                    except:
                                        zip_ref.extract(o_name, os.path.dirname(extracted_path))
                    except:

                        extracted_path = zip_ref.extract(old_name, to_path)
                        if zipfile.is_zipfile(extracted_path):  # 如果解压后的文件还是一个压缩文件，继续解压
                            with zipfile.ZipFile(extracted_path, 'r') as n_zip_ref:
                                for o_name in n_zip_ref.infolist():
                                    n_zip_ref.extract(o_name, to_path)



if __name__ == '__main__':
    unzip(zip_path)