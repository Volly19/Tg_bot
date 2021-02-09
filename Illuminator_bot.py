import telebot;
bot=telebot.TeleBot('1692809546:AAFkbxpY2OntiQohyh_jryZHXNIouP2Lo54');
name = '';
surname = '';
age = 0;
@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    if message.text == '/help':
    	bot.send_message(message.from_user.id, "Тут будет описание чтобы зарегистрироваться напиши /reg")
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "Как тебя зовут?");
        bot.register_next_step_handler(message, get_name); #следующий шаг – функция get_name
  
def get_name(message): #получаем фамилию
    global name;
    name = message.text;
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?');
    bot.register_next_step_handler(message, get_surname);
def get_surname(message):
    global surname;
    surname = message.text;
    bot.send_message(message.from_user.id, 'Сколько тебе лет?');
    bot.register_next_step_handler(message, get_age);
def get_age(message):
    global age;
    while age == 0: #проверяем что возраст изменился
        try:
             age = int(message.text) #проверяем, что возраст введен корректно
        except Exception:
          bot.send_message(message.from_user.id, 'Цифрами, пожалуйста');
          bot.send_message(message.from_user.id, 'Тебе '+str(age)+' лет, тебя зовут '+name+' '+surname+'?');
    else:
        	bot.send_message(message.from_user.id, 'Напиши /reg');
bot.polling(none_stop=True, interval=0)   