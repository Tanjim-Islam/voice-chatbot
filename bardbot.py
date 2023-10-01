from bardapi import BardCookies
import speech_recognition as sr
import pyttsx3

# Initialize the Text-to-Speech engine
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Set up Bard API with cookies
cookie_dict = {
    "__Secure-1PSID" : "",
    "__Secure-1PSIDTS" : "",
    "__Secure-1PSIDCC" : ""
}

bard = BardCookies(cookie_dict=cookie_dict)

# Initialize the Speech Recognition engine
recognizer = sr.Recognizer()

while True:
    # Capture voice input
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=0.3)
    
    try:
        # Recognize the speech and convert it to text
        query = recognizer.recognize_google(audio)
        print("You said:", query)
        
        # Get the reply from Bard
        reply = bard.get_answer(query)['content']
        print("Bard replied:", reply)
        
        # Speak the reply
        speak(reply)
        
    except sr.UnknownValueError:
        print("Sorry, I did not understand the audio.")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

