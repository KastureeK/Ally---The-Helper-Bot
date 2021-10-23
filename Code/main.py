import RunFile
import depressioncalc
import syslog
import speechemo
import textemo
import id3_decide
import chat
import text2speech
import listen
import getpass
import os
import configparser
import getdetails
import winsound
import random
import sendemail


def checkuser(name):

    if os.path.isdir(os.path.join('.', name)):
        return True
    return False


def registeruser():

    os.mkdir(os.path.join('.', getpass.getuser()))
    makeconfig()


def makeconfig():

    details = getdetails.getdetails()
    config = configparser.ConfigParser()
    cfile = open("config.ini", 'w')
    config.add_section("Details")
    config.set("Details", "User", getpass.getuser())
    config.set("Details", "Name", details[0])
    config.set("Details", "Age", details[1])
    config.set("Details", "Sex", details[2])
    config.set("Details", "Location", details[3])
    config.set("Details", "Contact number", "Add here")
    config.set("Details", "Contact email", "Add here")
    config.set("Details", "Blood Group", "Add here")

    """config.add_section("Hobbies")
    for i in range(len(details[4])):
        config.set("Hobbies",'hobby{}'.format(i),details[4][i])"""

    config.add_section("Medical Conditions")
    config.set("Medical Conditions", 'Walking', "0")
    config.set("Medical Conditions", 'Eyesight', "0")

    config.add_section("Emergency Contact")
    config.set("Emergency Contact", "Contact email", "Add here")
    config.set("Emergency Contact", "Name", "Add here")
    config.set("Emergency Contact", "Address", "Add here")
    config.write(cfile)


def givechoice(chs, listenob):

    text2speech.speak("would you like to chat or shall i start some {}?".format(chs))
    aud = listenob.makeaudiofile()
    txt = listenob.generatetext()
    if "chat" in txt.lower():
        return False
    else:
        return True


def main():

    t1 = "hello ally"
    t2 = "Hello, how are you?"
    listenob = listen.speech2text()
    rfile = RunFile.RunFile()
    if checkuser(getpass.getuser()):
        i = 0
        while True:

            aud = listenob.makeaudiofile()
            txt = listenob.generatetext()
            #print(txt)
            #print(txt)
            if "shutdown" in (txt.lower()):
                break
            elif "hello" in (txt.lower()):
                text2speech.speak("Hello, how are you?")
            else:
                if i == 1:
                    emo_s = speechemo.speechemo(aud)
                    emo_t = textemo.textemo(txt)
                    #print(emo_t)
                    #print(emo_s)
                    decision = "chat"
                elif i % 5 == 0 and i > 0:
                    emo_s = speechemo.speechemo(aud)
                    emo_t = textemo.textemo(txt)
                    #print(emo_t)
                    #print(emo_s)
                    emo=emo_s+emo_t
                    emo=emo//2
                    decision, para = id3_decide.decide(emo)
                else:
                    decision = "chat"

                if decision == "RUNFILE":
                    if para == "Movie":
                        if givechoice("movie", listenob):
                            par = os.listdir("movies")
                            par = ["movies/{}".format(i) for i in par]
                            #print(par)
                            par = random.choice(par)
                            rfile.rfil(par, 0, 1)
                            continue
                    elif para == "Song":
                        if givechoice("Song", listenob):
                            par = os.listdir("songs")
                            par = ["songs/{}".format(i) for i in par]
                            #print(par)
                            par = random.choice(par)
                            rfile.rfil(par, 0, 1)
                            continue
                    elif para == "Excercise":
                        if givechoice("Excercise", listenob):
                            par = os.listdir("exercises")
                            #print(par)
                            par = ["exercises/{}".format(i) for i in par]
                            rfile.rfil(random.choice(par), 0, 1)
                            continue
                elif decision == "CBT":
                    dep = depressioncalc.Calculate()
                    res = dep.calc()
                    syslog.adddreslog(res)
                    continue
                elif decision == "failsafe":
                    sendemail.sendmail()
                    winsound.Beep(800, 3000)
                    break
                elif decision=="Walk":
                    text2speech.speak("I suggest you to go on a walk. It seems like a nice evening.")
                e = "joy"
                if (emo_s + emo_t) // 2 == 2:
                    e = "neutral"
                reply = chat.genSentence(t1, t2, txt, e)
                text2speech.speak(reply)
                syslog.addchatlog(txt + "," + reply.replace(",","\,") + "," + str(emo_s) + "," + str(emo_t))
                t1 = txt
                t2 = reply
            i = i + 1
    else:
        registeruser()

if __name__ == "__main__":
    main()
