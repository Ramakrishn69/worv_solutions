import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
import wavio as wv

freq = 44100
duration = 5

print("Recording...")
recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)
sd.wait()
print("Recording finished.")

write("recording.wav", freq, (recording * 32767).astype(np.int16))
wv.write("recording.wav", recording, freq, sampwidth=2)

print("Playing back recording...")
sd.play(recording, freq)
sd.wait()
print("Playing back finished...")
