# coding=utf-8
'''
去除xml中重复的项目
'''

from ScriptTools.AutoHandleScript import AutoHandleScript

if __name__ == '__main__':
    target_path = "G:/temp/"

    filePaths = []
    # filePaths.append("D:/workspace_dev/tc.tmc.corporationapi/app/dal/src/main/resources/META-INF/spring/corporation-dal.xml")
    # filePaths.append("D:/workspace_dev/tc.tmc.corporationapi/app/dal/src/main/resources/sqlmap/corporation/corporation-sqlmap-config.xml")
    filePaths.append("D:/workspace_dev/tc.tmc.admin/app/dal/src/main/resources/META-INF/spring/corporation-dal.xml")
    filePaths.append("D:/workspace_dev/tc.tmc.admin/app/dal/src/main/resources/sqlmap/corporation/corporation-sqlmap-config.xml")

    handleScript = AutoHandleScript(filePaths, target_path)
    handleScript.run_script()
