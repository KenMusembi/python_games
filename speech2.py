
###############################################
#############SCRIPT START#########################
##############################################

import speech_recognition as sr

###############################################
# obtain path to "swahili_sample.wav" in the same folder as this script
###############################################

from os import path
AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "swahili_sample.wav")


###############################################
# use the audio file as the audio source
###############################################

r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)  # read the entire audio file


###############################################
# recognize speech using Wit.ai
###############################################

WIT_AI_KEY = "INSERT WIT.AI API KEY HERE"  
# Wit.ai keys are 32-character uppercase alphanumeric strings
try:
    print("Wit.ai thinks you said " + r.recognize_wit(audio, key=WIT_AI_KEY))
except sr.UnknownValueError:
    print("Wit.ai could not understand audio")
except sr.RequestError as e:
print("Could not request results from Wit.ai service; {0}".format(e))
 
###############################################
###############END OF SCRIPT######################
#############################################
