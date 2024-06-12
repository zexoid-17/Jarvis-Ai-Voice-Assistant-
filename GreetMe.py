import datetime
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    print(f"Speaking: {audio}")
    engine.say(audio)
    engine.runAndWait()

import sys
print(sys.path)


def greetMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning, sir")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon, sir")
    else:
        speak("Good Evening, sir")
    speak("Please tell me, how can I help you?")

