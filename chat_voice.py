import speech_recognition as sr
import pyttsx3

def voice_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak something...")
        audio = r.listen(source)
        try:
            return r.recognize_google(audio)
        except sr.UnknownValueError:
            return ""

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()