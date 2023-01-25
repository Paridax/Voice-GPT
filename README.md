# ChatGPT Voice
This is a program that allows you to talk to ChatGPT using your voice.
It uses [ChatGPT](https://chat.openai.com/) to generate responses to your voice input.
Unfortunately, the ChatGPT does not have an API, so this program opens the website and relays text between the site
and the Python terminal, so you can talk to ChatGPT using your voice.

## Installation
1. Install Python 3.8 or higher.
2. Install the dependencies using `pip install -r requirements.txt`.
3. Find your OpenAI token:
   * You can find the session token manually from your browser:

    1. Go to https://chat.openai.com/api/auth/session
    2. Press F12 to open console
    3. Go to `Application` > `Cookies``
    4. Copy the session token value in `__Secure-next-auth.session-token`
    5. Paste it into the `.env` file in the current working directory next to `TOKEN=`
4. Find the conversation URL (optional)
   * You can find the conversation URL manually from your browser. Just copy the string of characters after `https://chat.openai.com/chat/` and paste it into the `.env` file in the current working directory next to `CONVERSATION_ID=`
5. Run `python voice.py` to start the program. (there is also a text version, `python text.py`)
6. Say something to ChatGPT. It will respond to you.

Example `.env` file:
```env
TOKEN=<token goes here>
CONVERSATION_ID=<conversation id goes here>
```

## Example
```
--- ChatGPT ---
You: Hello, ChatGPT!
ChatGPT: Hello! How can I help you today?
You: I'm doing, good. Just testing out a project I made.
ChatGPT: That's great! What's the project?
You: It's a program that lets you talk to ChatGPT using your voice.
```
