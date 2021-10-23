import listen
import text2speech as ts


def getdetails():
    details=[]
    param = None
    while(param is None):
        ts.speak("What should I call you?")
        param=listen.listen()
    details.append(param)
    param = None
    while (param is None):
        ts.speak("How old are you {}?".format(details[0]))
        param = listen.listen()
    details.append(param)
    param = None
    while (param is None):
        ts.speak("What is your gender {}?".format(details[0]))
        param = listen.listen()
    details.append(param)
    param = None
    while (param is None):
        ts.speak("Where do you live {}?".format(details[0]))
        param = listen.listen()
    details.append(param)

    """ts.speak("I would like to know about your hobbies {}?".format(details[0]))
    param = None
    hobby=[]
    while (param is None or param.lower() !="stop"):
        param = None
        while (param is not None):
            param = listen.listen()
        ts.speak("Hobby noted. Say your hobby to add more else say Stop to stop?")
        hobby.append(param)
    details.append(hobby)"""
    return details