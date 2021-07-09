from gtts import gTTS
import playsound

text = "Em nhà ở đâu thế" 
output = gTTS(text,lang="vi", slow=False)
output.save("output.mp3")
playsound.playsound('output.mp3', True)