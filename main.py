import pyttsx3

text_speech = pyttsx3.init()

# changing the rate (defualt: 125)
rate = text_speech.getProperty('rate') 
text_speech.setProperty('rate', 110)

voices = text_speech.getProperty('voices')
text_speech.setProperty('voice', voices[0].id)   #changing index, changes voices. 1 for female

answer = input("Greetings. What did you want me to convert to speech today?")
text_speech.say(answer)

text_speech.runAndWait()
text_speech.stop()

# Using typed text to create custom audio file.

'''
text_speech.save_to_file('Greetings, this is an audio file from Orion. Whie learning this package pyttx3, he was able to create this audio file. Hope you enjoy it.', 'recording.mp3')
text_speech.runAndWait()

'''
