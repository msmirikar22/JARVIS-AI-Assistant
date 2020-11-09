import pyttsx3
import pywin32_system32
import datetime
import speech_recognition as sr 
import wikipedia 
import googlesearch
import smtplib


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

def sendEmail(to, content):
    server = smtplib.SMTP(['smtp.gmail.com', [465]])
    server.ehlo()
    server.starttls()
    
    server.sendmail('madhura.mirikar@gmail.com', to, content)
    server.close()



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
        elif 'google' in query:
            speak("Searchinhg Madam")
            query = query.replace("google","")
            try: 
                  from googlesearch import search 
            except ImportError:  
                  print("No module named 'google' found") 
            
             
            for j in search(query, tld="co.in", num=10, stop=10, pause=2): 
                    print(j) 
        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = ['mirikarshriya@gmail.com']
                sendEmail(to,content)
                speak("An email has been sent")
            except Exception as e:
                speak("Unable to send the email")

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

                
        

            






        







