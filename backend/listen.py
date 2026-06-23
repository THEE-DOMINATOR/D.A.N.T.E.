# By default, D.A.N.T.E. will use OpenAI's Whisper for speech recognition during requests. For better performance, while waiting for its name it will use a smaller model (tbd, but probably Teachable Machine)
# If you want to switch to something else, comment out the code in the functions below to replace it with your own schema. 
# Happy Hacking!

import whisper

def await_wake_word():
    pass # until i find something to put here, just so python doesnt magnificently blow to smithereens (boom)

def listen_to_request():
    pass # same as above, but for listening to the actual request instead of the wake word