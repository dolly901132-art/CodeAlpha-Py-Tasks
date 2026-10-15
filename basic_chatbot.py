print("================================")
print("       BASIC PYTHON CHATBOT")
print("================================")

print("Bot: Hello! I am a simple chatbot.")
print("Bot: You can say hello, how are you, or bye.")

while True:

    user_input = input("You: ").lower()

    if user_input == "hello":
        print("Bot: Hi! Nice to meet you.")

    elif user_input == "how are you":
        print("Bot: I'm fine, thanks!")

    elif user_input == "bye":
        print("Bot: Goodbye! Have a nice day!")
        break

    else:
        print("Bot: Sorry, I don't understand that.")

print("Chatbot ended.")