import telebot

TOKEN = "8337610302:AAGgbxMWrTWTcERD_YeVk3_hWDJscx3Bhxw"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Привет!")

if __name__ == "__main__":
    bot.polling(none_stop=True)
