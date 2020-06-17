import pyttsx3
import datetime
import wikipedia
import speech_recognition as sr
import webbrowser
import os
import smtplib
import random
import pyautogui
import psutil


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir !")

    elif hour>=12 and hour<18:
        speak("Good Afternoon! Sir")   

    else:
        speak("Good Evening! Sir")  

    speak(" I am Jarvis , Please tell me how may I help you today ?") 

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"

    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your_email', 'your_pass')
    server.sendmail('your_email', to, content)
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save("D:\\ASHOK\\Projects\\Virtual_assis\\Screenshots\\ss.png")

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at' + usage)
    battery = psutil.sensors_battery()
    speak('Battery is approx')
    speak(battery.percent)

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        #Logic for Executing tasks based on Query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'search in chrome' in query:
            speak("What Should I Search ? ")
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = takeCommand().lower()
            webbrowser.get(chromepath).open_new_tab(search+'.com')

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'D:\\Songs\\new songs'
            songs = os.listdir(music_dir)
            d = random.choice(songs)    
            os.startfile(os.path.join(music_dir, d))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\User\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open calculator' in query:
            codePath = "C:\\Windows\\System32\\calc.exe"
            os.startfile(codePath)

        # elif 'open calendar' in query:
        #     codePath = "C:\\Users\\User\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        #     os.startfile(codePath)

        elif 'open Notepad' in query:
            cPath = "C:\\Users\\User\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad"
            os.startfile(cPath)

        elif 'open word' in query:
            codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\Word 2013"
            os.startfile(codePath)

        elif 'open powerpoint' in query:
            codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\PowerPoint 2013"
            os.startfile(codePath)

        elif 'open My Computer' in query:
            codePath = "C:\\Users\\User\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\This PC"
            os.startfile(codePath)

        elif 'remember that' in query:
            speak("What Shoud I remember ?")
            data = takeCommand()
            speak("you said me to remember that !" + data)
            remember = open('data.txt','w')
            remember.write(data)
            remember.close()

        elif 'do you know anything' in query:
            remember = open('data.txt', 'r')
            speak("you said me to remember that !" + remember.read())

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "receipent_email"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sI am not able to send this email") 

        elif 'screenshot' in query:
            screenshot()
            speak("Screenshot has been successfully captured !") 

        elif 'cpu' in query:
            cpu()

        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")

        elif 'restart' in query:
            os.system("shutdown /r /t 1")

        elif 'offline' in query:
            quit()
