import speech_recognition as sr
import win32com.client as wincl
import pyaudio
import wave
import winsound
import text2speech

class speech2text:
    def _init_(self):
        self.text = None
        self.t = None

    def generatetext(self):

        with sr.AudioFile("speech/tempaud.wav") as source:
            # print 'Speak Anything'
            self.r = sr.Recognizer()
            self.audio = self.r.record(source)
            # self.t = self.audio.get_wav_data(8000,2)
            # print type(self.t)


            try:
                self.text = self.r.recognize_google(self.audio)
                #print('You Said : {}'.format(self.text))
                return self.text
            except:
                text2speech.speak("Couldn't hear you")

    def makeaudiofile(self):
        winsound.Beep(frequency=800, duration=500)
        self.CHUNK = 1024
        self.FORMAT = pyaudio.paInt16  # paInt8
        self.CHANNELS = 2
        self.RATE = 44100  # sample rate
        self.RECORD_SECONDS = 4
        self.WAVE_OUTPUT_FILENAME = "speech/tempaud.wav"

        self.p = pyaudio.PyAudio()

        self.stream = self.p.open(format=self.FORMAT,
                                  channels=self.CHANNELS,
                                  rate=self.RATE,
                                  input=True,
                                  frames_per_buffer=self.CHUNK)  # buffer

        #print("* recording")

        self.frames = []

        for i in range(0, int(self.RATE / self.CHUNK * self.RECORD_SECONDS)):
            self.data = self.stream.read(self.CHUNK)
            self.frames.append(self.data)  # 2 bytes(16 bits) per channel

        #print("* done recording")

        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()

        self.wf = wave.open(self.WAVE_OUTPUT_FILENAME, 'wb')
        self.wf.setnchannels(self.CHANNELS)
        self.wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
        self.wf.setframerate(self.RATE)
        self.wf.writeframes(b''.join(self.frames))
        self.wf.close()
        winsound.Beep(frequency=1600, duration=500)
        return("speech/tempaud.wav")

def listen():
    winsound.Beep(frequency=800, duration=500)
    r = sr.Recognizer()
    text = None
    with sr.Microphone() as source:
        #print('Speak Anything')
        audio = r.listen(source, phrase_time_limit=3)
        try:
            text = r.recognize_google(audio)
            #print('You Said : {}'.format(text))
            winsound.Beep(frequency=1600, duration=500)
            return text
        except:
            print("Couldn't hear ya")

if __name__ == "main_":
    speak = speech2text()
    speak.makeaudiofile()
    text = speak.generatetext()
    # text = text2speech()
    inp = "You said, " + text
    print(inp)
    #speak.speak(inp)