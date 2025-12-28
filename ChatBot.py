from datetime import datetime

def show_menu():
    print("\nAvailable commands:")
    print("- hello")
    print("- how are you")
    print("- what is your name")
    print("- help")
    print("- bye / exit / quit")

def time_greeting():
    hour = datetime.now().hour
    if hour < 12:
        return "Good morning"
    elif hour < 17:
        return "Good afternoon"
    else:
        return "Good evening"

def chatbot():
    print(f"Chatbot: {time_greeting()}! Welcome to the chatbot 😊")
    
    name = input("Chatbot: What's your name? ").strip()
    print(f"Chatbot: Nice to meet you, {name}!")
    
    show_menu()

    # 🔹 UTF-8 encoding added here (FIX)
    with open("chat_history.txt", "a", encoding="utf-8") as file:
        file.write("\n--- New Chat Session ---\n")

        while True:
            user_input = input(f"{name}: ").strip().lower()
            file.write(f"{name}: {user_input}\n")

            if user_input == "hello":
                reply = "Hi! 😊"
            
            elif user_input == "how are you":
                reply = "I'm fine, thanks!"
            
            elif user_input == "what is your name":
                reply = "I am a rule-based chatbot."
            
            elif user_input == "help":
                show_menu()
                continue
            
            elif user_input in ["bye", "exit", "quit"]:
                reply = f"Goodbye, {name}! Have a great day 👋"
                print("Chatbot:", reply)
                file.write("Chatbot: " + reply + "\n")
                break
            
            else:
                reply = "Sorry, I don't understand that."

            print("Chatbot:", reply)
            file.write("Chatbot: " + reply + "\n")

# Run chatbot
chatbot()
