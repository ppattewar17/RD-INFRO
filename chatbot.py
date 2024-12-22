def chatbot():
    print("chatbot: Hello! How can I help you today?(type 'exit' to end the chat)")
    while True:
        user_input = input("You:").strip().lower()

        if user_input == "exit":
            print("chatbot: Goodbye! Have a great day!")
            break 

        elif "hello" in user_input or "hi" in user_input:
            print("chatbot: Hello! How can i assist you today?")
        elif "how are you?" in user_input:
            print("chatbot: I'm just a program, but I'm here to help you")
        elif "your name" in user_input:
            print("chatbot: I'm a simple rule-Based chatbot")
        elif "time" in user_input:
            from datetime import datetime
            current_time = datetime.now().strftime("%H:%M:%S")
            print(f"chatbot: The current time is {current_time}.")
        elif "weather" in user_input:
            print("chatbot: I'm not connected to the internet, so I can't provide weather updates.")
        else:
            print("chatbot: I'm sorry, I don't understand that.Can you try rephrasing?")

if __name__ =="__main__":
    chatbot()