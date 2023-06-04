from gtts import gTTS
import os
import speech_recognition as sr
# from playsound import playsound

def say(text):
    print(text)
    tts = gTTS(text=text, lang='en')
    tts.save('audio.mp3')
    # For windows
    # playsound('audio.mp3')
    
    # For Linux
    file = 'audio.mp3'
    os.system("mpg123 " + file)
    
    os.remove('audio.mp3')
    
# say("This is for testing purpose")

def listen():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source2:
             
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=0.2)
             
            #listens for the user's input
            audio2 = r.listen(source2)
             
            # Using google to recognize audio
            MyText = r.recognize_google(audio2,language = 'en-IN',show_all = True)
            # print(MyText)
            MyText = MyText['alternative'][0]['transcript']
            # print(MyText)
            
            MyText = MyText.lower()
 
            print("Did you say ",MyText)
            # say(MyText)
            return MyText
             
    except:
        # print("Could not understand. Please repeat.")
        say("Couldn't understand. Please repeat.")
        return -1
    
# listen()