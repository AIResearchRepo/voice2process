import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print (' Say something !!!!');
    audio = r.listen(source)
print ('I got ** '+ r.recognize_google(audio))

try:
    print( 'Google said '+ r.recognize_google(audio))
except:
    pass
    