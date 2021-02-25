#Python program to send mutiple emails without typing any word

import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener=sr.Recognizer()
engine=pyttsx3.init()

def talk (text):
    engine.say(text)
    engine.runAndWait()

def get_info():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice=listener.listen(source)
            info=listener.recognize_google(voice)   #Use google API
            print(info)
            return info.lower() #Give output in lower characters
    except:
        nope= print("An error occurred")
        return nope

def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('#Mail', '#Password')    #Enter your mail I'd and password here
    email=EmailMessage()
    email['From']='#Mail'      #Enter your mail I'd
    email['To']=receiver
    email['Subject']=subject
    try:
        email.set_content(message)
        server.send_message(email)
    except:
        print("Mail error")

email_list={ '#Name1': '#Mail1',
             '#Name2': '#Mail2',
}

def get_email_info():
    talk('To whom you want to send email?')
    name=get_info()
    receiver=email_list[name]
    print(receiver)
    talk('What is the subject of your email?')
    subject=get_info()
    talk("WHat text you want to keep in your email?")
    message=get_info()
    send_email(receiver, subject, message)
    talk('Hey Vinayak! Your email is sent successfully')
    talk('Do you want to send more email?')
    send_more=get_info()
    if 'yes' in send_more:
        get_email_info()   #For sending more emails

get_email_info()