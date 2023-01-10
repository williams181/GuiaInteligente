# Import the required module for text
# to speech conversion
from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os

# The text that you want to convert to audio
mytext = 'Guia Inteligente'

# Language in which you want to convert 
language = 'pt-br'

myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
myobj.save("data\\audio\\output\\audiodescricao.mp3")

# Playing the converted file
os.system("data\\audio\\output\\audiodescricao.mp3")


