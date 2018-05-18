'''
Created on 2017年6月22日

@author: ywl48338
'''
from autodeploy.AutoDeployment import AutoDeployment

if __name__ == '__main__':
    environment = "dev"
    projectPaths = []
    '''admin'''
    # projectPaths.append("D:\\workspace_dev\\tc.tmc.admin")
    # projectPaths.append("D:\\workspace_dev\\tc.tmc.admin")
    '''
    
    呼叫中心
    '''
    # projectPaths = ["D:\\workspace_dev\\tc.tmc.callcenterapi"]
    '''
    权限
    '''
    # projectPaths = ["D:\\workspace_dev\\tc.tmc.permission"]

    '''
    服务费
    '''
    # projectPaths.append("D:\\workspace_dev\\tc.tmc.corporationapi")
    # projectPaths.append("D:\\workspace_dev\\tc.tmc.charge")

    # projectPaths=["D:\\workspace_dev\\tc.tmc.corporationapi","D:\\workspace_dev\\tc.tmc.flightwebapi","D:\\workspace_dev\\tc.tmc.corporationwebapi"]
    # projectPaths = ["D:\\workspace_dev\\tc.tmc.corporationapi"]
    # projectPaths=["D:\\workspace_dev\\tc.tmc.admin","D:\\workspace_dev\\tc.tmc.corporationapi"]
    # projectPaths=["D:\\workspace_dev\\tc.tmc.flightwebapi","D:\\workspace_dev\\tc.tmc.corporationapi"]
    # projectPaths=["D:\\workspace_dev\\tc.tmc.platform"]
    # projectPaths=["D:\\workspace\\changedateweb"]

    # projectPaths = ["D:\\workspace_dev\\tc.tmc.manualitemsapi", "D:\\workspace_dev\\tmcopplatform"]
    # projectPaths = ["D:\\workspace_dev\\tc.tmc.manualitemsapi"]
    # projectPaths.append("D:\\workspace_dev\\tmcopplatform")

    # projectPaths.append("D:\\workspace_dev\\tc.tmc.corp.coreinterfaceapi")
    projectPaths.append("D:\\workspace_dev\\tc.tmc.corporationapi")
    projectPaths.append("D:\\workspace_dev\\tc.tmc.oaapi")
    projectPaths.append("D:\\workspace_dev\\tc.tmc.corporationwebapi")
    # projectPaths.append("D:\\workspace_dev\\tc.tmc.corporationwebapi")
    # projectPaths.append("D:\\workspace_dev\\tc.tmc.corp.coreinterfaceapi","D:\\workspace_dev\\tc.tmc.corporationwebapi")



    # projectPaths.append("D:\\workspace_dev\\interflightorderapi","D:\\workspace_dev\\tmcopplatform")
    '''财务'''
    # projectPaths.append("D:\workspace_dev\\dsf.flight.tmc.refundapi")

    tomcatPath = "D:\\apache-tomcat-8.0.44"
    autoDep = AutoDeployment(projectPaths, tomcatPath, environment)
    autoDep.autoDeploy()
