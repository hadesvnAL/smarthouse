from speechtoyou import speechtoyou
from youtospeech import youtospeech

you = speechtoyou()

if "chào" in you:
    youtospeech("chào bạn")

elif (you=="Bạn tên gì"):
    youtospeech("tôi là trợ lý ảo quán trà ai")
else:
    youtospeech("xin lỗi tôi chưa thông minh nên không hiểu câu này")