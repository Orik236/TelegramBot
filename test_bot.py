import os, random
import requests
import telegram
from telegram.ext import Updater, ConversationHandler, CommandHandler, MessageHandler, Filters
def start(bot, update):
    bot.send_photo(chat_id = update.message.chat_id, photo ="https://cataas.com/cat/says/hello" )
    pass

def cat_with_tag(bot, update, args):
    keyboard = [['cute', 'happy', 'pirate'],
                ['sleep', 'fat', 'halloween'],
                ['loaf', 'wtf', 'facecat']]
    tag = telegram.ReplyKeyboardMarkup(keyboard)
    bot.send_message(chat_id=update.message.chat_id,
                     text="Choose tag",
                     reply_markup=tag)
    user_write = update.message.text
    bot.send_message(chat_id=update.message.chat_id,
                     text=user_write)
    if len(args) == 0:
        bot.send_photo(chat_id = update.message.chat_id, photo = "https://cataas.com/cat/" + user_write)
    else:
        bot.send_photo(chat_id = update.message.chat_id, photo = "https://cataas.com/cat/" + user_write + '/' + " ".join(args))

def cat(bot, update, args):
    if len(args) == 0:
        bot.send_photo(chat_id = update.message.chat_id, photo = "https://cataas.com/cat")
    else:
        user_says = " ".join(args)
        bot.send_photo(chat_id=update.message.chat_id, photo="https://cataas.com/cat/says/" + user_says)

def cat_gif(bot, update, args):
    if len(args) == 0:
        bot.send_animation(chat_id = update.message.chat_id, animation="https://cataas.com/cat/gif")
    else:
        bot.send_animation(chat_id = update.message.chat_id, animation = "https://cataas.com/cat/gif/says/" + " ".join(args))

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url

def dog(bot, update):
    url = get_url()
    bot.send_photo(chat_id = update.message.chat_id, photo = url)
    pass

def girlfriend(bot, update):
    girl = ['Собака', 'Няшка', 'Любимая', 'Хозяйка', 'Госпожа', 'Овца', 'Дура', 'Милашка', 'Бегемотик', 'Стерва']
    bot.sendMessage(chat_id=update.message.chat_id, text = girl[random.randint(0, len(girl))])
    pass

def boyfriend(bot, update):
    boy = ['Господин', 'Любовь', 'Защитник', 'Баран', 'Козел', 'Жаным', 'Албасты', 'Кобель', 'Солнышко', 'Любимый']
    bot.sendMessage(chat_id=update.message.chat_id, text=boy[random.randint(0, len(boy))])
    pass

def citation(bot, update):
    Citations = ["Куда один туда и все.\n(c)Нурик", "Махат поху котак бас.\n(с) Эдик",
                 "Вард на 15 секунд,\nА Абыл на час!\n(c) Канат", "Ебать, я телепортируюсь.\n(c) Нурдаудет",
                 "Главное душа.\n(c) Ара", "Свои поймут.\n(c) Нурик", "Я б ее оставил\nПрост по пути было\n(c) Ара"]
    bot.sendMessage(chat_id=update.message.chat_id, text= Citations[random.randint(0, len(Citations))])
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
    dispatcher.add_handler(CommandHandler('john', John))
    dispatcher.add_handler(CommandHandler('today', vanga))
    dispatcher.add_handler(CommandHandler('getdog', dog))
    dispatcher.add_handler(CommandHandler('citata', citation))
    dispatcher.add_handler((CommandHandler('cat', cat, pass_args=True)))
    dispatcher.add_handler((CommandHandler("cat_gif", cat_gif, pass_args=True)))
    dispatcher.add_handler(CommandHandler("cat_tag", cat_with_tag, pass_args=True))


    dispatcher.add_handler(MessageHandler(Filters.command, unknown))
    #updater.start_polling()

    updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)
    updater.bot.set_webhook('https://summerpractice2019.herokuapp.com/' + TOKEN)

    updater.idle()

bot = telegram.Bot(token=os.environ['NICKNAME_TOKEN'])


if __name__ == '__main__':
    main()
