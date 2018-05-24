from datetime import datetime


def create_service(basic_name, service_path, dao_path):
    print("创建service->"+basic_name)
    service_name = basic_name+"Service"
    service_file = service_path+"/"+service_name+".java"

    service_content = []
    service_impl_content = []

    dao_file = open(dao_path)
    method_content = []
    flag = False
    for line in dao_file.readlines():
        if line.startswith("public interface"):
            flag = True
            continue
        if line.find("}") > -1:
            flag = False
        if flag and not line.startswith("\n"):
            method_content.append(line)

    service_content.append("package com.eleven.manage.platform.service;")
    service_content.append("import com.eleven.manage.platform.dto.*;")
    service_content.append("import java.util.List;")
    service_content.append("/**")
    service_content.append(" * @author ywl")
    service_content.append(" * @date "+datetime.now().strftime("%Y/%m/%d"))
    service_content.append(" **/")
    service_content.append("public interface "+service_name+" {")

    service_impl_content.append("package com.eleven.manage.platform.service.impl;")
    service_impl_content.append("import java.util.List;")
    service_impl_content.append("import org.springframework.beans.factory.annotation.Autowired;")
    service_impl_content.append("import org.springframework.stereotype.Service;")
    service_impl_content.append("import org.springframework.transaction.annotation.Transactional;")
    service_impl_content.append("import com.eleven.manage.platform.dto.*;")
    service_impl_content.append("import com.eleven.manage.platform.mybatis.dao.*;")
    service_impl_content.append("import com.eleven.manage.platform.service." +service_name + ";")
    service_impl_content.append("/**")
    service_impl_content.append(" * @author ywl")
    service_impl_content.append(" * @date " + datetime.now().strftime("%Y/%m/%d"))
    service_impl_content.append(" **/")
    service_impl_content.append("@Service(\"" + service_name[0:1].lower() + service_name[1:] + "\")")
    service_impl_content.append("public class " + service_name + "Impl" + " implements " + service_name+" {")
    service_impl_content.append("@Autowired")
    service_impl_content.append("private " + basic_name + "Dao " + basic_name[0:1].lower() + basic_name[1:] + "Dao;")

    for method in method_content:
        method_str = ""
        if method.find("List") > 0:
            result_do = method[method.find("<")+1:method.find(">")]
            result_dto = result_do.replace("DO", "DTO")
            method_str += "    List<"+result_dto+"> "
            method_name = method[method.find(">")+1:method.find("(")]
            method_str += method_name
            method_str += "("
            params = method[method.find("(") + 1:method.find(")")]
            param_array = params.split(",")
            for param in param_array:
                temp_arr = param.split(" ")
                if temp_arr[0].endswith("DO"):
                    method_str += temp_arr[0].replace("DO", "DTO")
                    method_str += " "+temp_arr[1]+", "
                else:
                    method_str += param + ","

        else:
            method_str += method[0:method.find("(")+1]
            params = method[method.find("(")+1:method.find(")")]
            param_array = params.split(",")
            for param in param_array:
                temp_arr = param.split(" ")
                if temp_arr[0].endswith("DO"):
                    method_str += temp_arr[0].replace("DO", "DTO")
                    method_str += " " + temp_arr[1] + ", "
                else:
                    method_str += param + ","
        print(method_str)
        if method_str.endswith(","):
            service_content.append(method_str[0:len(method_str) - 1] + ");")
        else:
            service_content.append(method_str[0:len(method_str) - 2] + ");")

        service_impl_content.append("@Override")
        if method_str.endswith(","):
            service_impl_content.append("public " + method_str[0:len(method_str) - 1] + "){")
        else:
            service_impl_content.append("public " + method_str[0:len(method_str) - 2] + "){")
        if method_str.find("int")>-1:
            service_impl_content.append("return 0;")
        else:
            service_impl_content.append("return null;")
        service_impl_content.append("}")

    service_content.append("}")
    service_impl_content.append("}")
    write_file = open(service_file, "w")

    for content in service_content:
        write_file.writelines(content)
        write_file.writelines("\n")

    print("创建serviceImpl")
    service_impl_name = service_name + "Impl"
    service_impl_file = service_path + "/impl/" + service_impl_name + ".java"
    service_impl_write_file = open(service_impl_file, "w")
    for content in service_impl_content:
        service_impl_write_file.writelines(content)
        service_impl_write_file.writelines("\n")

def create_controller(basic_name, controller_path):
    print("创建controller")


if __name__ == '__main__':

    dao_paths = []
    dao_paths.append("D:/workspace_idea/LongManagePlatform/src/main/java/com/eleven/manage/platform/mybatis/dao/MenuDao.java")
    dao_paths.append("D:/workspace_idea/LongManagePlatform/src/main/java/com/eleven/manage/platform/mybatis/dao/RoleDao.java")
    dao_paths.append("D:/workspace_idea/LongManagePlatform/src/main/java/com/eleven/manage/platform/mybatis/dao/PermissionDao.java")

    service_path = "D:/workspace_idea/LongManagePlatform/src/main/java/com/eleven/manage/platform/service"
    controller_path = "D:/workspace_idea/LongManagePlatform/src/main/java/com/eleven/manage/platform/web"

    for dao_path in dao_paths:
        dao_name_array = dao_path.split("/")
        dao_name = dao_name_array[len(dao_name_array)-1]
        basic_name = dao_name[:-8]
        create_service(basic_name, service_path, dao_path)
        create_controller(basic_name, controller_path)
        print("创建完毕")