import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
import os

Lucky = pyttsx3.init()
#.getProperty(): lấy giọng
voice = Lucky.getProperty('voices')
#.setProperty(): Chọn giọng
Lucky.setProperty('voice',voice[1].id)

def speak(audio):
    print("Lucky: " + audio)
    Lucky.say(audio)
    Lucky.runAndWait()
#speak("what can i do for you")

def time():
    Time = datetime.datetime.now().strftime("%I: %M : %p")
    speak(Time)
#time()

def welcome():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <= 12:
        speak("Good morning Trí, How can i help you ?")
    elif hour > 12 and hour <= 18:
        speak("Good evening Trí, How can i help you ?")
    elif hour > 18 and hour <= 24:
        speak("Have Good night Trí, How can i help you ?")
    else:
        speak("Go sleep Trí, your mom will be sad if you are still playing game!") 
#welcome()

def command():
    c = sr.Recognizer()
    with sr.Microphone() as source:
        c.pause_threshold = 2
        audio = c.listen(source)
    try:
        query = c.recognize_google(audio,language='en')
        print("Hồ Minh Trí: " + query)
    except sr.UnknownValueError:
        print("Please repeat or enter the command")
        query = str(input("Your order is: "))
    return query

if __name__== "__main__":
    welcome()
    while True:
        query=command().lower()
        if "google" in query:
            speak("what should i search bro?")
            search=command().lower()
            url = f"https://www.google.com/search?q={search}"
            wb.get().open(url)
            speak(f"Here we go baby: {search} on google")
        if "youtube" in query:
            speak("what should i search bro?")
            search=command().lower()
            url = f"https://www.youtube.com/search?q={search}"
            wb.get().open(url)
            speak(f"Here we go baby: {search} on youtube")
        elif "open video" in query:
            mono=r"D:\Coding\AI-speech\MONO.mp4"
            os.startfile(mono)
        elif "time" in query:
            time()
        if "quit" in query:
            speak("Lucky is quitting bro, see you")
            quit()
        if "music" in query:
            sontung =r"D:\Coding\AI-speech\TUNG.mp4"
            os.startfile(sontung)
        if "open facebook" in query:
            url = f"https://www.facebook.com/razerboy.hmtri/"
            wb.get().open(url)
            speak(f"Here we go baby: facebook of the most handsome guy in the world")
        if "open github" in query:
            url = f"https://github.com/Tristanon"
            wb.get().open(url)
            speak(f"Here we go baby: github for work")