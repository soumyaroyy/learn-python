import pyttsx3
# engine = pyttsx3.init()
# voices = engine.getProperty('voices') 
# engine.setProperty('voice', voices[15].id)
# engine.say('''Twinkle, twinkle, little star,
# How I wonder what you are!
# Up above the world so high,
# Like a diamond in the sky.
# ''')
# engine.runAndWait()
# engine.stop()

def onStart(name):
   print('starting', name)
def onWord(name, location, length):
   print ('word', name, location, length)
def onEnd(name, completed):
   print ('finishing', name, completed)
engine = pyttsx3.init()
engine.connect('started-utterance', onStart)
engine.connect('started-word', onWord)
engine.connect('finished-utterance', onEnd)
engine.say('The quick brown fox jumped over the lazy dog.')
engine.say('''Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.
''')
engine.runAndWait()