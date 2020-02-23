from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os


def setup():
    chatbot = ChatBot('Bot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    trainer='chatterbot.trainers.ListTrainer')
    for file in os.listdir(r'C:\Users\Timothy Lam\Documents\Pycharm Projects\Chatbot\data'):
        convData = open(r'C:\Users\Timothy Lam\Documents\Pycharm Projects\Chatbot\data\\' + file,encoding='latin-1').readlines()
        chatbot.set_trainer(ListTrainer)
        chatbot.train(convData)
        #print("Training completed")
    

setup()
