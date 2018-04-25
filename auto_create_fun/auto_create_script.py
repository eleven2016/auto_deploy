import xml.dom.minidom
import subprocess

class auto_create_script(object):
    '''
    初始化
    '''

    def __init__(self, **config, **sqls):
        self.gen_path = config.get('gen_path')
        self.target_path = config.get('target_path')
        self.table_name = config.get('table_name')
        self.site_name = config.get('site_name')
        self.module_name = config.get('module_name')
        self.sqls = sqls

    # 执行脚本入口
    def run_script(self):
        print("-----------执行自动脚本---------")
        # 修改配置文件
        self.__update_gen_config_xml()
        # 自动生成dao
        self.__create_table_file()
        # 执行dal脚本,生成类文件
        self.__run_dal_script()
        # 生成service以及Impl和mapper

        # 生成controller和mapper

        # 生成vm页面

        # 生成js文件



    # 修改配置文件
    def __update_gen_config_xml(self):
        print("-----------1.修改配置文件---------")
        gen_config_path = self.gen_path + "/gen_config.xml"
        dom = xml.dom.minidom.parse(gen_config_path)

        root = dom.documentElement

        entries = root.getElementsByTagName('entry')

        for entry in entries:
            attr = entry.getAttribute("key")
            if attr == 'dal_package':
                entry.firstChild.nodeValue = "com.ly.flight.tmc." + self.site_name + ".dal." + self.module_name
            if attr == 'appName':
                entry.firstChild.nodeValue = self.site_name
            if attr == 'appModule':
                entry.firstChild.nodeValue = self.module_name

        config_file = open(gen_config_path, 'w', 1024, 'UTF-8')
        dom.writexml(config_file, addindent='  ', newl='', encoding='utf-8')
        print("-------------修改配置文件结束---------")

    # 创建表文件
    def __create_table_file(self):
        print("--------------2.创建table文件------------------")
        # 根据主键查询的sql
        sql = "select * from " + self.table_name + " where ID = #id#"
        # 创建对应的文件
        table_file_path = self.gen_path + "/tables/" + self.table_name + ".xml"

        dom = xml.dom.minidom.Document()
        root_node = dom.createElement("table")
        root_node.setAttribute("sqlname", self.table_name)

        dom.appendChild(root_node)

        query_node = dom.createElement("operation")
        query_node.setAttribute("name", "getById")
        query_node.setAttribute("paramtype", "primitive")
        query_node.setAttribute("multiplicity", "one")

        sql_node = dom.createElement("sql")
        text_node = dom.createTextNode(sql)
        sql_node.appendChild(text_node)
        query_node.appendChild(sql_node)
        root_node.appendChild(query_node)

        table_file = open(table_file_path, 'w', 1024, 'UTF-8')
        dom.writexml(table_file, addindent='  ', newl='\n', encoding='utf-8')
        print("--------------创建table文件结束------------------")

    # 执行dal脚本
    def __run_dal_script(self):
        cmd_arg = ["gen.bat", "dal", self.table_name]

        sub = subprocess.Popen(cmd_arg, stdout=subprocess.PIPE, shell=True, cwd=self.gen_path)
        out, err = sub.communicate()
        lines = out.splitlines()
        for line in lines[3:len(lines)]:
            print(line)
