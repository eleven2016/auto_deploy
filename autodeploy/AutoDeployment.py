'''
Create

@author: ywl48338
'''
import xml.dom.minidom
import subprocess
import os
from time import sleep


class AutoDeployment:
    '''
    classdocs
    '''

    def __init__(self, project, tomcat):
        self.projectPaths = project
        self.tomcatPath = tomcat
        self.projectName = []

    def autoDeploy(self):
        self.__setDefaultConfig()
        ###self.__closeTomcat()
        self.__buildProjects()
        self.__removeFromWebapps()
        self.__deployProject()
        self.__restartTomcat()

    '''
   默认配置
    '''

    def __setDefaultConfig(self):
        self.__getProjectNames()

    '''
    获取工程名称
    '''

    def __getProjectNames(self):
        pomPath = "assembly\\" + "pom.xml"
        for path in self.projectPaths:
            tempPath = path + "\\" + pomPath
            DOMTree = xml.dom.minidom.parse(tempPath)
            collection = DOMTree.documentElement
            element = collection.getElementsByTagName("assembly.name")
            print(element[0].firstChild.nodeValue)
            self.projectName.append(element[0].firstChild.nodeValue)

    '''
    关闭tomcat
    '''

    def __closeTomcat(self):
        sub = subprocess.Popen("tasklist", stdout=subprocess.PIPE)
        out, err = sub.communicate()
        print("ok")
        javaPid = ''
        lines = out.splitlines();
        for line in lines[3:len(lines)]:
            tempPs = line.decode();
            if tempPs.find("java.exe") > -1:
                javaPid = tempPs[tempPs.find("java.exe") + 8:tempPs.find("Console")].lstrip().rstrip()
        if javaPid != "":
            print("tomcat" + javaPid)
            cmdArg = ["taskkill", "/f", "/im", javaPid]
            subprocess.Popen(cmdArg, shell=False)

    # 编译工程
    def __buildProjects(self):
        for path in self.projectPaths:
            print(path)
            cmdArg = ["mvn", "clean", "install", "-Pdev"]
            sub = subprocess.Popen(cmdArg, stdout=subprocess.PIPE, shell=True, cwd=path)
            out, err = sub.communicate()
            lines = out.splitlines();
            for line in lines[3:len(lines)]:
                print(line)

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

    def __deployProject(self):
        for path in self.projectPaths:
            tempPath = path + os.path.sep + "target"
            files = os.listdir(tempPath)
            for file in files:
                if file.find(".war") > -1:
                    self.__copyToWebapps(tempPath + os.path.sep + file)

    def __copyToWebapps(self, filePath):
        readFile = open(filePath, "rb")
        print(os.path.split(readFile.name)[1])
        writeFile = open(self.tomcatPath + os.path.sep + "webapps" + os.path.sep + os.path.split(readFile.name)[1],
                         "wb")
        writeFile.write(readFile.read())

    def __restartTomcat(self):
        tomcatBinPath = self.tomcatPath + os.sep + "bin"
        subprocess.Popen(args="startup.bat", shell=True, cwd=tomcatBinPath)
        sleep(30)