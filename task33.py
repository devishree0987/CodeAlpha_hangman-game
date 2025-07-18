def get_bot_response(user_input):
    """
    Determines the chatbot's response based on the user's input.
    """
    user_input_lower = user_input.lower() # Convert input to lowercase for case-insensitive matching

    if "hello" in user_input_lower or "hi" in user_input_lower:
        return "Hi there! How can I help you today?"
    elif "how are you" in user_input_lower:
        return "I'm just a program, but I'm doing great! Thanks for asking."
    elif "what is your name" in user_input_lower:
        return "I don't have a name. I'm a simple chatbot created to assist you."
    elif "bye" in user_input_lower or "goodbye" in user_input_lower:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand that. Can you rephrase or ask something else?"

def start_chatbot():
    """
    Starts the interactive chatbot conversation.
    """
    print("--- Welcome to the Basic Chatbot! ---")
    print("Type 'bye' or 'goodbye' to exit the conversation.")
    print("-" * 30)

    while True:
        user_message = input("You: ")
        
        # Get the bot's response
        bot_response = get_bot_response(user_message)
        
        print(f"Chatbot: {bot_response}")
        
        # Check if the user wants to exit
        if "bye" in user_message.lower() or "goodbye" in user_message.lower():
            break

    print("\n--- Chatbot session ended. ---")

if __name__ == "__main__":
    start_chatbot()