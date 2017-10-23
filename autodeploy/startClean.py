'''
Created on 2017年6月27日

@author: ywl48338
'''
from autodeploy.AutoCleanDeployment import AutoCleanDeployment
if __name__ == '__main__':
    
    tomcat="D:\\apache-tomcat-8.0.44"
    
    cleanDeploy=AutoCleanDeployment(tomcat)
    cleanDeploy.clean()