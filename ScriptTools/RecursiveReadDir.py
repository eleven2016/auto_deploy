import os


def find_java_file(dir_path, target_dicts):
    for dir_temp in os.listdir(dir_path):
        file_temp = os.path.join(dir_path, dir_temp)
        if os.path.isdir(file_temp):
            # 如果是目录,递归查询
            find_java_file(file_temp, target_dicts)
        if os.path.isfile(file_temp) and file_temp.endswith(".java") and file_temp != "package-info.java":
            file_name = os.path.basename(file_temp)
            target_dicts[file_name] = file_temp


def read_java_file_content(java_file_path, file_document):

    java_file = open(java_file_path)

    filter_black_space = []
    # 去掉空行
    for line in java_file.readlines():
        if line.startswith("\n") or len(line) == 3:
            continue
        filter_black_space.append(line)

    # 去掉@param
    filter_param_content = []
    param_flag = False
    for line in filter_black_space:
        if line.find("@author") > -1 or line.find("@param") > -1 or line.find("@return") > -1 or line.find("@throws") > -1 or line.find("@see") > -1:
            param_flag = True
            continue
        elif param_flag and line.endswith("*/\n"):
            param_flag = False
            filter_param_content.append(line)
        elif param_flag:
            continue
        else:
            filter_param_content.append(line)

    # 过滤licence说明
    filter_license_content = []
    licence_flag = False
    for line in filter_param_content:
        if line.startswith(" * Copyright"):
            licence_flag = True
            continue
        elif licence_flag and line.endswith("*/\n"):
            licence_flag = False
            continue
        elif licence_flag:
            continue
        else:
            filter_license_content.append(line)

    for line in filter_license_content:
        # print(line)
        file_document.add_paragraph(line.replace("\n", ""), 'No Spacing')


