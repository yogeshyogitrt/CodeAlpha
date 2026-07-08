import random
import datetime

def start_complex_chat():
    """Main function to run the upgraded chatbot."""
    
    print("Chatbot: Hello! I'm an chatbot. Let's talk!")
    print("(Type 'bye', 'exit', or 'quit' to end the chat)")
    print("-" * 50)
    
    user_name = ""
    
    while True:
        user_input = input("You: ").strip().lower()
        
        if user_input in ["bye", "goodbye", "exit", "quit"]:
            responses = ["Goodbye! Have a great day!", "See you later!", "Catch you later!"]
            print(f"Chatbot: {random.choice(responses)}")
            break
            
        elif user_input in ["hello", "hi", "hey", "greetings"]:
            responses = ["Hello there!", "Hi! How can I help you today?", "Hey! What's on your mind?"]
            print(f"Chatbot: {random.choice(responses)}")
            
        elif "my name is" in user_input:
            words = user_input.split()
            user_name = words[-1].capitalize()
            print(f"Chatbot: Nice to meet you, {user_name}!")
            
        elif "what is my name" in user_input:
            if user_name:
                print(f"Chatbot: Your name is {user_name}, of course!")
            else:
                print("Chatbot: I don't know your name yet. You can tell me by saying 'My name is...'")
        
        elif "how are you" in user_input or "how's it going" in user_input:
            responses = [
                "I'm functioning perfectly, thanks for asking!", 
                "Doing great! And you?", 
                "I'm just a bunch of code, but I'm having a good time!"
            ]
            print(f"Chatbot: {random.choice(responses)}")
            
        elif "joke" in user_input or "funny" in user_input:
            jokes = [
                "Why do programmers prefer dark mode? Because light attracts bugs!",
                "How many programmers does it take to change a light bulb? None, that's a hardware problem.",
                "Why did the Python snake cross the road? To get to the other IDE."
            ]
            print(f"Chatbot: Here's one: {random.choice(jokes)}")
            
        elif "time" in user_input:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            print(f"Chatbot: Right now, it is {current_time}.")
            
        elif "who are you" in user_input or "what are you" in user_input:
            print("Chatbot: I am an AI script. I don't have feelings, but I'm great at answering questions!")
            
        else:
            fallbacks = [
                "I'm not quite sure I understand.",
                "Could you rephrase that?",
                "That's interesting! Tell me more.",
                "My programming doesn't cover that yet. Try asking me for a joke or the time!"
            ]
            print(f"Chatbot: {random.choice(fallbacks)}")

if __name__ == "__main__":
    start_complex_chat()
