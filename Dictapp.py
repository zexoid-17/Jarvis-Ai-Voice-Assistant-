import os 
import pyautogui
import webbrowser
import pyttsx3
from time import sleep

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    print(f"Speaking: {audio}")  # Debugging print statement
    engine.say(audio)
    engine.runAndWait()

dictapp = {"commandprompt":"cmd","paint":"mspaint","word":"winword","excel":"excel","chrome":"chrome","vscode":"code","powerpoint":"powerpnt"}

def openappweb(query):
    speak("Launching, sir")
    if ".com" in query or ".co.in" in query or ".org" in query:
        query = query.replace("open","")
        query = query.replace("jarvis","")
        query = query.replace("launch","")
        query = query.replace(" ","")
        webbrowser.open(f"https://www.{query}")
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"start {dictapp[app]}")

def closeappweb(query):
    speak("Closing, sir")
    # Define a function to close multiple tabs
    def close_tabs(num_tabs):
        for _ in range(num_tabs):
            pyautogui.hotkey("ctrl", "w")
            sleep(0.5)

    if "one tab" in query or "1 tab" in query:
        close_tabs(1)
        speak("One tab closed")
    elif "2 tab" in query or "two tabs" in query:
        close_tabs(2)
        speak("Two tabs closed")
    elif "3 tab" in query or "three tabs" in query:
        close_tabs(3)
        speak("Three tabs closed")
    elif "4 tab" in query or "four tabs" in query:
        close_tabs(4)
        speak("Four tabs closed")
    elif "5 tab" in query or "five tabs" in query:
        close_tabs(5)
        speak("Five tabs closed")
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"taskkill /f /im {dictapp[app]}.exe")
                speak(f"{app} closed")