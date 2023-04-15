import random

# Define the chatbot's responses to different user inputs
responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm doing well, thanks!", "Not too bad, thanks for asking.", "I'm just okay."],
    "bye": ["Goodbye!", "Bye-bye!", "See you later!"],
    "jaja": ["to jaja sim homin!", "Vai colocar um hoje!", "Ai mataram o cleitin!"]
}

# Define the function to generate chatbot's response
def respond(input_text):
    if input_text.lower() in responses:
        return random.choice(responses[input_text.lower()])
    else:
        return "I'm sorry, I don't understand. Could you please rephrase?"

# Define the main function to run the chatbot
def main():
    print("Hello! I'm a simple chatbot. How can I help you today?")
    while True:
        user_input = input("> ")
        if user_input.lower() == "quit":
            break
        else:
            bot_response = respond(user_input)
            print(bot_response)

# Run the chatbot
if __name__ == "__main__":
    main()
