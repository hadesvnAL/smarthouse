import speech_recognition
import datetime
from datetime import datetime

laika_ear = speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
	print("laika: I'm listening")
	audio = laika_ear.listen(mic)
try: 
	you = laika_ear.recognize_google(audio)
except:
	you = ""
print("You:" + you)

if you =="":
	laika_brain = "I can't hear you,"
elif you == "hello":
	laika_brain = "Hello Hades"
elif you== "today":
	today= date.today()
	laika_brain = today.strftime("%B %d, %Y")
elif you== "time":
	time=datetime.now()
	laika_brain=time.strftime("%H hours %M minutes %S seconds")
else:
	laika_brain = "I'm fine"
print(laika_brain)
