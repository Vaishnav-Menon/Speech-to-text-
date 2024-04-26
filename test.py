import pyaudio
import speech_recognition as sr
import pyttsx3
import matplotlib.pyplot as plt
import numpy as np

# Function to convert audio to text and plot the audio waveform
def audio_to_text():
    recognizer = sr.Recognizer()
    mic = pyaudio.PyAudio().open(format=pyaudio.paInt16, channels=1, rate=44100, input=True)

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for noise levels
        audio = recognizer.listen(source, timeout=10)  # Record audio for 20 seconds

    try:
        print("Processing...")
        text = recognizer.recognize_google(audio)  # Use Google's speech recognition
        print("You said:", text)
        speak_text(text)  # Speak out the recognized text

        # Plot the audio waveform
        plt.figure(figsize=(12, 4))
        samples = np.frombuffer(audio.frame_data, dtype=np.int16)
        plt.plot(np.linspace(0, len(samples) / 44100, num=len(samples)), samples)
        plt.xlabel("Time (s)")
        plt.ylabel("Amplitude")
        plt.title("Audio Waveform")
        plt.show()
    except sr.UnknownValueError:
        print("Sorry, I could not understand audio.")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

# Function to speak out the recognized text
def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Call the function to start recording and converting audio to text
audio_to_text()
