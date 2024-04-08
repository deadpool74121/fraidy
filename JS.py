import smtplib
import time
import pyjokes
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import cv2
from requests import get
import pywhatkit as kit
import secure_smtplib
import sys


engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',170)


#............text to speech..........


def speak(audio):
    print("  ")
    print(f"  {audio}")
    print("   ")
    engine.say(audio)
    engine.runAndWait()

    
#......to convert voice into text...


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...!!")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recogniting...!!")
        querry = r.recognize_google(audio, language='en-in')
        print(f"user said: {querry}\n")
    except Exception as e:
        #speak("say that again please...")
        print("say that again please...")
        return None
    return querry

def wishme():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")
    if hour>=0 and hour<12:
        speak(f"good morning Sir,its {tt}")
    elif hour>=12 and hour<18:
        speak(f"good afternoon Sir,its {tt}")
    else:
        speak(f"good evening Sir,its {tt}")
    speak("i am fraidy sir...,How can I help you")

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your email id ','your password')
    server.sendmail('your email id',to,content)
    server.close()


if __name__=="__main__":
    wishme()
    while True:
        querry = takeCommand().lower()

        #......normal.....conversation

        if 'hello' in querry:
            speak("hello sir ,i am here..!")
        elif 'bye' in querry:
            speak("nice to meet you sir, see you again..!")
        elif 'what are you doing' in querry:
            speak("i am working with you sir...!")
        elif 'bye' in querry:
            speak("nice to meet you sir, see you again..!")
        elif 'thank you' in querry:
            speak("welcome sir")
        elif 'who are you' in querry:
            speak("i am fraidy")
        elif 'birth date' in querry:
            speak("my birth date is 22 november 2023..!")
        elif 'good night' in querry:
            speak("good night sir, sweet dreams")
        elif 'the time' in querry:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"sir,the time is {strTime}")
        elif 'tell me a joke' in querry:
            joke = pyjokes.get_joke()

            speak(joke)

            # .......system operatins.....!


        elif 'open notepad' in querry:
            npath="C:\\Windows\\notepad.exe"
            os.startfile(npath)
        elif 'open word' in querry:
            wpath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(wpath)
        elif 'open point' in querry:
            ppath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            os.startfile(ppath)
        elif 'open excel' in querry:
            epath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
            os.startfile(epath)
        elif 'open google chrome' in querry:
            cpath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome.lnk"
            os.startfile(cpath)
        elif 'open command' in querry:
            ccpath = "C:\\Users\\dorem\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt.lnk"
            os.startfile(ccpath)
        elif 'open control panel' in querry:
            cppath = "C:\\Users\\dorem\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Control Panel.lnk"
            os.startfile(cppath)
        elif 'open run' in querry:
            rpath = "C:\\Users\\dorem\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Run.lnk"
            os.startfile(rpath)
        elif 'open code' in querry:
              cdpath="C:\\Program Files\\JetBrains\\PyCharm Community Edition 2023.2.5\\bin\\pycharm64.exe"
              os.startfile(cdpath)
        elif 'open camera' in querry:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam',img)
                k = cv2.waitKey(50)
                if k == 27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif 'shutdown' in querry:
            os.system("shutdown /s /t 5")
        elif 'restart' in querry:
            os.system("shutdown /r /t 5")
        elif 'sleep' in querry:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")



        #.......close functions........


        elif 'close notepad' in querry:
            speak("ok sir,closing notepad")
            os.system("taskkill /f /im notepad.exe")
        elif 'close word' in querry:
            speak("ok sir,closing word")
            os.system("taskkill /f /im WINWORD.EXE")
        elif 'close powder point' in querry:
            speak("ok sir,closing power point")
            os.system("taskkill /f /im POWERPNT.EXE")
        elif 'close excel' in querry:
            speak("ok sir,closing Excel")
            os.system("taskkill /f /im EXCEL.EXE")    
        elif 'close command' in querry:
            speak("ok sir,closing command prompt")
            os.system("taskkill /f /im cmd.exe")
        elif 'close control panel' in querry:
            speak("ok sir,closing control panel")
            os.system("taskkill /f /im explorer.exe")
        elif 'close chrome' in querry:
            speak("ok sir,closing chrome")
            os.system("taskkill /f /im chrome.exe")
        elif 'close code' in querry:
            speak("ok sir,closing pycharm")
            os.system("taskkill /f /im pycharm64.exe")

        #........set alarm..........

       # elif 'set alarm' in querry:
        #    nn = int(datetime.datetime.now().hour)
         #   if nn==22:'''




        #.....online tasks....!

        elif 'ip address' in querry:
            ip = get('https://api.ipify.org').text
            speak(f"your ip address is : {ip}")
        elif 'wikipedia' in querry:
            speak("searching...")
            querry = querry.replace("wikipedia", "")
            results = wikipedia.summary(querry, sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in querry:
            webbrowser.open("youtube.com")
        elif 'open google' in querry:
            speak("Sir,what should i search on google")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")
        elif 'open facebook' in querry:
            webbrowser.open("facebook.com")
        elif 'open instagram' in querry:
            webbrowser.open("instagram,.com")
        elif 'send message' in querry:
            speak("sir what's msg you should send..")
            cd = takeCommand().lower()
            kit.sendwhatmsg('+919352846442',f"{cd}",1,)
        elif 'play song on youtube' in querry:
            speak("which music play??")
            ce = takeCommand().lower()
            kit.playonyt(f"{ce}")
        elif 'send email' in querry:
            try:
                speak("what should i say?")
                content = takeCommand().lower()
                to = "kumarsatyam54255@gmail.com"
                sendEmail(to,content)
                speak("email has been sent...")
            except Exception as e:
                #print(e)
                speak("sorry sir , email can't be sent")

        elif 'so jao' in querry:
            speak("ok sir , thank you have a good day")
            sys.exit()
        elif 'no thanks' in querry:
            speak("ok sir , thank you have a good day")
            sys.exit()
        #speak("sir do you have other work..")

