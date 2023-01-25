from gpt import ChatGPT
import pyttsx3
from dotenv import load_dotenv
from os import getenv
from os import system

load_dotenv()

token = getenv("TOKEN")
conversation_id = None

engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def main():
    print("Connecting...")
    chatbot = ChatGPT(token, conversation_id)
    system("cls")
    print("ChatGPT")
    while True:
        try:
            user = input("You: ")
            if len(user.strip()) == 0:
                continue
            bot = chatbot.transcribe_response(user, "ChatGPT: ")
            speak(bot)
        except KeyboardInterrupt:
            chatbot.close()
            break


if __name__ == "__main__":
    main()