import os
import speech_recognition as sr

SHOW_LOGS = False

def speak(text):
    print(f"Jarvis: {text}")
    safe_text = text.replace("'", "").replace('"', "")
    os.system(f"say '{safe_text}'")

def listen_until_done(timeout_seconds=10):
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 4000 
    recognizer.dynamic_energy_threshold = False 
    recognizer.pause_threshold = 1.2 
    
    with sr.Microphone() as source:
        try:
            audio_data = recognizer.listen(source, timeout=timeout_seconds, phrase_time_limit=20)
            query = recognizer.recognize_google(audio_data)
            return query
        except (sr.UnknownValueError, Exception):
            return ""
