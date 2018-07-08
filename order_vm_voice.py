import time
import speech_recognition as sr 
from helper_api import help_options,speak_text


def data_from_mic(recognizer,microphone):
    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        print "Say Now ..."
        audio = recognizer.listen(source)
        
    
    # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #     update the response object accordingly
    try:
        response["transcription"] = recognizer.recognize_google(audio, key=None, language="en-US", show_all=False)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError as e:
        print "Printing the error trace"
        print e.message
        # speech was unintelligible
        response["error"] = "I am so sorry. I didn't get what you say"

    return response
    

def speech_recognize(count=0):
    # create recognizer and mic instances
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    if(count > 0):
        speak_text("Speak again ")
    else:
        speak_text("How can I help you ?")
        speak_text("For example, say help to display help")
    

    response = data_from_mic(recognizer,microphone)
    if not response["success"]:
        print("I didn't catch that. What did you say?\n")

    # if there was an error, stop the game
    if response["error"]:
        print("ERROR: {}".format(response["error"]))
        speak_text(response["error"])
        speech_recognize(2)
    
    data = response["transcription"]
    if data == 'help':
        data = help_options()
    speak_text(data)
    print data


if __name__ == '__main__':
    speech_recognize()