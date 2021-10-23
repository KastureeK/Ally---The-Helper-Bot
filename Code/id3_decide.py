import configparser
import datetime
import syslog
import pickle

file1=open("classsave.bin","rb")
classifier=pickle.load(file1)
file1.close()
print("file loaded")

def getdur():
    time=int(str(datetime.datetime.now().time()).split(":")[0])
    if time>=16 and time<20:
        return 4
    elif time>=10 and time<16:
        return 3
    elif time>5 and time<10:
        return 2
    else:
        return 1

def getparmfordec():
    tm=str(getdur())
    nl = str(syslog.getchatlength())
    cf = configparser.ConfigParser()
    cf.read("config.ini")
    d1=str(int(cf["Medical Conditions"]["Walking"]))
    d2=str(int(cf["Medical Conditions"]["Eyesight"]))
    ds = str(syslog.getreslog())
    #print("tm")
    print("tm"+tm)
    print("nl"+nl)
    print("d1"+d1)
    print("d2"+d2)
    print("ds"+ds)
    return tm,nl,d1,d2,ds

def decide(emo):
    return "chat", None

def decide1(emo):
    tm,nl,d1,d2,ds = getparmfordec()
    if(nl==0):
        return "chat", None
    a=[[]]
    a[0].append(tm)
    a[0].append(emo)
    a[0].append(nl)
    a[0].append(d2)
    a[0].append(d1)
    a[0].append(ds)
    a=classifier.predict(a)
    if a[0]==1:
        return "RUNFILE","Movie"
        return "RUNFILE","Movie"
    if a[0]==2:
        return "RUNFILE","Excercise"
    if a[0]==3:
        return "Walk", None
    if a[0]==4:
        return "CBT", None
    if a[0]==5:
        return "chat", None
    if a[0]==6:
        return "failsafe", None
    if a[0]==7:
        return "RUNFILE","Song"

if __name__=="__main__":
    #print("here")
    print(classifier.predict([[1,3,1,0,1,2]]))