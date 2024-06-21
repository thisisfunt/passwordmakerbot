import telebot
import random
import config

bot = telebot.TeleBot(config.SECRETKEY)
s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Приветствую, друг!\nЯ бот который поможет тебе создать пароль, который нельзя взломать.\nЧтобы создать напиши мне make (длина пароля)")

@bot.message_handler(content_types=["text"])
def send_info(message):
    if(message.text.lower().split(" ")[0] == "make"):
        lenght = int(message.text.lower().split(" ")[1])
        password = ""
        i = 0
        while(i < lenght):
            password += s[random.randint(0, len(s) - 1)]
            i += 1
        bot.send_message(message.chat.id,"Держи твой пароль: " + password)

bot.polling(none_stop=True)
