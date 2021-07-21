import pyttsx3
import pywin32_system32
import datetime
import speech_recognition as sr 
import wikipedia 
import webbrowser as wb
import os
import pyautogui
import pyjokes
import psutil

engine = pyttsx3.init()




def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome back Madam")
    
    
    speak("JARVIS at your service. Please tell me how can I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
    
        print(query)

    except Exception as e:
        print(e)
        speak("Say that again please")
        return "None"

    return query



def screenshot():
    img = pyautogui.screenshot()
    img.save("F:\\komal\\vscode\\ss\\ss.png")

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CUP is at'+ usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if 'time' in query:
            time()
        
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak("Searching...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query)
            print(result)
            speak(result)
    
        elif 'search in chrome' in query:
            speak("What should i search ?")
            chromepath='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')
        elif 'logout' in query:
            os.system("shutdown -1")
        
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
        
        elif 'restart' in query:
            os.system("shutdown /r /t 1")
        elif 'play songs' in query:
            songs_dir = 'F:\\komal\\vscode\\music'
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))
        elif 'remember that' in query:
            speak("what should i remember?")
            data = takeCommand()
            speak("you said me to remember that"+data)
            remember = open('data.txt','w')
            remember.write(data)
            remember.close()
        elif 'do you know anything' in query:
            remember = open('data.txt','r')
            speak("you said me to remember that" +remember.read())
        elif 'screenshot' in query:
            screenshot()
            speak("Done!")
        elif 'cpu' in query:
            cpu()
        elif 'joke' in query:
            jokes()

        elif 'offline' in query:
            speak("Bye Bye Madam")

            hour = datetime.datetime.now().hour
            if hour>=6 and hour <12:
                speak("Good Morning Madam. Have a nice day")
                quit()
            elif hour>=12 and hour<16:
                speak("Good Day Madam")
                quit()
            
            elif hour>=16 and hour<21:
                speak("Hope you have a great evening")
                quit()
                
            else:
                speak("Have a good night Madam. Sleep Tight.")
                quit()