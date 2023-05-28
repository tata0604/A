import random

# Define some responses for the chatbot
responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm doing well, thank you!", "I'm fine, thanks for asking.", "Pretty good!"],
    "what would you like to see": ["I am looking for a phone", "Do you have good quality headphones?"],
    "what is your budget": ["Around 3000", "I have an open budget"],
    "what brand are you looking for": ["Samsung", "Nokia", "Redmi"],
    "would you like to see something else": ["No thats it thankyou!", "Yes please"],
    "yes":["ok"],
    "default": ["I'm sorry, I didn't understand what you said.", "Can you please rephrase that?", "I'm not sure what you mean."]
}

# Define a function to respond to user input
def chatbot_response(user_input):
    if user_input.lower() in responses:
        return random.choice(responses[user_input.lower()])
    else:
        return random.choice(responses["default"])

# Chat with the user
print("Hi, I'm a simple chatbot. What can I help you with today?")
while True:
    user_input = input("you : ")
    if user_input.lower() == "bye":
        print("Goodbye!")
        break
    else:
        print(f"BOT : {chatbot_response(user_input)}")