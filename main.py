import telebot

# 1. ЗАМЕНИ 'ТВОЙ_ТОКЕН_БОТА' на токен от @BotFather (в кавычках)
TOKEN = '8604764432:AAHJ4CKYoeENiiPgJwElrRD9IZF50FN8r1A'
bot = telebot.TeleBot(TOKEN)

# 2. ЗАМЕНИ 123456789 на свой ID из @userinfobot (без кавычек)
ADMIN_ID = 8019944756

# Имитация базы данных кредитов пользователей
user_credits = {}

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привет! Это бот Pixo. \nКоманды админа: /removecredits [id] [сумма]")

@bot.message_handler(commands=['removecredits'])
def remove_credits(message):
    # Проверка на админа
    if message.from_user.id != ADMIN_ID:
        bot.reply_to(message, "❌ Тебе нельзя использовать эту команду!")
        return

    try:
        # Разбиваем сообщение на части: /removecredits 123 50
        args = message.text.split()
        target_user_id = args[1]
        amount = int(args[2])

        # Здесь логика удаления. Для теста просто выводим сообщение.
        bot.reply_to(message, f"✅ Админ удалил {amount} кредитов у пользователя {target_user_id}")
        
    except (IndexError, ValueError):
        bot.reply_to(message, "⚠ Ошибка! Пиши так: /removecredits 1234567 10")

# Запуск бота
print("Бот запущен!")
bot.infinity_polling()
