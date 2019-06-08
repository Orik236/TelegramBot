import os, random
import requests
import telegram
from telegram import update
from telegram.ext import Updater, ConversationHandler, CommandHandler, MessageHandler, Filters, InlineQueryHandler


def start(bot, updater):
    updater.message.reply_text("Hello")
    pass

def get_url():
    contents1 = requests.get('https://random.dog/woof.json').json()
    url = contents1['url']
    return url

def dog(bot, update):
    url = get_url()
    bot.send_photo(chat_id = update.message.chat_id, photo = url)
    pass

def girlfriend(bot, update):
    girl = ['Собака', 'Няшка', 'Любимая', 'Рабыня', 'Хозяйка', 'Малютка', 'Госпожа', 'Овца']
    bot.sendMessage(chat_id=update.message.chat_id, text = girl[random.randint(0, len(girl))])
    pass

def boyfriend(bot, update):
    boy = ['Господин', 'Любовь', 'Защитник', 'Баран', 'Козел', 'Жаным']
    bot.sendMessage(chat_id=update.message.chat_id, text=boy[random.randint(0, len(boy))])
    pass

def kanat(bot, update):
    Kanat = ['Мент', 'Кана', 'Каракурт', 'Котак']
    bot.sendMessage(chat_id=update.message.chat_id, text=Kanat[random.randint(0, len(Kanat))])
    pass

def citation(bot, update):
    Citations = ['']
    pass

def vanga(bot, update):
    Today=['Сегодня ты бухаешь с Нуриком', 'Сегодня ты чувствуешь себя Арой', 'Сегодня ты дэнсер, как Аза',
           'Сегодня тя отпиздит Нурдик', 'Сегодня ты будешь играть с Кано', 'Сегодня ты спасешь мир с Ану',
           'Сегдня ты будешь спорить с Эдиком']
    bot.sendMessage(chat_id=update.message.chat_id, text= Today[random.randint(0, len(Today))])
    pass

def cancel(bot, updater):
    updater.message.reply_text('GoodByee')

def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="unknown stuff.")
    pass

def John(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="ВАЧА ВАЧА ВАЧА, JOHN CENA!!!!!!")

def main():
    TOKEN = os.environ['NICKNAME_TOKEN']
    PORT = int(os.environ.get('PORT', '8443'))
    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('girlfriend', girlfriend))
    dispatcher.add_handler(CommandHandler('boyfriend', boyfriend))
    dispatcher.add_handler(CommandHandler('kanat', kanat))
    dispatcher.add_handler(CommandHandler('john', John))
    dispatcher.add_handler(CommandHandler('today', vanga))
    dispatcher.add_handler(CommandHandler('getdog', dog))

    dispatcher.add_handler(MessageHandler(Filters.command, unknown))
    #updater.start_polling()

    updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)
    updater.bot.set_webhook('https://summerpractice2019.herokuapp.com/' + TOKEN)

    updater.idle()

bot = telegram.Bot(token=os.environ['NICKNAME_TOKEN'])


if __name__ == '__main__':
    main()
