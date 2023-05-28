import random

responses = {
    "hi": ["Hello!", "Hello there...", "Hey!"],
    "how are you": ["Fine, thanks for asking", "I am doing well...."],
    "what is your name": ["My name is Chatbot", "Chat Bot"],
    "default": ["I am sorry, I didn't understand", "Can you please ask another question..."]
}

def chat_response(user_input):
    if user_input.lower() in responses:
        return random.choice(responses[user_input.lower()])
    else:
        return random.choice(responses['default'])

print("Hello, I am a chatbot...")
while True:
    user_input = input()
    if user_input.lower() == 'bye':
        print("Goodbye...")
        break
    else:
        print(chat_response(user_input))
