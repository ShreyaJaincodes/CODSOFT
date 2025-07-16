def chatbot():
    print("🤖 Chatbot: Hello! I am your simple chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower()

        if "hello" in user_input or "hi" in user_input:
            print("🤖 Chatbot: Hi there! How can I help you?")
        elif "how are you doing" in user_input:
            print("🤖 Chatbot:  great  😄")
        elif "can i ask you something" in user_input:
            print("🤖 Chatbot: yes you can ask anything")
        elif "do you know python" in user_input:
            print("🤖 Chatbot: yes, i am built using that only")
            break
        elif "do you know about laptop" in user_input:
            print("🤖 Chatbot: Looking for laptops? Try Dell, HP, or Lenovo!")
        else:
            print("🤖 Chatbot: Sorry, I didn't understand that.")

# Run the chatbot
chatbot()
