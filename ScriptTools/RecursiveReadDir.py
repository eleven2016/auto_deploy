import os
import docx.shared as Shared


def find_java_file(dir_path, target_dicts):

    file_list = []
    dir_list = []

    for dir_temp in os.listdir(dir_path):
        file_temp = os.path.join(dir_path, dir_temp)
        if os.path.isdir(file_temp):
            dir_list.append(file_temp)
        if os.path.isfile(file_temp) and file_temp.endswith(".java") and not file_temp.endswith("package-info.java"):
            file_list.append(file_temp)
    # 优先处理文件
    for file_temp in file_list:
        file_name = os.path.basename(file_temp)
        target_dicts[file_name] = file_temp

    # 其次处理目录
    for dir_temp in dir_list:
        find_java_file(dir_temp, target_dicts)


def read_java_file_content(java_file_path, file_document):

    java_file = open(java_file_path)

    filter_black_space = []
    # 去掉空行
    for line in java_file.readlines():
        if line.startswith("\n") or len(line) == 3 or line.find("@SuppressWarnings") > -1:
            continue
        filter_black_space.append(line)

    # 去掉@param
    filter_param_content = []
    param_flag = False
    for line in filter_black_space:
        if line.find("@author") > -1 or line.find("@param") > -1 or line.find("@return") > -1 or line.find("@throws") > -1 or line.find("@see") > -1 or line.find("@link") > -1:
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

    # 过滤掉html元素
    filter_html_content = []
    html_flag = False
    for line in filter_license_content:
        if line.find("* <pre") > -1:
            html_flag = True
            continue
        elif html_flag and line.endswith("</pre>\n"):
            html_flag = False
            continue
        elif html_flag:
            continue
        else:
            filter_html_content.append(line)

    # 过滤掉import
    filter_import_content = []
    for line in filter_html_content:
        if line.startswith("import") or line.startswith("package "):
            continue
        filter_import_content.append(line)

    # 数据写入
    for line in filter_import_content:
        paragraph = file_document.add_paragraph()
        paragraph.style = 'No Spacing'
        run = paragraph.add_run()
        run.text = line.replace("\n", "")
        # run.style = 'No Spacing'
        run.font.size = Shared.Mm(2.5)


