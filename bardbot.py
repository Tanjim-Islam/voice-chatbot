from bardapi import BardCookies
import speech_recognition as sr
import pyttsx3


engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


cookie_dict = {
    "__Secure-1PSID" : "",
    "__Secure-1PSIDTS" : "",
    "__Secure-1PSIDCC" : ""
}

bard = BardCookies(cookie_dict=cookie_dict)


recognizer = sr.Recognizer()

while True:
    
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=0.3)
    
    try:
        
        query = recognizer.recognize_google(audio)
        print("You said:", query)
        
        
        reply = bard.get_answer(query)['content']
        print("Bard replied:", reply)
        
        
        speak(reply)
        
    except sr.UnknownValueError:
        print("Sorry, I did not understand the audio.")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

