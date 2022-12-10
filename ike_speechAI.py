import speech_recognition as sr
import time
import random
from time import ctime
import webbrowser
import pyttsx3
from gtts import gTTS
import playsound
import os
import operator
import math



#This initializes the microphone
r = sr.Recognizer()
def call(text):
    action_call = 'ike', 'hike' #Ike stands for "I know everything", I have included hike to account for misunderstanding 'ike'
    
    text = text.lower()
    
    if action_call in text:
        return True
    return False
#This initializes when Ike cannot understand a question I have asked, or if my voice is uninterpreted
def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            ike_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            ike_speak('Sorry, I did not understand you')
        except sr.RequestError:
            ike_speak('Sorry, my speech service is temporarily unavailable')
        return voice_data
#This sets up the AI, to verbally respond to my queries    
def ike_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' +str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)
#This will save an mp3 file of the audio recorded, but then deletes it after the program is no longer running    
def response(text):
    print(text)
    
    tts = gTTS(text = text, lang = 'en')
    audio = 'Audio.mp3'
    tts.save(audio)
    
    playsound.playsound(audio)
    
    os.remove(audio)

#These are the different queries inside the program, that I can currently ask Ike  
def respond(voice_data):
    if 'what is your name' in voice_data:
        ike_speak('My name is Ike')
        
    if 'what time is it' in voice_data:
        ike_speak(ctime())
    
    if 'search' in voice_data:
        search = record_audio('What can I find for you?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        ike_speak('Here is what I found for' + '' + search)
        
    if 'locate' in voice_data:
        location = record_audio('Where do you want me to locate')
        url = 'https://google.com/maps?q=' + location + '/&amp;'
        webbrowser.get().open(url)
        ike_speak('I have found' + '' + location)
    
    if 'check Wiki' in voice_data:
        wikipedia = record_audio('Searching Wikipedia for')
        url = 'https://wikipedia.org/wiki'
        webbrowser.get().open(url)
        ike_speak('This is what I have found on wikipedia')
        
 #Exits program               
    if 'exit' in voice_data:
        exit()
        

    

        
#this is ikes response when the program is first ran  
ike_speak('How may I help you?')
while 1:
    voice_data = record_audio()
    respond(voice_data)

