'''
Created on 2017年7月25日

@author: ywl48338
'''
import codecs

if __name__ == '__main__':
    
    '''
    dto文件路径
    '''
    dtoFilePath="D:\\workspace_dev\\tc.tmc.manualitemsapi\\app\\biz\\src\\main\\java\\com\\ly\\flight\\tmc\\manualitemsapi\\biz\\vo\\refund\RefundCallBackRequestVO.java";
    attributeParams=[];
    dtoName="";
    
    #读取文件,获取类名和属性集合
    dtoFile=codecs.open(dtoFilePath,"r","utf-8");
    
    dtoClassName=(dtoFilePath.split("\\")[-1]);
    dtoName=dtoClassName[:-5]
    #print(dtoName);
    lines=dtoFile.readlines();
    for line in lines:
        if line.find("private")>0 and line.find("static")<0:
            tempParam=line[line.find("private"):line.find(";")];
            arrayParam=tempParam.split(" ")[2:]
            for p in arrayParam:
                if p:
                    attributeParams.append(p)
            #attributeParams.append(tempParam.split(" ")[2])
    
    print("public static "+dtoName+" VO2DTO("+dtoName[:-3]+"VO input){");
    print("if (null!=input){");
    print(dtoName+ " output=new "+dtoName+"();");
    for attr in attributeParams:
        #print(str(attr[0]).upper())
        setParam="output.set"+str(attr[0]).upper()+attr[1:]+"(";
        #print(setParam)
        getParam="input.get"+str(attr[0]).upper()+attr[1:]+"());";
        print(setParam+getParam)
    
    print("return output;")
    print("}")
    print("return null;")
    print("}")
        