import wave, struct, math, random

class BeepGenerator:
  def __init__(self, sample_rate = 44100.00):
    self.audio = []
    self.sample_rate = sample_rate

  def append_silence(self, duration_milliseconds=500):
    num_samples = duration_milliseconds * (self.sample_rate / 1000.0)
    for x in range(int(num_samples)):
      self.audio.append(0.0)
    return

  def append_sinewave(
      self,
      frequency=440.0,
      duration_milliseconds=500,
      volume=1.0):

    num_samples = duration_milliseconds * (self.sample_rate / 1000.0)
    for x in range(int(num_samples)):
      #sine_wave = math.sin(2 * math.pi * frequency * (x / self.sample_rate))
      self.audio.append(volume * math.sin(2 * math.pi * frequency * (x / self.sample_rate)))
    return

  def save(self, file_name, nchannels=1, sampwidth=2):
    wave_file = wave.open(file_name, "w")
    nframes = len(self.audio)
    comptype = "NONE"
    compname = "not compressed"
    wave_file.setparams((nchannels, sampwidth, self.sample_rate, nframes, comptype, compname))

    for sample in self.audio:
      wave_file.writeframes(struct.pack('h', int(sample * 32767.0)))

    wave_file.close()
    return

def generate_random_wav(duration=1.0, frequency=440.0, sample_rate = 44100.0):
  duration = 1.0
  frequency = 440.0
  obj = wave.open('foo.wav', 'w')
  obj.setnchannels(1)
  obj.setsampwidth(2)
  obj.setframerate(sample_rate)
  for i in range(99999):
    value = random.randint(-32767, 32767)
    data = struct.pack('<h', value)
    obj.writeframesraw(data)
  obj.close()


def main():
  print("Doing the thing")
  sample_rate = 44100.0
  bg = BeepGenerator(sample_rate)
  bg.append_sinewave(volume=0.25, duration_milliseconds=100)
  bg.append_silence()
  bg.append_sinewave(volume=0.5, duration_milliseconds=700)
  bg.append_silence()
  bg.save("foo2.wav")

if __name__ == "__main__":
  main()
