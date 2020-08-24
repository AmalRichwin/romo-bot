from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
#creating a new chatbot
chatbot = ChatBot('ROMO')
trainer = ListTrainer(chatbot)
trainer.train(["How are you?",
    "I am good.",
    "That is good to hear.",
    "Thank you",
    "You are welcome.",])
 
#getting a response from the chatbot
response = chatbot.get_response("Bye")
print(response)