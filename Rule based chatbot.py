import re

print("=" * 50)
print("🤖 Welcome to CodSoft Rule-Based Chatbot")
print("Type 'bye' to exit.")
print("=" * 50)

while True:
    user = input("\nYou: ").lower().strip()

    if user == "bye":
        print("Bot: Goodbye! Have a great day.")
        break

    elif re.search(r"\b(hi|hello|hey)\b", user):
        print("Bot: Hello! How can I help you?")

    elif "how are you" in user:
        print("Bot: I'm doing great. Thanks for asking!")

    elif "your name" in user:
        print("Bot: I am a Rule-Based Chatbot.")

    elif "college" in user:
        print("Bot: That's nice! Which college are you studying in?")

    elif "course" in user:
        print("Bot: I can help with AI, Python, and programming questions.")

    elif "python" in user:
        print("Bot: Python is a powerful programming language used in AI, web development, and data science.")

    elif "ai" in user or "artificial intelligence" in user:
        print("Bot: Artificial Intelligence enables machines to perform tasks that normally require human intelligence.")

    elif "machine learning" in user:
        print("Bot: Machine Learning is a branch of AI where computers learn from data.")

    elif "thank" in user:
        print("Bot: You're welcome!")

    elif "time" in user:
        from datetime import datetime
        print("Bot: Current time is", datetime.now().strftime("%I:%M %p"))

    else:
        print("Bot: Sorry, I don't understand that. Please ask another question.")
