from speechtotext import speechtotext
from texttospeech import texttospeech

text = speechtotext()

if (text=="Hello"):
    texttospeech("chào bạn")
elif (text=="Bạn tên gì"):
    texttospeech("tôi là trợ lý ảo quán trà ai")
else:
    texttospeech("xin lỗi tôi chưa thông minh nên không hiểu câu này")