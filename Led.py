import speech_recognition as sr
import pyttsx3
from datetime import date,datetime
from gtts import gTTS
import pyaudio
import playsound
import os
import datetime
import time
import wikipedia
import webbrowser
import serial
laika_mouth = pyttsx3.init()
laika_brain =""
Arduino_Serial = Arduino_Serial('com...',9600)
print Arduino_Serial.readline()



i=0
while i<3:
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("laika: Mời bạn nói: ")
		audio = r.listen(source,timeout=5, phrase_time_limit=5)
		print("laika:...")
		try: 
			you = r.recognize_google(audio,language="vi-VI")
			print("You -->: {}".format(you))
		except:
			i=i+1
			print("laika: Xin lỗi! tôi không nhận được voice!")
			laika_brain = "Mình không nghe được bạn nói, bạn nói lại nhé"
			output = gTTS(laika_brain,lang="vi", slow=False)
			output.save("output.mp3")
			playsound.playsound('output.mp3')
			os.remove('output.mp3')
			continue
		if "chào" in you:
			laika_brain = loichao + "Tôi là laika, trợ lý ảo của bạn. Bạn cần giúp gì không"
			print("laika: ",laika_brain)
		
		elif "bật đèn" in you:
			Arduino_Serial.write('1')
			laika_brain="Ok!Đèn hành lang đang được mở"
			print('you:',you)
			print('laika:',laika_brain)
			output = gTTS(laika_brain,lang="vi", slow=False)
			output.save("output.mp3")
			playsound.playsound('output.mp3')
			break
		elif "Tắt Đèn" in you:
			Arduino_Serial.write('0')
			laika_brain="Ok!Đèn hành lang đang được tắt"
			print('you:',you)
			print('laika:',laika_brain)
			output = gTTS(laika_brain,lang="vi", slow=False)
			output.save("output.mp3")
			playsound.playsound('output.mp3')
			break
		
		elif "tạm biệt" in you:
			laika_brain = "Tạm biệt bạn, hẹn gặp lại"
			output = gTTS(laika_brain,lang="vi", slow=False)
			output.save("output.mp3")
			playsound.playsound('output.mp3')
			break
		else:
			laika_brain = "Xin lỗi phần này tôi chưa được học"

		output = gTTS(laika_brain,lang="vi", slow=False)
		output.save("output.mp3")
		playsound.playsound('output.mp3')
		os.remove('output.mp3')

