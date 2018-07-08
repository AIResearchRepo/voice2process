import os
import platform

"""
This function will say the help function
"""
def help_options():
    options=["Virtual Machine","4GB RAM","AWS"]
    data = "create %s with %s on %s" % tuple(options)
    return data

"""
This function will convert from text to speech
"""
def speak_text(data="I am unable to process the request"):
    if platform.system() == 'Darwin':
        os.system("say %s"%data)
    elif platform.system() == 'Linux':
        os.system("echo %s | festival --tts"%data)
    else:
        print "I am unable to dectect your OS"

    