import speech_recognition as sr
from gtts import gTTS
import os

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Konuşun...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio, language="tr-TR")
        print(f"Anladım: {text}")
        return text
    except sr.UnknownValueError:
        print("Söylenen anlaşılamadı.")
        return ""
    except sr.RequestError:
        print("Servisle iletişim kurulamadı.")
        return ""

def speak(text):
    tts = gTTS(text=text, lang="tr")
    filename = "response.mp3"
    tts.save(filename)
    os.system(f"mpg321 {filename}")
