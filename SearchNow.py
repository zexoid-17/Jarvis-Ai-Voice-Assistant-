import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pywhatkit

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

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    print(f"Speaking: {audio}")  # Debugging print statement
    engine.say(audio)
    engine.runAndWait()

def searchGoogle(query):
    query = query.replace("jarvis", "")
    query = query.replace("google search", "")
    query = query.replace("google", "")
    speak("This is what I found on Google")
    try:
        pywhatkit.search(query)
        result = wikipedia.summary(query, sentences=1)
        speak(result)
    except wikipedia.exceptions.DisambiguationError as e:
        speak("There are multiple results for this search. Please be more specific.")
    except Exception as e:
        speak("No speakable output available")

def searchYoutube(query):
    query = query.replace("jarvis", "")
    query = query.replace("youtube search", "")
    query = query.replace("youtube", "")
    speak("This is what I found for your search!") 
    web = "https://www.youtube.com/results?search_query=" + query
    webbrowser.open(web)
    pywhatkit.playonyt(query)
    speak("Done, Sir")

def searchWikipedia(query):
    query = query.replace("jarvis", "")
    query = query.replace("wikipedia", "")
    query = query.replace("search wikipedia", "")
    speak("Searching from Wikipedia....")
    try:
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia..")
        print(results)
        speak(results)
    except wikipedia.exceptions.DisambiguationError as e:
        speak("There are multiple results for this search. Please be more specific.")
    except Exception as e:
        speak("No speakable output available")

# Main logic to handle commands
if __name__ == "__main__":
    query = takeCommand().lower()

    if query == "none":
        speak("Sorry, I did not understand that.")
    elif "google" in query:
        searchGoogle(query)
    elif "youtube" in query:
        searchYoutube(query)
    elif "wikipedia" in query:
        searchWikipedia(query)
    else:
        speak("Sorry, I didn't understand that command.")
