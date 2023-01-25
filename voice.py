import speech_recognition as sr
import whisper
from gpt import ChatGPT
import pyttsx3
from dotenv import load_dotenv
from os import getenv
import numpy as np
import torch
from time import sleep
from os import system

load_dotenv()

token = getenv("TOKEN")
conversation_id = None

engine = pyttsx3.init()

model = "tiny.en"
audio_model = whisper.load_model(model)


def listen(message):
    print(message, end="")

    r = sr.Recognizer()
    r.energy_threshold = 300
    r.pause_threshold = 2
    r.dynamic_energy_threshold = False

    with sr.Microphone(sample_rate=16000) as source:
        while True:
            # get and save audio to wav file
            audio = r.listen(source)
            torch_audio = torch.from_numpy(
                np.frombuffer(audio.get_raw_data(), np.int16).flatten().astype(np.float32) / 32768.0)
            audio_data = torch_audio

            audio_data = audio_model.transcribe(audio_data, language="english")

            predicted_text = audio_data["text"]
            if len(predicted_text.strip()) > 0:
                print(predicted_text)
                return predicted_text


def speak(text):
    engine.say(text)
    engine.runAndWait()


def main():
    print("Connecting...")
    chatbot = ChatGPT(token, conversation_id, headless=False)
    sleep(5)
    system("cls")
    print("ChatGPT")
    while True:
        try:
            user = listen("You: ")
            bot = chatbot.transcribe_response(user, "ChatGPT: ")
            speak(bot)
        except KeyboardInterrupt:
            chatbot.close()
            break


if __name__ == "__main__":
    main()