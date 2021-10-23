import subprocess
from statistics import mode

def genSentence(t1,t2,t3,e):
    l=[0,0,0,0,0]
    cmd ='python chatbot/test_api.py -f 192.168.99.100 -c "{}" -c "{}" -c "{}" -e "{}"'.format(t1,t2,t3,e)
    for i in range(2):
        l[i]=subprocess.check_output(cmd)
    try:
        a=mode(l)
    except:
        a=l[1]
    a=a.decode("utf-8")
    a=a.split(":")[1].strip()
    a=a.split(a[0])[1]
    return a

if __name__=="__main__":
    a=genSentence("Hello", "Hello, how are you?", "I am fine. How about you?", "joy")
    #print(a)
