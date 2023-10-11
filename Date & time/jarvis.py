import pyttsx3 #install pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import smtplib
engine = pyttsx3.init('sapi5')
voices =engine.getProperty("voices")
print(voices[1].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
     hour = int(datetime.datetime.now().hour)
     if hour >=0 and hour<12:
         speak("good morning ")
     else :
        speak("good evening ")
     speak("My name is jarvis  \n how may i help you sir")
def takeCommand():
    '''
    it takes microphone input from user and return string output

    '''
    r = sr.Recognizer()
    with sr.Microphone() as source :
        print("listening")
        r.pause_threshold ==1
        audio = r.listen(source)
    try:
      print("recognising")

      query = r.recognize_google(audio , language='en-in' )
      print(f"user said :{query}\n")
    except Exception as e :
        print(e)
        return "none"
    return query
# def sendEmail(to, content):
#     server = smtplib.SMTP("smtp@gmail.com",587)
#     server.ehlo()
#     server.starttls()
#     server.login("sbbhardwaj143@gmail.com","Shubham@1234#")
#     server.sendmail("sbbhardwaj143@gmail.com", to ,content)
#     server.close()
def start():
    for i in range(2) :
        query =  takeCommand().lower()
        print(query)


        if "wikipedia" in query:
               speak("searching wikipedia")
               query= query.replace("wikipedia","")
               results = wikipedia.summary(query, sentences=2)
               speak("according to wikipedia")
               print(results)
               speak(results)


        elif "open youtube" in query :
            print("Opening Youtube Please Wait")
            webbrowser.open("youtube.com")

        elif "google" in query :
            print("Opening  Please Wait")
            webbrowser.open("google.com")

        elif "play music" in query :
            print("Opening Please Wait")
            music_dir = 'C:\\Users\\bhardwaj\\Desktop\\English Song New'
            songs = os.listdir(music_dir)
            print(songs)
            choose_song = int(input("enter the number of song you want to play"))
            os.startfile(os.path.join(music_dir, songs[choose_song]))
        elif "time" in query :
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"the time is {strTime}")

        elif "open code" in query :
            print("opening vs code for you")
            codePath = "C:\\Users\\Bhardwaj\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
            os.startfile(codePath)
        # elif "email" in query:
        #     try:
        #         speak("what should i say")
        #         # content =takeCommand()
        #         content = "Hi Shubham Bhardwaj How are you "
        #         to = "bhardwajshubhi3898@gmail.com"
        #         sendEmail(to,content)
        #         speak("email is send")
        #     except Exception as e :
        #         print(e)
        elif "exit" in query :
            speak("gud bye sir")
            exit()
        else :
             speak("you have not given any input or your input is \n not correct")
             print('''Do You Want to give any input
                          1. yes
                          2. No
                          ''')
             speak('''Do You Want to give any input\n press 1 for yes \n 2 for no for exit''')
             chance = int(input("Enter Your Choice:  "))
             if chance==1:
                 start()
             else:
                speak("thank you sir \n see you soon")
                exit()

if __name__ == '__main__':
    speak("Hello Shubham ")
    wishMe()
    start()
