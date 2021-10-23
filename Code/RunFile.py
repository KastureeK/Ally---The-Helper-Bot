import os
import time
from mutagen.mp3 import MP3
import math
from pymediainfo import MediaInfo
#import depressioncalc

class RunFile:
    def __init__(self):
        pass
    def rfil(self,filePath,duration,count):
        filePath=os.path.join("path",filePath)
        if("mp3" in filePath.lower()):
            duration=math.ceil((MP3(filePath)).info.length)
        if ("mp4" in filePath.lower()):
            duration = math.ceil(((MediaInfo.parse(filePath)).tracks[0].duration)/1000)
        if(count==1):
            if(duration==0):
                os.startfile(filePath)
            else:
                os.startfile(filePath)
                time.sleep(duration)
        else:
            for i in range(len(filePath)):
                if (duration[i] == 0):
                    os.startfile(filePath[i])
                else:
                    os.startfile(filePath[i])
                    time.sleep(duration[i])

if __name__=="__main__":
    x = "Berzerk.mp3"
    ob=RunFile()
    ob.rfil(x,0,1)
    