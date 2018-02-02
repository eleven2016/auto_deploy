'''
Created on 2017年6月27日

@author: ywl48338
'''
import os


class AutoCleanDeployment(object):
    '''
    默认把webapps下所有的war工程清除
    classdocs
    '''

    def __init__(self, tomcat):
        self.tomcatPath = tomcat
        self.projectName = []

    def clean(self):
        webapps = self.tomcatPath + os.path.sep + "webapps"

        files = os.listdir(webapps)

        for file in files:
            if file.find(".war") > -1:
                self.projectName.append(file[0:file.find(".war")])

        print(self.projectName)

        self.__removeFromWebapps()

        print("清除完毕")

    # tomcat下删除文件
    def __removeFromWebapps(self):
        webappsPath = self.tomcatPath + os.path.sep + "webapps"
        for name in self.projectName:
            projectPath = webappsPath + os.path.sep + name
            warPath = webappsPath + os.path.sep + name + ".war"
            if os.path.exists(warPath):
                os.remove(warPath)
            self.__removeDir(projectPath)

    def __removeDir(self, dirPath):
        if os.path.exists(dirPath):
            files = os.listdir(dirPath)
            for file in files:
                tempPath = dirPath + os.sep + file
                if os.path.isfile(tempPath):
                    os.remove(tempPath)
                if os.path.isdir(tempPath):
                    self.__removeDir(tempPath)
            os.rmdir(dirPath)
