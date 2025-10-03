import telebot

# Вставь сюда свой токен от BotFather
TOKEN = "ВАШ_ТОКЕН"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой тестовый бот 💅")

bot.polling()
