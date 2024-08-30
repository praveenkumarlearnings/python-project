import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
a=0
b=0
c=1


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source,timeout=3,phrase_time_limit=6)
            command="waiting"
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'leo' in command:
                command = command.replace('leo', '')
                print(command)
                return command
    except:
        return command
    

def run_leo():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime("%m/%d/%Y, %h :%M :%S")
        talk('Current time is ' + time)

    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'explain about' in command:
        person = command.replace('explain about', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)


    elif 'calculate' in command:
        global a
        if '+' in command:
            ans=command.split()
            for i in ans:
                if i.isnumeric():
                    a+=int(i)
        print("The answer is ",a)
        talk(f"The answer is {a}")

        global b
        elif '-' in command:
            ans = command.split()
            for i in ans:
                if i.isnumeric():
                    b -= int(i)
        print("The answer is ", b)
        talk(f"The answer is {b}")

        elif  'multiply' in command:
            ans = command.split()
            m=[]
            for  i in ans:
                if i.isnumeric():
                    m.append(i)
            mul=m[0]*m[1] 
        print("The answer is ", mul)
        talk(f"The answer is {mul}")

        global d
        if '/' in command:
            ans = command.split()
            for i in ans:
                if i.isnumeric():
                     d/= int(i)
        print("The answer is ", d)
        talk(f"The answer is {d}")


    elif 'date' in command:
        talk('sorry, I have a headache')

    elif ' are you single' in command:
        reply='I am in a relationship with my beste'
        print(reply)
        talk(reply)

    elif 'joke' in command:
        joke=pyjokes.get_joke()
        print(joke)
        talk(joke)

    else:
        talk('please say the command again.')
while True:
    run_leo()
