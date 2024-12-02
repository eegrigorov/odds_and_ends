from pyowm import OWM
import telebot

bot = telebot.TeleBot("7845372713:AAG43QwfLNzsVj9rMMpD5XpJDks1gSuyaqI")
owm = OWM('f24f64157f295b0305abe3a8b771f008')
mgr = owm.weather_manager()

@bot.message_handler(content_types=['text'])
def send_echo(message):
    observation = mgr.weather_at_place(message.text)
    w = observation.weather
    temp = w.temperature('celsius')["temp"]
    answer = "В городе " + message.text + " сейчас " + w.detailed_status + "\n"
    answer += "Температура: " + str(temp)

    bot.send_message(message.chat.id, answer)

bot.polling(none_stop = True)