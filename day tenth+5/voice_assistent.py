import speech_recognition as sr
import pyttsx3
import wikipedia
import ecapture
import datetime
import os
import time
import webbrowser
import subprocess
import _json
import requests
import wolframalpha
import pyjokes



engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')      #0 indicates Male voice and 1 indicates female voice.

'''engine = pyttsx3()
engine = pyttsx3.init()
engine.say("Hello Raghav, how may i help you?")
engine.runAndWait'''

def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = datetime.datetime.now().hour        #manipulates date and time.
    if (hour >= 0 and hour < 12):
        speak("Good Morning Raghav")
        print("Good Morning Raghav")
    elif (hour >= 12 and hour < 18):
        speak("Good Afternoon Raghav")
        print("Good Afternoon Raghav")
    else:
        speak("Good evening Raghav")
        print("Good evening Raghav")

'''r = sr.Recognizer()
with sr.Microphone() as source:                 # use the default microphone as the audio source
    audio = r.listen(source)                    # listen for the first phrase and extract it into audio data

try:
    print("You said " + r.recognize(audio))     # recognize speech using Google Speech Recognition
except LookupError:                             # speech is unintelligible
    print("Could not understand audio")'''


def takeCommand():
    r =sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language = 'en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement
speak("Loading your AI personal assistent")
print("Loading your AI personal assistent")
wishMe()


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    #Enable low security in gmail
    server.login("Your email id", 'Your email password')
    server.sendmail('Your email id', 'Your email password')
    server.close()


if __name__ == "__main__":
    while True:
        speak("Tell me how can i help you now?")
        statement = takeCommand().lower()
        if statement == 0:
            continue


        if ("goodbye" in statement or "ok bye in statement" or "stop" in statement):
            speak("Your personal assistent is shuting down, Tata")
            print("Your personal assistent is shutting down, Tata")
    


        #Now we are going to teach some skills or tasks
        if 'wikipedia' in statement:
            speak("Searching for wikipedia...")
            #statement = statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences = 4)
            speak = ("According to wikipedia")
            print(results)
            speak(results)


        elif 'open youtube' in statement:
            speak("Opening youtube for you")
            webbrowser.open("www.youtube.com")

        
        elif 'open gmail' in statement:
            speak("Opening Gmail for you")
            webbrowser.open("mail.google.com")


        elif 'send email' in statement:
            try:
                speak("What should i say")
                content = takeCommand()
                speak("Whom shoul i send")
                to = input()
                sendEmail(to, content)
                speak("Email has been sent.")
            except Exception as e:
                print(e)
                speak("I am not able to send this email.")


        elif 'open google' in statement:
            speak("Opening google for you")
            webbrowser.open("www.google.com")
            

        elif 'time' in statement:
            time = datetime.datetime.now()       #strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {time}")

        
        elif 'music' or 'spotify' or 'songs' in statement:
            speak("Opening songs for you")
            webbrowser.open("www.spotify.com")


        elif 'latest news' or 'news' in statement:
            speak("Opening news for you")
            webbrowser.open("www.ndtv.com")


        elif 'camera' in statement:
            ec.capture(0, "Camera is here", "img.jpg")


        elif 'search' in statement:
            statement = statement.replace("search", "")
            webbrowser.open(statement)   
        

        elif 'Who are you?' or 'what can you do' in statement:
            speak("I am your voice assistent. I can help you in everything you want me to do from web.")
            speak("Tell me something about you Raghav.")


        elif 'joke' in statement:
            speak(pyjokes.getjoke())
            
            
        elif 'powerpoint presentation' or 'open power point presentation' in statement:
            speak("Opening power point presentation for you")
            ppt = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013"
            os.startfile(ppt)


        elif 'shut up' or 'shut up for sometime' or 'keep yout mouth shut' in statement:
            speak("How can i stop myself for a second without talking with you sir?")


        elif 'please shut up' in statement:
            speak("Okay sir don't hout at me")
            speak("For how much time do you want me to shut my mouth?")
            a = int(takeCommand())
            time.sleep(a)
            print(a)


time.sleep(3)