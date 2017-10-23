'''
Created on 2017年6月26日

@author: ywl48338
'''
import urllib.request
if __name__ == '__main__':
    f = urllib.request.urlopen('http://music.baidu.com/data/music/file?link=&song_id=1128053')    
    data = f.read()    
    with open('F:/test/BingYus.mp3', 'wb') as code:    
        code.write(data)  
    pass