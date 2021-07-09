you="giờ"

import datetime
from datetime import datetime

if you =="":
	laika_brain = "I can't hear you,"
elif you == "hello":
	laika_brain = "Hello Hades"
elif you== "today":
	today= date.today()
	laika_brain = today.strftime("%B %d, %Y")
elif you== "giờ":
	giờ=datetime.now()
	laika_brain=giờ.strftime("%H hours %M minutes %S seconds")
else:
	laika_brain = "I'm fine"
print(laika_brain)