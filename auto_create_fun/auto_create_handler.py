from auto_create_fun.auto_create_script import auto_create_script

if __name__ == '__main__':
    # 配置
    config = {
        # gendal脚本的目录
        'gen_path': 'D:/workspace_test/AutoDeploy/auto_create_fun/db',

        # target目录
        'target_path': 'D:/workspace_test/AutoDeploy/auto_create_fun/target',

        # table名称
        'table_name': 'EMPLOYEE',

        # 站点名称
        'site_name': 'test',

        # 子模块名称
        'module_name': 'test'
    }

    # sql
    sqls = {
        'getById': 'select * from  EMPLOYEE where ID = #id#',
        'findByConditions': 'select * from EMPLOYEE ',
        'insert' : 'insert into'
    }

    auto_script = auto_create_script(**config)
    auto_script.run_script()
