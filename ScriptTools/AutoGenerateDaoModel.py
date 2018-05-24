'''
自动生成dao和model层
'''
import xml.dom.minidom
from datetime import datetime
import os

###创建model
def createModel(model_name,attribute_list,model_path,model_package):
    print("----------------创建实体类--------------")
    content = []
    package_name = model_package[0:model_package.find(model_name)-1]
    content.append("package "+package_name+";")
    content.append("\n")
    content.append("\n")
    content.append("import lombok.Data;")
    content.append("\n")
    content.append("/**")
    content.append("\n")
    content.append(" * @author ywl")
    content.append("\n")
    content.append(" * @date "+datetime.now().strftime("%Y/%m/%d"))
    content.append("\n")
    content.append(" */")
    content.append("\n")
    content.append("@Data")
    content.append("\n")
    content.append("public class "+model_name+"{")
    content.append("\n")

    for attr in attribute_list.keys():
        content.append("    private "+attribute_list[attr]+" "+attr+";")
        content.append("\n")
        content.append("\n")

    content.append("}")

    writeFile = open(model_path+"/"+model_name+".java", "w")

    for line in content:
        writeFile.writelines(line)

    print("创建model结束-->"+model_name)


###创建DTO
def createDTO(model_name,attribute_list,model_path,model_package):
    print("----------------创建DTO--------------")
    content = []
    package_name = model_package[0:model_package.find(model_name)-1]
    content.append("package com.eleven.manage.platform.dto;")
    content.append("\n")
    content.append("\n")
    content.append("import lombok.Data;")
    content.append("\n")
    content.append("/**")
    content.append("\n")
    content.append(" * @author ywl")
    content.append("\n")
    content.append(" * @date "+datetime.now().strftime("%Y/%m/%d"))
    content.append("\n")
    content.append(" */")
    content.append("\n")
    content.append("@Data")
    content.append("\n")
    content.append("public class "+model_name+"{")
    content.append("\n")

    for attr in attribute_list.keys():
        content.append("    private "+attribute_list[attr]+" "+attr+";")
        content.append("\n")
        content.append("\n")

    content.append("}")

    writeFile = open(model_path+"/"+model_name+".java", "w")

    for line in content:
        writeFile.writelines(line)

    print("创建DOT结束-->"+model_name)


##创建方法
def createDao(collection,dao_path,model_name,model_package):
    print("----------------创建接口方法--------------")
    dao_name_array = collection.getAttribute("namespace").split(".")
    dao_name = dao_name_array[len(dao_name_array) - 1]
    print("获得dao的名称:" + dao_name)

    dao_package = collection.getAttribute("namespace")[0:collection.getAttribute("namespace").find(dao_name)-1]
    print("创建dao-->" + dao_package)

    content = []
    content.append("package " + dao_package + ";")
    content.append("\n")
    content.append("\n")
    content.append("import "+model_package[0:model_package.find(model_name)-1]+".*;")
    content.append("\n")
    content.append("import org.springframework.stereotype.Service;")
    content.append("\n")
    content.append("import java.util.List;")
    content.append("\n")
    content.append("/**")
    content.append("\n")
    content.append(" * @author ywl")
    content.append("\n")
    content.append(" * @date " + datetime.now().strftime("%Y/%m/%d"))
    content.append("\n")
    content.append(" */")
    content.append("\n")
    dao_name_temp = dao_name[0:1].lower()+dao_name[1:]
    content.append("@Service(\""+dao_name_temp+"\")")
    content.append("\n")
    content.append("public interface " + dao_name + "{")
    content.append("\n")


    ##根据不同的方法生成不同的内容
    delete_elements = collection.getElementsByTagName("delete")
    for delete_element in delete_elements:
        id = delete_element.getAttribute("id")
        parameter = delete_element.getAttribute("parameterType")
        content.append("    int " + id + " ("+parameter+" id);")
        content.append("\n")
        content.append("\n")

    update_elements = collection.getElementsByTagName("update")
    for update_element in update_elements:
        id = update_element.getAttribute("id")
        parameter = update_element.getAttribute("parameterType")
        parameter_arr = parameter.split(".")
        parameter_temp = parameter_arr[len(parameter_arr)-1]
        content.append("    int " + id + " (" + parameter_temp + " param);")
        content.append("\n")
        content.append("\n")

    insert_elements = collection.getElementsByTagName("insert")
    for insert_element in insert_elements:
        id = insert_element.getAttribute("id")
        parameter = insert_element.getAttribute("parameterType")
        parameter_arr = parameter.split(".")
        parameter_temp = parameter_arr[len(parameter_arr) - 1]
        content.append("    int " + id + " (" + parameter_temp + " param);")
        content.append("\n")
        content.append("\n")

    select_elements = collection.getElementsByTagName("select")
    for select_element in select_elements:
        id = select_element.getAttribute("id")
        parameter = select_element.getAttribute("parameterType")
        parameter_arr = parameter.split(".")
        parameter_temp = parameter_arr[len(parameter_arr) - 1]
        content.append("    List<"+parameter_temp+"> " + id + "(" + parameter_temp + " param);")
        content.append("\n")
        content.append("\n")

    content.append("}")

    writeFile = open(dao_path + "/" + dao_name + ".java", "w")

    for line in content:
        writeFile.writelines(line)



