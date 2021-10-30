import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os
import random
import webbrowser
# from PyDictionary import PyDictionary
# import googletrans
# import gtts
# import playsound


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)   #for male voice use voice[1]
# translator = googletrans.Translator()

# her_lang = 'ko'

def talk(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        talk("Good morning chumui!")
        talk("I AM JACK HOW MAY I HELP YOU")

    elif hour>=12 and hour < 16:
        talk("Good afternoon chumui!")
        talk("I AM JACK HOW MAY I HELP YOU")

    elif hour>=16 and hour < 21:
        talk("Good evening chumui!")
        talk("I AM JACK HOW MAY I HELP YOU")

    else:
        talk("Good night CHUMUI!")
        talk("I AM JACK HOW MAY I HELP YOU")

def take_Command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jack' in command:
                command = command.replace('jack', '')
                print(command)
    except:
        pass
    return command

if __name__ == "__main__":

   wishMe()

def run_jack():
    command = take_Command()
    if 'play' in command:
        song = command.replace('play', '')
        talk('ok sir, playing' + song)
        pywhatkit.playonyt(song)

    elif 'location' in command:
        data = command.split(" ")
        location = data[2]
        talk("Hold on Frank, I will show you where " + location + " is.")
        os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")

    elif 'my pubg video' in command:
         wet = "C:\\Users\\Chumui\\Desktop\\my pubg"
         songs = os.listdir(wet)
         os.startfile(os.path.join(wet, songs[0]))

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk(f"Sir, the time is{time}")
        #talk('Current time is ' + time)

    elif 'i love you' in command:
        talk('i love you too , you are my life')

    elif 'search' and 'search about' and 'what do you mean by' in command:
        person = command.replace('search or search about or what do you mean by', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'open chrome' in command:
        gld = "C:\\Program Files (x86)\\Google\Chrome\\Application\\chrome.exe"  #use your chrome path from your desktop
        os.startfile(gld)
    elif 'open instagram' in command:
        inst = webbrowser.open('https://www.instagram.com/')
        talk('ok sir open instagram' + inst)
    elif 'open facebook' in command:
        fb = webbrowser.open('https://www.facebook.com')
        talk('ok sir open facebook' + fb)
    elif 'are you single' in command:
        talk('yes my lovely boy')
    elif 'ok good night' in command:
        talk("ok good night my love")
    elif 'hello' in command:
        talk("hello")
    elif 'what is your name' in command:
        talk("my name is jack Tripura")
    elif 'joke' in command:
        jk = pyjokes.get_joke()
        print(jk)
        talk("ok sir" + jk)
    elif 'my folder video' in command:
        music_dir = "C:\\Users\\Chumui\\Music\\musci\\song and video"
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, songs[1]))
    elif 'open my visual studio code' in command:
        vs_code = "C:\\Users\\Chumui\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(vs_code)
    elif 'open facebook' in command:
        webbrowser.open("www.facebook.com")
    #
    # elif 'translate' in command:
    #     tras = translator.translate(text, dest=her_lang)
    #     print(tras.text)
    #     con_audio = gtts.gTTS(tras.text, lang=her_lang)
    #     con_audio.save('alexaji.mp3')
    #     playsound.playsound('alexaji.mp3')
    elif 'my friend' in command:
        talk("my friend sagar is best")

    else:
        talk('please repeat your command')

while True:
    run_jack()
