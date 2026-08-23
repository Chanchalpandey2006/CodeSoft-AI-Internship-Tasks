print("=== Rule-Based Chatbot ===")
print("Type 'bye' to exit.")

responses = {
    "hello": "Hello! How can I help you?",
    "hi": "Hi! Nice to meet you.",
    "how are you": "I'm doing well. Thanks for asking!",
    "what is your name": "I am a simple rule-based chatbot.",
    "help": "You can greet me, ask my name, or ask how I am."
}

while True:
    user_input = input("\nYou: ").strip().lower()
    if user_input == "bye":
        print("Bot: Goodbye! Have a great day.")
        break

    for rule, reply in responses.items():
        if rule in user_input:
            print("Bot:", reply)
            break
    else:
        print("Bot: Sorry, I don't understand that yet.")
