from gtts import gTTS
import os 

# The text that you want to convert to audio
mytext='guia'

# Language in which you want to convert
language = 'pt-br'

myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
myobj.save(mytext+".mp3")

os.system("data\\audio\\output\\" + mytext + ".mp3"+" tempo 1.0")