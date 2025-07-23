def chatbot():
    print("Chatbot: Hello! I’m your friendly chatbot. Ask me anything! (Type 'bye' to exit)\n")
    
    while True:
        user_input = input("You: ").strip().lower()

        
        if any(greet in user_input for greet in ["hello", "hi", "hey"]):
            print(" Chatbot: Hey there! How can I help you today?")
        
        elif "python" in user_input:
            print(" Chatbot: Python is a powerful and beginner-friendly programming language. Great choice!")
        
        elif "laptop" in user_input and "recommend" in user_input:
            print(" Chatbot: I'd recommend Lenovo, Acer, or HP for good performance and value.")
        
        elif "graphic design" in user_input or "graphic designing" in user_input:
            print(" Chatbot: For graphic design, go for a laptop with a strong GPU and color-accurate display. Try MacBook Pro, Dell XPS, or ASUS ZenBook!")
        
        elif "joke" in user_input:
            print(" Chatbot: Why don’t programmers like nature? It has too many bugs!")
        
        elif "bye" in user_input or "exit" in user_input:
            print(" Chatbot: Thanks for chatting with me. Have a great day!")
            break
        
        else:
            print(" Chatbot: Hmm... I didn’t catch that. Try asking about Python, laptops, or tell me to tell a joke!")

# Run the chatbot
chatbot()


