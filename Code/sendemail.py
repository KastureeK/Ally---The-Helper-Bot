import smtplib
import configparser
from email.mime import multipart,text


def getemail():
    cf=configparser.ConfigParser()
    cf.read("") #path to config file
    ml=cf['Details']["contact email"]
    #print(ml)
    return ml

def sendmail():
    #print("here")
    rel=getemail()
    ms=multipart.MIMEMultipart()
    sender = "" #sender email
    receiver = "Relative <{}>".format(rel)
    ms['From'] = sender
    ms['To'] = receiver
    ms['Subject'] = "Urgent"
    body = "You are receiving this message because your relative seems to be too depressed and might need urgent attention. Kindly look into it urgently.\nTeam Ally\nGood Luck"
    ms.attach(text.MIMEText(body, 'plain'))
    #print(receiver)

    message = f"""\
    Subject: Urgent
    
    You are receiving this message because your relative seems to be too depressed and might need urgent attention. Kindly look into it urgently.\n Team Ally"""

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login("email", "password")
        text1 = ms.as_string()
        server.sendmail(sender, receiver, text1)

    #print("mail sent")

if __name__=="__main__":
    sendmail()
