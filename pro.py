import nltk
from nltk.chat.util import Chat, reflections

# Download NLTK necessary datasets
nltk.download('punkt')

# Define a set of pattern-response pairs for the chatbot
pairs = [
    (r'Hi|Hello|Hey', ['Hello! How can I help you today?', 'Hi there! How can I assist you?']),
    (r'What is your name?', ['I am a chatbot created by OpenAI.']),
    (r'How are you?', ['I am doing great, thank you for asking! How about you?']),
    (r'(.)(help|assist)(.)', ['I am here to help you! What do you need assistance with?']),
    (r'(.) your favorite color (.)', ['I don\'t have a favorite color, but I can talk about any color!']),
    (r'quit', ['Goodbye! Have a wonderful day!']),
    (r'(.*)', ['Sorry, I didn\'t quite understand that. Can you rephrase?'])
]

# Create the chatbot
def chatbot():
    print("Hello! I am a chatbot. Type 'quit' to end the conversation.")
    chat = Chat(pairs, reflections)
    chat.converse()

# Start the chatbot
if __name__ == "__main__":
    chatbot()