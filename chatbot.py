from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Step 1: Initialize the ChatBot
chatbot = ChatBot(
    'MyBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.TimeLogicAdapter'
    ],
    database_uri='sqlite:///database.sqlite3'  # Stores conversation data in a SQLite database
)

# Step 2: Train the ChatBot with pre-trained data
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")  # Trains the bot with the English corpus

# Step 3: Start a continuous conversation loop
print("Chatbot is ready! Type 'exit' to end the conversation.")
while True:
    try:
        user_input = input("Ananya: ")
        
        # Exit condition
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        # Get response from chatbot
        response = chatbot.get_response(user_input)
        print("Response:", response)

    except (KeyboardInterrupt, EOFError) as e:
        print("\nChatbot: Goodbye!")
        break