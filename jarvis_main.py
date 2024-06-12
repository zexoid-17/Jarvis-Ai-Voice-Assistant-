import pyttsx3
import speech_recognition as sr
import pyaudio
import datetime
import wikipedia
import webbrowser
import pywhatkit
from bs4 import BeautifulSoup
import requests
import datetime

# Initialize the text-to-speech engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    print(f"Speaking: {audio}")  # Debugging print statement
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, timeout=4)

    try:
        print("Understanding..")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except sr.UnknownValueError:
        print("Sorry, I did not understand that. Could you say that again?")
        return "None"
    except sr.RequestError:
        print("Sorry, my speech service is down. Please try again later.")
        return "None"
    except Exception as e:
        print(f"An error occurred: {e}")
        return "None"
    return query.lower()

import sys
print(sys.path)


if __name__ == "__main__":
    print("Program Started")  # Debugging print statement
    while True:
        query = takeCommand()
        if query != "None" and "wake up" in query:
            try:
                from GreetMe import greetMe
                greetMe()
            except ImportError:
                print("GreetMe module not found.")
                break
            except Exception as e:
                print(f"An error occurred while calling greetMe: {e}")
                break

            while True:
                query = takeCommand()
                if query != "None" and "go to sleep" in query:
                    speak("Okay sir, you can call me anytime.")
                    break
                
                
                ## conversation
                elif "hello" in query:
                    speak("Hello sir, how are you ?")
                elif "i am fine" in query:
                    speak("that's great, sir")
                elif "how are you" in query:
                    speak("Perfect, sir")
                elif "thank you" in query:
                    speak("you are welcome, sir")
                      
                    #  Open and Close apps/websites :
                    # Open and close apps like word, paint and various websites.   
                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)
                    
                    
                    ##Searching from web
                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)
                    
                    
                    # Temperature
                elif "temperature" in query:
                    search = "temperature in delhi"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                elif "weather" in query:
                    search = "temperature in delhi"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                    
                    
                    # Time
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")    
                    speak(f"Sir, the time is {strTime}")
                    
                    #   Finally sleep
                elif "finally sleep" in query:
                    speak("Going to sleep,sir")
                    exit()
                    
                    
               
                    
               
                
                    
                

