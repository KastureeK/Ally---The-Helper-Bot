# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 07:44:22 2019

@author: abhid
"""

import speech_recognition as sr
import text2speech as ts
import syslog
import time
import listen



class Calculate:
    
    def __init__(self):
        self.text = None
        self.listenob = listen.speech2text()
    def generatetext(self,i):
        aud = self.listenob.makeaudiofile()
        txt = self.listenob.generatetext()
        return txt
    def calc(self):
        self.questionsnegative = ["Were you bothered by things that usually don't bother you?",
                             "Did you have trouble eating?",
                             "did you feel gloomy even with friends around?", "Do you have trouble concentrating?",
                             "okay, this might sound weird but did you feel depressed?",
                             "Did you feel down and out in life?", "Were you fearful of anything?",
                             "How often were your sleep restless?",
                             "How often did you socialise to people?", "Did you feel lonely?",
                             "Were people unfriendly towards you?",
                             "Mind if I ask if you had crying spells?", "how often did you feel sad",
                             "how often did you get the feeling that people don't like you",
                             "how often did you feel that you couldn't get going?"]
        self.questionspositive = ["Did you feel you were as good as other people?",
                             "Did you feel like everything you did was an effort?",
                             "How did you feel about the future hopeful?", "How often did you feel happy?",
                             "Did you enjoy how you were living? in other words how often did you enjoy life"]

        self.ansneg = 0
        self.anspos = 0
        #speak = speech2text()
        for i in self.questionspositive:
            ts.speak(i)
            self.text = None
            self.text = self.generatetext(5)
            self.resp = str(self.text)
            if self.text == None:
                ts.speak("I was not able to hear you, could you please say that again?")
                self.text = self.generatetext(5)
                self.resp = str(self.text)

            #for k in self.resp:
            k=''
            if "no " in self.resp:
                self.anspos = self.anspos + 3
                k='no'
            elif "not " in self.resp:
                self.anspos = self.anspos + 3
                k = 'not'
            elif "little"  in self.resp:
                self.anspos = self.anspos + 2
                k = 'little'
            elif "frequently"  in self.resp:
                self.anspos = self.anspos + 1
                k="frequently"
            elif "usually" in self.resp:
                self.anspos = self.anspos + 0
                k="usually"
            else:
                self.anspos = self.anspos + 1
                k=self.resp
            syslog.adddeplog("{},{},{},{}".format(self.questionspositive.index(i),self.resp, k, self.anspos))
        for i in self.questionsnegative:
            ts.speak(i)
            self.text = None
            self.text = self.generatetext(5)
            self.resp = str(self.text)
            if self.text == None:
                ts.speak("I was not able to hear you, could you please say that again?")
                self.text = self.generatetext(5)
                self.resp = str(self.text)
            k = ''
            if "no " in self.resp:
                self.ansneg = self.ansneg + 0
                k='no'
            elif "not " in self.resp:
                self.ansneg = self.ansneg + 0
                k = 'not'
            elif "little"  in self.resp:
                self.ansneg = self.ansneg + 1
                k = 'little'
            elif "frequently"  in self.resp:
                self.ansneg = self.ansneg + 2
                k="frequently"
            elif "usually" in self.resp:
                self.ansneg = self.ansneg + 3
                k="usually"
            else:
                self.ansneg = self.ansneg + 1
                k=self.resp
            syslog.adddeplog("{},{},{},{}".format(self.questionsnegative.index(i),self.resp, k, self.ansneg))

        self.final = self.anspos + self.ansneg
        #print(self.final)
        return self.final

if __name__=="__main__":
    dep = Calculate()
    calculatedDep=dep.calc()
    trait = ""
    if(calculatedDep<=15):
        trait = " seems like you are a Happy Person, good going!"
    elif(calculatedDep>15) and (calculatedDep<=30):
        trait = " you seem a bit sad, would you like me to recommend something to you?"
    elif (calculatedDep > 30) and (calculatedDep <= 45):
        trait = " you seem to be going through a rough patch. Do not worry, time flies very past."
    else:
        trait = " I can suggest that asking for help is not bad at all. Would you like me to contact someone close to you?"
    ts.speak("With a score of "+int(calculatedDep)+ trait)