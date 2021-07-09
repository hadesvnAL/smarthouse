import pyttsx3
import speech_recognition
from datetime import date,datetime
import wikipedia
import webbrowser
import time
import os 
i=0
while i<5:
	hear = speech_recognition.Recognizer()
	with speech_recognition.Microphone() as mic:
		print('...')
		audio = hear.listen(mic)
	try:
		you = hear.recognize_google(audio)
	except:
		you= ""
	if you=="":
		ai="I can't hear you"
		i=i+1
	elif "today" in you:
		today = date.today()
		ai = today.strftime("%B %d, %Y")
	elif "hi" in you:
		ai = 'Hello'
	elif "time" in you:
		now=datetime.now()
		ai=now.strftime("%H Hours %M Minutes %S Seconds")
	elif 'how are you' in you:
		ai="I'm Fine"
	elif 'how old are you' in you:
		ai="I'm zero year old"
	elif "thank" in you:
		ai='You are welcome'
	elif "name" in you:
		ai="My name is Zec"
	elif 'sleep 5 second' in you:
		ai='Finish'
		time.sleep(5)
	elif 'sleep 10 second' in you:
		ai='Finish'
		time.sleep(10)
	elif 'sleep 1 minute' in you:
		ai='Finish'
		time.sleep(60)
	elif 'shut down' in you:
		os.system('shutdown -s')
	elif 'restart' in you:
		os.system('shutdown -r')
	elif "YouTube" in you:
		webbrowser.open('https://www.youtube.com',new=2)
		ai="Ok!Bye"
		print('Me:',you)
		print('AI:',ai)
		aispeak = pyttsx3.init()
		aispeak.say(ai)
		aispeak.runAndWait()
		break
	elif "Google" in you:
		webbrowser.open('https://www.google.com.vn/',new=2)
		ai="Ok!Bye"
		print('Me:',you)
		print('AI:',ai)
		aispeak = pyttsx3.init()
		aispeak.say(ai)
		aispeak.runAndWait()
		break
	elif "music" in you:
		webbrowser.open('https://www.youtube.com/results?search_query=music',new=2)
		ai="Ok!Bye"
		print('Me:',you)
		print('AI:',ai)
		aispeak = pyttsx3.init()
		aispeak.say(ai)
		aispeak.runAndWait()
		break
	elif "EDM" in you:
		webbrowser.open('https://www.youtube.com/watch?v=KjvM4WJcedA',new=2)
		ai="Ok!Bye"
		print('Me:',you)
		print('AI:',ai)
		aispeak = pyttsx3.init()
		aispeak.say(ai)
		aispeak.runAndWait()
		break
	elif "Facebook" in you:
		webbrowser.open('https://www.facebook.com/',new=2)
		ai="Ok!Bye"
		print('Me:',you)
		print('AI:',ai)
		aispeak = pyttsx3.init()
		aispeak.say(ai)
		aispeak.runAndWait()
		break
	elif "Gmail" in you:
		webbrowser.open('https://mail.google.com/mail/u/0/#inbox',new=2)
		ai="Ok!Bye"
		print('Me:',you)
		print('AI:',ai)
		aispeak = pyttsx3.init()
		aispeak.say(ai)
		aispeak.runAndWait()
		break
	elif "bye" in you:
		ai='GoodBye'
		print('Me:',you)
		print('AI:',ai)
		aispeak = pyttsx3.init()
		aispeak.say(ai)
		aispeak.runAndWait()
		break
	elif you=='Wikipedia':
		hear = speech_recognition.Recognizer()
		with speech_recognition.Microphone() as mic:
			print("Wikipedia: ...")
			audio = hear.listen(mic)
		try:
			wiki = hear.recognize_google(audio)
		except:
			wiki='Sorry'
		wikipedia.set_lang("vi")
		wiki=wikipedia.summary(wiki)
		print(wiki)
		ai='Finish ^.^'
		time.sleep(3)
	elif 'game' in you:
		os.system('python flappybird.py')
		ai='Finish'
	else: ai='Sorry!'	
	print('Me:',you)
	print('AI:',ai)
	aispeak = pyttsx3.init()
	aispeak.say(ai)
	aispeak.runAndWait()
