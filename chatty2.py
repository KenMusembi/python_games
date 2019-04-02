#This is an Input/Output AI Chatbot based on Manual Rules

import os
os.system('color 3f') # sets the background to blue

#make Python speak
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")

#start the conversation
print('Habari!') #greeting
speak.Speak('Habari!')


#keep going the conversation
print('Unaitwa aje?') #ask
speak.Speak('Unaitwa aje?')
Name = input() #save answer
print('Nafurahi kukuona, ' + Name + '!!') #reply
speak.Speak('Nafurahi kukuona, ' + Name + '!!')
print('Jina lako lina maneno:')
speak.Speak('jina lako lina maneno:')
print(len(Name))
speak.Speak(len(Name))

#keep going the conversation
print('Umri yako?') #ask
speak.Speak('Umri yako?')
Reply = input() #save answer
print('Utakuwa na umri ' + str(int(Reply) + 1) + ' mwaka ujao.') #reply
speak.Speak('Utakuwa na umri ' + str(int(Reply) + 1) + ' mwaka ujao.')

#keep going the conversation
print('Nimefurahi kuongea na wewe. Kwaheri, ' + Name) #ask
speak.Speak('nimefurahi kuongea na wewe.  Kwaheri ' + Name)

