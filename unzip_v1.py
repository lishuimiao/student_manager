import zipfile
import os

to_path = r"/Users/samlee/Documents/南网业务/RPA/zip/"
src_path = r"/Users/samlee/Documents/南网业务/RPA/src_zip/2019-2022年职工食堂打卡记录（机关和下属所有食堂）.zip"


def unzip_file(zip_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        for old_name in zip_ref.infolist():
            try:
                new_name = old_name.filename.encode('cp437').decode('gbk')
                if old_name.filename != new_name:
                    old_name.filename = new_name
                    zip_ref.extract(old_name, to_path)
            except:
                zip_ref.extract(old_name, to_path)
                # zip_ref.extractall(path=to_path)  # 解压到当前目录


def unzip_recursive(zip_path):
    unzip_file(zip_path)
    file_list = os.listdir(to_path)
    for file in file_list:
        file_path = os.path.join(to_path,file)
        if os.path.isdir(file_path):
            file_list = os.listdir(file_path)
            for file in file_list:
                file_path_1 = os.path.join(file_path,file)
                if file.endswith(".zip"):
                    unzip_file(file_path_1)

        elif file.endswith(".zip"):
            unzip_file(file_path)

    # extracted_files = [ f for f in os.listdir(to_path)]zip_path
    # extracted_files = [f.filename for f in zipfile.ZipFile(zip_path).filelist]
    # for extracted_file in extracted_files: #获取总文件数
    #     try:
    #         new_extracted_file = extracted_file.encode('cp437').decode('gbk')
    #         if extracted_file != new_extracted_file:
    #             extracted_file = new_extracted_file
    #             if extracted_file.endswith('.zip'):
    #                 unzip_recursive(extracted_file)
    #     except:
    #         if extracted_file.endswith('.zip'):
    #             unzip_recursive(extracted_file)


unzip_recursive(src_path)