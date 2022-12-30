import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import time
import subprocess

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')

def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet_user():
    hour = datetime.datetime.now().hour
    if hour>=0 and hour<4:
        speak("Good Night, have a tight sleep")
    elif hour>=4 and hour<12:
        speak("Good Morning, I am Dexter")
    elif hour>=12 and hour<18:
        speak("Good Afternoon, I am Dexter")
    elif hour>=18 and hour<24:
        speak("Good Evening, hope you had a productive day!")


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement

speak("Loading your AI personal assistant Dexter")

if __name__=='__main__':

    greet_user()
    while True:
        speak("Tell me how can I help you now?")
        statement = takeCommand().lower()
        if statement==0:
            continue

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am Dexter version 1 point O your personal assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome, gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather'
                  'In different cities and get top headline news from times of india')
    
    
        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Black Cat")
    
        elif "bye" in statement or "stop" in statement:
            speak('your personal assistant Dexter is shutting down,Good bye')
            break
    
        elif 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement = statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to wikipedia")
            speak(results)
    
        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)
    
        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)
    
        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)
    
        elif 'time' in statement:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
    
        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)
    
        # elif "camera" in statement or "take a photo" in statement:
        #         ec.capture(0, "robo camera", "img.jpg")
    
        elif 'search' in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)
    
    
        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

        else:
            speak("I am sorry I am not programmed to help you with that!")
    
        time.sleep(3)