if __name__ == '__main__':

    '''
    1.mapper文件手动编写
    2.根据mapper文件生成相应的dao和model
    '''

    mappers_path = []
    dto_path = "D:/workspace_idea/LongManagePlatform/src/main/java/com/eleven/manage/platform/dto"
    dao_path = "D:/workspace_idea/LongManagePlatform/src/main/java/com/eleven/manage/platform/mybatis/dao"
    model_path = "D:/workspace_idea/LongManagePlatform/src/main/java/com/eleven/manage/platform/mybatis/model"


    # mappers_path.append("D:/workspace_idea/LongManagePlatform/src/main/resources/mybatis-mapper/UserMapper.xml")
    # mappers_path.append("D:/workspace_idea/LongManagePlatform/src/main/resources/mybatis-mapper/MenuMapper.xml")
    # mappers_path.append("D:/workspace_idea/LongManagePlatform/src/main/resources/mybatis-mapper/PermissionMapper.xml")
    # mappers_path.append("D:/workspace_idea/LongManagePlatform/src/main/resources/mybatis-mapper/PermissionMenuMapper.xml")
    mappers_path.append("D:/workspace_idea/LongManagePlatform/src/main/resources/mybatis-mapper/RoleMapper.xml")
    mappers_path.append("D:/workspace_idea/LongManagePlatform/src/main/resources/mybatis-mapper/RolePermissionMapper.xml")
    mappers_path.append("D:/workspace_idea/LongManagePlatform/src/main/resources/mybatis-mapper/UserRoleMapper.xml")

    ##读取mapper
    for mapper_path in mappers_path:
        DOMTree = xml.dom.minidom.parse(mapper_path)
        collection = DOMTree.documentElement
        result_map_element = collection.getElementsByTagName("resultMap")

        result_map_element_type = result_map_element[0].getAttribute("type")
        print("获得model的路径:" + result_map_element_type)

        model_name_array = result_map_element_type.split(".")
        model_name = model_name_array[len(model_name_array)-1]
        print("获得model的名称:"+model_name)

        result_elements = result_map_element[0].getElementsByTagName("result")
        attribute_list = {}

        for element in result_elements:
            attribute = element.getAttribute("property")
            java_type = element.getAttribute("javaType")
            attribute_list[attribute] = java_type
        print("获得model的所有属性:"+attribute_list.__str__())

        createModel(model_name, attribute_list, model_path, result_map_element_type)
        createDTO(model_name.replace("DO", "DTO"), attribute_list, dto_path, result_map_element_type)
        createDao(collection, dao_path, model_name, result_map_element_type)
