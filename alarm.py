#alarm.py

from delorean import Delorean
from pydub import AudioSegment
from pydub.playback import play

alarm = False
while alarm == False:
    now = str(Delorean().datetime.time())
    print("The time is ",now)
    if now >= "22:41:00.000000":
        alarm = True
        sound = AudioSegment.from_wav('Echo.wav')
        play(sound)

