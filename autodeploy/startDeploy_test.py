'''
Created on 2017年6月22日

@author: ywl48338
'''
from autodeploy.AutoDeployment import AutoDeployment

if __name__ == '__main__':

    environment = "test"
    #projectPaths=["D:\\workspace_dev\\tc.tmc.admin"]
    # projectPaths=["D:\\workspace_dev\\tc.tmc.corporationapi","D:\\workspace_dev\\tc.tmc.flightwebapi","D:\\workspace_dev\\tc.tmc.corporationwebapi"]
    #projectPaths=["D:\\workspace_dev\\tc.tmc.corporationapi"]
    # projectPaths=["D:\\workspace_dev\\tc.tmc.admin","D:\\workspace_dev\\tc.tmc.corporationapi"]
    # projectPaths=["D:\\workspace_dev\\tc.tmc.flightwebapi","D:\\workspace_dev\\tc.tmc.corporationapi"]
    # projectPaths=["D:\\workspace_dev\\tc.tmc.platform"]
    # projectPaths=["D:\\workspace\\changedateweb"]
    
    #projectPaths = ["D:\\workspace_dev\\tc.tmc.manualitemsapi", "D:\\workspace_dev\\tmcopplatform"]
    #projectPaths = ["D:\\workspace_dev\\tc.tmc.manualitemsapi"]
    #projectPaths = ["D:\\workspace_dev\\tmcopplatform"]
    
    
    #projectPaths = ["D:\\workspace_dev\\tc.tmc.corp.coreinterfaceapi"]
    #projectPaths = ["D:\\workspace_dev\\tc.tmc.corporationapi","D:\\workspace_dev\\tc.tmc.corporationwebapi"]
    #projectPaths = ["D:\\workspace_dev\\tc.tmc.corporationwebapi"]
    #projectPaths = ["D:\\workspace_dev\\tc.tmc.corp.coreinterfaceapi","D:\\workspace_dev\\tc.tmc.corporationwebapi"]

    #projectPaths=["D:\\workspace_dev\\tc.tmc.oaapi"]

    #projectPaths = ["D:\\workspace_dev\\interflightorderapi","D:\\workspace_dev\\tmcopplatform"]
    
    tomcatPath = "D:\\apache-tomcat-8.0.44"
    autoDep = AutoDeployment(projectPaths, tomcatPath, environment)
    autoDep.autoDeploy()
