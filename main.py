from bot import Bot
from es.data_loader import DataLoader

bot = Bot()
data_loader = DataLoader()

while True:
    user_input = input("[YOU] ")
    if user_input == "exit":
        break
    if user_input == "load_data":
        data_loader.load_data()

    print("[BOT] " + bot.ask(user_input))

